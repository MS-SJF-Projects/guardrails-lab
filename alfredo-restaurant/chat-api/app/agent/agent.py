from typing import List

from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.pydantic_v1 import ValidationError
from langchain_core.tools import ToolException


from .templates import load_chat_template
from .tools.customer import customer_retrieval_tool
from .tools.hours import opening_hours_tool
from .tools.order import cancel_order_tool, retrieve_order_tool, retrieve_user_orders_tool
from .tools.menu import daily_menu_tool
from .llm import create_llm
from .schemas import MessageSchema


def run_agent(user_request: str, chat_history: List[MessageSchema]=[]):
    """Simple method to run the make a call to the agent.

       This function prepares a chat template, formats the input prompt, and executes
       an agent to retrieve responses

           Parameters:
               question (str): The main question to retrieve responses for.

           Returns:
               A dictionary of the form:
               {
                'user_request': <user_request>,
                'chat_history': [{'role': 'user', 'content': 'what is it you want?'}],
                'output': 'response-from-the-agent-as-a-result'
                }
    """
    # Create an instance of the LLM (Azure OpenAI instance), load the chat template & create the Agent.
    llm = create_llm()

    # Load a Langchain ChatPromptTemplate instance using the templates in the 'prompts' subdirectory.
    # The resulting ChatPromptTemplate has two possible input variables: 'input' and 'chat_history'.
    chat_template = load_chat_template()

    # Load the Tools. See the 'tools' subdirectory for each tool definition.
    tools = [daily_menu_tool, customer_retrieval_tool, opening_hours_tool, retrieve_user_orders_tool, cancel_order_tool]

    # Create the Langchain Agent which requires the LLM, Tools and PromptTemplate
    agent = create_openai_tools_agent(llm, tools, chat_template)

    # Create the runtime in charge of executing the agent.  ie. it is in charge of calling the LLM,
    # running the tools when the LLM says to use a particular tool, adding the tool output (returned data)
    # into the message history, and calling the llm again, etc.
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # Convert the chat_history to the Langchain format
    # (i.e. list of tuples as required by from langchain_core.messages.utils._convert_to_message)
    # https://github.com/langchain-ai/langchain/blob/master/libs/core/langchain_core/messages/utils.py
    chat_history_langchain_format = [(msg.role, msg.content) for msg in chat_history]

    # Invoke the agent
    # https://api.python.langchain.com/en/latest/agents/langchain.agents.agent.AgentExecutor.html
    try:
        response = agent_executor.invoke({"user_request": user_request, "chat_history":  chat_history_langchain_format})
    except Exception as e:
        response = {
            'user_request': user_request,
            'chat_history': chat_history,
            'output': f"Apologies, an error occurred: {str(e)}"
        }
    return response

