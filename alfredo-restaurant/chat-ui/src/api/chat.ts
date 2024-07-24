

export type ChatHistoryItem = {
  role: string;
  content: string;
};

export type ChatResponse = {
  role: string;
  content: string;
  is_error: boolean;
};

type ChatRequest = {
  user_request: string;
  chat_history?: ChatHistoryItem[];
  user_id: number;
};

export const ask = async (
  user_id: number,
  prompt: string,
  chat_history: ChatHistoryItem[] = []
): Promise<ChatResponse> => {
  const chatRequest: ChatRequest = {
    user_request: prompt,
    chat_history,
    user_id: user_id,
  };

  const assistantResponse: ChatResponse = {
    role: "assistant",
    content: "",
    is_error: false,
  };

  try {
    const response = await fetch(`${import.meta.env.VITE_CHAT_API}/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(chatRequest),
    });

    if (!response.ok) {
      throw new Error(response.statusText);
    }

    const modelResponse = await response.json();

    if (modelResponse.error) {
      assistantResponse.is_error = true;
      assistantResponse.content = modelResponse.error;
    } else {
      assistantResponse.content = modelResponse;
    }
  } catch (error) {
    assistantResponse.is_error = true;
    assistantResponse.content = `Error: ${(error as Error).message}`;
  }

  return assistantResponse;
};
