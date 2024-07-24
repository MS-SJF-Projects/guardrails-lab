import json
from datetime import datetime, timedelta
from pathlib import Path

from sqlalchemy.orm import Session

from .database import drop_db, get_db, init_db
from .models import Customer, MenuItem, OpeningHours, Order, OrderItem, OrderStatus


async def load_initial_data():
    # Remove any existing database tables
    drop_db()

    init_db()
    print("Database tables created")

    # Get a db session and load data
    db = get_db()
    load_regular_menus(db)
    load_specials(db)
    load_customers(db)
    load_opening_hours(db)
    create_orders(db)



def load_regular_menus(db: Session):

    path = Path(__file__).parent / "init_data" / "menu.json"
    with open(path) as f:
        json_data = json.load(f)

    availability_all_days = {
        "available_monday": True,
        "available_tuesday": True,
        "available_wednesday": True,
        "available_thursday": True,
        "available_friday": True,
        "available_saturday": True,
        "available_sunday": True
    }

    try:

        for category, items in json_data.items():
            for item in items:
                # Create a MenuItem instance with data from JSON and set it to be available every day
                menu_item = MenuItem(
                    name=item["name"],
                    price=item["price"],
                    ingredients=", ".join(item["ingredients"]),
                    category=category,
                    labels=item["label"],
                    **availability_all_days
                )
                # Add the menu item to the session
                db.add(menu_item)

        # Commit the session to save all the new records to the database
        db.commit()

    except Exception as e:
        db.rollback()
        print(f"Error loading data: {e}")

    finally:
        # Close the session
        db.close()

    print("Menu items have been loaded successfully.")



def load_specials(db: Session):
    path = Path(__file__).parent / "init_data" / "specials.json"
    with open(path) as f:
        json_data = json.load(f)

    try:
        for day, items in json_data.items():
            for item in items:
                # Create a MenuItem instance with data from JSON
                special_item = MenuItem(
                    name=item["name"],
                    price=item["price"],
                    ingredients=", ".join(item["ingredients"]),
                    category="Special",  # Use 'Special' as a category to distinguish from regular items
                    labels=item.get("label", ""),
                    available_monday=(day == "Monday"),
                    available_tuesday=(day == "Tuesday"),
                    available_wednesday=(day == "Wednesday"),
                    available_thursday=(day == "Thursday"),
                    available_friday=(day == "Friday"),
                    available_saturday=(day == "Saturday"),
                    available_sunday=(day == "Sunday")
                )
                # Add the special item to the session
                db.add(special_item)

        # Commit the session to save all the new records to the database
        db.commit()

    except Exception as e:
        db.rollback()
        print(f"Error loading specials: {e}")

    finally:
        # Close the session
        db.close()

    print("Specials have been loaded successfully.")



def load_customers(db: Session):

    path = Path(__file__).parent / "init_data" / "customers.json"
    with open(path) as f:
        json_data = json.load(f)

    try:
        # Iterate over each customer in the JSON data
        for customer in json_data:
            # Flatten the nested address into individual fields
            address = customer["address"]
            customer_record = Customer(
                firstname=customer["firstname"],
                lastname=customer["lastname"],
                email=customer["email"],
                external_id=customer["id"],
                card_digits=customer["card_digits"],
                street=address["street"],
                city=address["city"],
                state=address["state"],
                zip=address["zip"],
                country=address["country"],
                special=customer["special"].lower() == "true",  # Convert "true"/"false" string to Boolean
                phone=customer["phone"]
            )
            # Add the customer record to the session
            db.add(customer_record)

        # Commit the session to save all the new records to the database
        db.commit()

    except Exception as e:
        db.rollback()
        print(f"Error loading data: {e}")

    finally:
        # Close the session
        db.close()

    print("Customer data has been loaded successfully.")



def load_opening_hours(db: Session):
    path = Path(__file__).parent / "init_data" / "opening-hours.json"
    with open(path) as f:
        json_data = json.load(f)

    try:
        for period, hours in json_data.items():
            is_special = (period == "special")
            for hour in hours:
                opening_hour = OpeningHours(
                    day=hour["day"],
                    start=hour["start"],
                    end=hour["end"],
                    status=hour["status"],
                    is_special=is_special
                )
                db.add(opening_hour)
        db.commit()

    except Exception as e:
        db.rollback()
        print(f"Error loading opening hours: {e}")

    finally:
        # Close the session
        db.close()

    print("Opening hours have been loaded successfully.")


def create_orders(db: Session):
    try:
        # Fetch all customers and menu items ordered by id
        customers = db.query(Customer).order_by(Customer.id).all()
        menu_items = db.query(MenuItem).order_by(MenuItem.id).all()

        # Check if there are enough customers
        if len(customers) < 10 or len(menu_items) < 2:
            print("Not enough customers or menu items available. Ensure you have at least 10 customers and 2 menu items.")
            return

        # Select the 1st, 4th, 6th, 8th, and 10th customers
        selected_customers = [customers[0], customers[3], customers[5], customers[7], customers[9]]

        selected_menu_items = menu_items[:2]

        now = datetime.utcnow()
        orders_info = [
            {"status": OrderStatus.DELIVERED, "time_offset": timedelta(hours=-5), "customer": selected_customers[0], "items": selected_menu_items},
            {"status": OrderStatus.DELIVERED, "time_offset": timedelta(hours=-4), "customer": selected_customers[1], "items": selected_menu_items},
            {"status": OrderStatus.DISPATCHED, "time_offset": timedelta(hours=-3), "customer": selected_customers[2], "items": selected_menu_items},
            {"status": OrderStatus.IN_PROGRESS, "time_offset": timedelta(hours=-2), "customer": selected_customers[3], "items": selected_menu_items},
            {"status": OrderStatus.PENDING, "time_offset": timedelta(hours=-1), "customer": selected_customers[4], "items": selected_menu_items},
        ]



        for idx, order_info in enumerate(orders_info):
            order_date = now + order_info["time_offset"]

            # Create a new order
            order = Order(
                customer_id=order_info["customer"].id,
                order_date=order_date,
                total_amount=0.0,  # will be updated after adding order items
                status=order_info["status"].value
            )
            # Set the first order's ID to a value which will not be confused with customer ID
            if idx == 0:
                order.id = 8800

            db.add(order)
            db.commit()  # Commit to generate order ID

            # Add 2 items to each order
            total_amount = 0.0
            for menu_item in order_info["items"]:
                quantity = 1  # Fixed quantity to keep it deterministic
                order_item = OrderItem(
                    order_id=order.id,
                    menu_item_id=menu_item.id,
                    quantity=quantity,
                    note=f"Fixed note for {menu_item.name}"
                )
                db.add(order_item)
                total_amount += menu_item.price * quantity

            # Update the total amount for the order
            order.total_amount = total_amount
            db.commit()

        print("Orders have been created successfully.")

    except Exception as e:
        db.rollback()
        print(f"Error loading orders: {e}")

    finally:
        db.close()
