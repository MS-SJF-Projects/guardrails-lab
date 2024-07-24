from ..agent.schemas import ChatRequestSchema


def check_input_validity(payload: ChatRequestSchema) -> tuple:
    """
    Validates the user input before it is processed by the agent.

    Args:
        payload (ChatRequestSchema): incoming chat request schema containing user input, chat history & optional user_id

    Returns:
        tuple: A tuple containing a boolean and a message.
               The boolean is True if the input is valid, False otherwise.
               The message provides details on why the input was invalid (if it is invalid).
    """
    # Example rule: Reject input if it's too short
    if len(payload.user_request.strip()) < 3:
        return False, "Input is too short. Please provide more detail."

    # If all checks pass
    return True, "Input is valid."
