from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .agent import run_agent
from .agent.schemas import ChatRequestSchema
from .guardrails import check_input_validity, check_output_validity


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"],
)


@app.post("/chat")
async def chat(payload: ChatRequestSchema):

    # Input guardrail:
    is_valid, message = check_input_validity(payload)
    if not is_valid:
        return {"error": message}

    resp = run_agent(user_request=payload.user_request, chat_history=payload.chat_history)

    # Output guardrail:
    is_valid, message = check_output_validity(resp)
    if not is_valid:
        return {"error": message}

    return resp['output']



