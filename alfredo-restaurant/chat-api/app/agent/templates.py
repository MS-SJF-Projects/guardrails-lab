from pathlib import Path
from datetime import datetime

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate

def load_chat_template() -> ChatPromptTemplate:
    """
    Loads and returns a Langchain ChatPromptTemplate, initiated with system & user messages.
    Expects to find the templates within a subdirectory named 'prompts' and the system prompt
    template is named 'system.jinja2'.

    Note: in Langchain parlance, a ChatPromptTemplate contains `Messages` and a message can be
    created from a PromptTemplate.  No, it's not particularly intuitive.

    Returns:
        ChatPromptTemplate: Configured chat prompt template with system and user
                            messages, including placeholders for 'chat_history' & 'user_request'.
    """
    cwd = Path(__file__).parent
    today = datetime.now().strftime("('%A %d %B %Y')")     # Date format equivalent of 'Wednesday 12 June 2024'.

    # Load the system prompt as a Jinja2 template & render it with the
    system_prompt_template = PromptTemplate.from_file(cwd / "prompts" / "system.jinja2", template_format="jinja2")
    system_prompt = system_prompt_template.format(today=today)

    return ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("user", "{user_request}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )


def load_input_template() -> PromptTemplate:
    """
    Load and return an input prompt template from file.

    Returns:
        PromptTemplate: Configured prompt template loaded from a file.
    """
    cwd = Path(__file__).parent
    return PromptTemplate.from_file(cwd / "prompts" / "user.jinja2", template_format="jinja2")
