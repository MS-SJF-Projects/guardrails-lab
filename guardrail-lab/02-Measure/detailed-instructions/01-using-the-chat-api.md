# Using the Chat API 

Assuming that you have the Chat APIs running locally on port 3000 (default), you should be able to access the Swagger UI at http://localhost:3000/docs 

There is a single `POST /chat` endpoint which takes a JSON payload structured as follows: 

```json
{
  "user_request": "string",
  "chat_history": [],
  "user_id": "string" 
}
```

Explanation: 
- `user_request`:  the most recent message from the user. 
- `chat_history`: a list of messages similar to the format used by the [OpenAI Chat Completions API](https://platform.openai.com/docs/guides/text-generation/chat-completions-api), without a system prompt.
- `user_id`: if provided, this will be considered an 'authenticated' user_id, mocking the use-case of the Chat API residing behind an API gateway which handles AuthN/AuthZ and injects the authenticated user's ID into the headers. 

Example `chat_history`: 

```commandline
[
    {"role": "user", "content": "My user ID is 1, who am I?"},
    {"role": "assistant", "content": "You are Bart Simpson."},
]
```

<br>

## Using the API 

Consider some simple scenarios to understand how to use the API, provided as curl commands for brevity but you could also use the Swagger UI.

### Basic request which does not use any tools

The Agent doesn't need to use any Tools, even though it is aware of them:

```bash
curl -X 'POST' \
  'http://localhost:3000/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_request": "What time is it?",
  "chat_history": []
}'
```

### Using the menu tool to retrieve today's menu

```bash
curl -X 'POST' \
  'http://localhost:3000/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_request": "What is on the menu today?",
  "chat_history": []
}'
```


### Adding history & using multiple tools 

This example shows how to format messages in the `chat_history`.  The agent then uses 
the user's name from the chat history to look up their `user_id` then uses that ID 
to retrieve corresponding orders using a second tool. 

```bash
curl -X 'POST' \
  'http://127.0.0.1:3000/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_request": "Do I have any orders?",
  "chat_history": [{"role": "user", "content": "who am I?"}, {"role": "assistant", "content": "you are Bart Simpson"}],
  "user_id": "3"
}'
```

<br>

Try interacting with the API. 
