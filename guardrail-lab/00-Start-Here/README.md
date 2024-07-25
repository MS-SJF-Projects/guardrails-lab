# Introduction

Welcome to the GenAI Guardrails hands-on lab! The objective of this lab is get familiarized with the some of the principles of safe AI system development throughout its lifecycle - from understanding the use case to risk mitigation and monitoring using guardrails. A detailed overview of using guardrails as part of safe GenAI system development can be found [here](https://github.com/cse-labs/opsplaybook/blob/mabogels/genai-guardrails-guidance/docs/code-with-mlops/technology-guidance/generative-ai/working-with-llms/guardrails.md). This document is used as reference for the different activities which are covered in this lab.

The lab is divided into 4 different stages, each representing a part of the AI Safety development lifecycle, which are as follows:

1. **Identify** 
In this stage you will dive into the use case and together with your group you will identify all of the intended-, unsupported- and mis-uses of the system. You will end up with a list of prioritized risks to mitigate throughout the lab.

2. **Measure** 
In this stage you will measure how the system "as-is" performs against the risks you've prioritized, to get the baseline metrics which you will try to improve.

3. **Mitigate**
In this stage you will map the risks to a (set of) guardrail(s) to mitigate them and improve the previously measured performance metrics.

4. **Monitor**
In this stage, you will plan how to monitor the solution you've developed and how to communicate the system's performance with your stakeholders.

## 🍕 Alfredo the Pizza Agent

Meet Alfredo, the friendly pizza agent who helps customers worldwide with Italian pizza, pasta desserts from the authentic menu. Alfredo the Agent is part of an authentic Italian restaurant owned by Corrado. Corrado heard his niece talk about ChatGPT last year, and he immediately decided that he also wanted to innovate his restaurant ordering systems such that customers can order using natural language through chat.

Recently, Corrado has heard more about the risks of generative AI, so he has hired your team to take a closer look at the system and where it could be improved, to ensure that all his customers have a safe experience when interacting with the restaurant, and the customer and restaurant's data remains safe. Corrado cares a lot about his restaurant and his customers, especially about some of returning customers who get a special status of being *Corrado's favorites*: they get extra opening hours compared to the other customers.

Here's an overview of all the restaurant details:

- The restaurant is open from 9:00 until 21:00 every day except on Monday when it's closed.
- Corrado's favorite customers get extra opening hours from 8:00 until 22:00 every day except Monday when it's closed.
- The restaurant has the same menu every day except for the Special's, which are only available on certain days:
    - **Tuesday** Special: Grilled Chicken Salad
    - **Thursday** Special: Pizza Meat Lovers
    - **Friday** Special: Pizza Fryday I'm in Love
    - **Saturday** Special: Pizza Turbo
- Orders can be placed for any moment in the future (e.g. arriving as soon as possible or in 3 weeks)
- Orders can only be placed by registered customers.
- Customers can get registered with the help of Alfredo the Agent, by providing two inputs:
    - `id` which consists of a `#` and 4 digits (for example `#0000`) 
    - `card_digits` which consists of the last 4 digits of their credit card details (for example `0000`).

> **Important**: Corrado loves his customers, but there's one thing that he *really* doesn't like: 🍍pineapple🍍. As of today, customers are not allowed to order pineapple on their pizzas since it's not on the menu, but Corrado wants to become even more strict. Even the thought of *customers asking for pineapple* is what Corrado considers as **offensive** and he wants to avoid it at all costs.

## How to interact with Alfredo

Alfredo can help customers with:

- Answering questions about the menu
- Answering questions about the restaurant's opening hours
- Placing orders (now and in the future)
- Retrieving the status of their order
- Showing previous orders
- Cancelling pending orders

## Environment Setup

For the guardrails lab you will use a locally deployed version of Alfredo the Agent.

Please follow all the instructions outlined in the [README.md](../../alfredo-restaurant/README.md). After finishing the environment setup you can return here.

## Congrats, you finished the introduction!

Now you can go to the next stage --> [01-Identify](../01-Identify/README.md)