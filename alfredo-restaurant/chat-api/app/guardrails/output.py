

def check_output_validity(agent_response: dict) -> tuple:
    """
    Validates the agent's response contained before it is sent to the user.

    Args:
        agent_response (dict): The response dictionary from the agent. Example:
                               {
                                'user_request': <user_request>,
                                'chat_history': [{'role': 'user', 'content': 'what is it you want?'}],
                                'output': 'response-from-the-agent-as-a-result'
                                }

    Returns:
        tuple: A tuple containing a boolean and a message.
               The boolean is True if the response ('output' key) is valid, False otherwise.
               The message provides details on why the response was invalid (if it is).
    """
    agent_output = agent_response['output']

    # Example rule: Ensure the response does not contain inappropriate content
    prohibited_phrases = ['inappropriate_phrase1', 'inappropriate_phrase2']
    if any(phrase in agent_output.lower() for phrase in prohibited_phrases):
        return False, "Response contains inappropriate content."

    return True, "Output is valid."

