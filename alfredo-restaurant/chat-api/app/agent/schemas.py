from typing import Optional

from pydantic import BaseModel


class MessageSchema(BaseModel):
    """Messages """
    role: str
    content: str


class ChatResponseSchema(BaseModel):
    output: str


class ChatRequestSchema(BaseModel):
    user_request: str
    chat_history: Optional[list[MessageSchema]] = []
    user_id: Optional[int] = None
