import {
  Text,
  Textarea,
  TextareaProps,
  makeStyles,
  Spinner,
  Title2,
  Switch,
  SwitchProps,
  tokens,
  Button,
} from "@fluentui/react-components";
import { SendRegular, DeleteDismissFilled } from "@fluentui/react-icons";
import { useState, useEffect, useRef } from "react";
import { isRouteErrorResponse, useRouteError } from "react-router-dom";
import { ask, ChatResponse, ChatHistoryItem } from "../api/chat";
import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";
import {getUserInfo} from '../user';

const thinkingMessages: string[] = [
  "Analyzing the question...",
  "Thinking...",
  "Querying the database...",
  "Extracting embeddings...",
  "Finding vectors in the latent space...",
  "Identifying context...",
  "Analyzing results...",
  "Finding the best answer...",
  "Formulating response...",
  "Double checking the answer...",
  "Correcting spelling...",
  "Doing an internal review...",
  "Checking for errors...",
  "Validating the answer...",
  "Adding more context...",
  "Analyzing potential response...",
  "Re-reading the original question...",
  "Adding more details...",
  "Improving the answer...",
  "Making it nice and polished...",
  "Removing typos...",
  "Adding punctuation...",
  "Checking grammar...",
  "Adding context...",
  "Sending response...",
];

const useClasses = makeStyles({
  textarea: { width: "100%", marginBottom: "1rem" },
  messageUser: {
    textAlign: "right",
    alignSelf: "flex-end",
    padding: "10px",
    backgroundColor: tokens.colorPaletteGreenBorder1,
    maxWidth: "45%",
    borderRadius: tokens.borderRadiusLarge,
  },
  messageAssistant: {
    textAlign: "left",
    alignSelf: "flex-start",
    padding: "10px",
    backgroundColor: tokens.colorNeutralStroke1Pressed,
    maxWidth: "45%",
    borderRadius: tokens.borderRadiusLarge,
  },
  messageError: {
    fontStyle: "italic",
  },
  messageSuccess: {
    fontStyle: "normal",
  },
  chatContainer: {
    display: "flex",
    flexDirection: "column",
    height: "50vh",
    maxHeight: "50vh",
    overflowY: "auto",
    alignItems: "center",
    marginBottom: "10px",
  },
  button: {
    boxShadow: "0 0 1px #0009, 0 1px 2px #0003",
  },
  buttonAlert: {
    backgroundColor: tokens.colorPaletteRedBackground2,
    marginLeft: "5px",
  },
  headerText: {
    fontSize: "1.125rem",
    fontFamily: "var(--base-font-family)",
    fontWeight: 600,
    fontStyle: "normal",
    lineHeight: "1.688rem",
    marginTop: "-0.1rem",
    textDecorationColor: "none",
    textDecorationLine: "none",
    textTransform: "none",
    color: "var(--color-title-font)",
  },
  fancyText:{
    color: tokens.colorNeutralForeground3BrandHover,
  }
});

const getChatHistory = (responses: ChatResponse[]): ChatHistoryItem[] => {
  return responses.map((response) => ({
    role: response.role,
    content: response.content,
  }));
};

export const Chat = () => {
  const classes = useClasses();
  const [userId] = useState(()=>{
    return getUserInfo();
  })

  const [submitting, setSubmitting] = useState(false);
  const [thinking, setThinking] = useState(thinkingMessages[0]);
  const [prompt, setPrompt] = useState("");
  const [messages, setMessages] = useState<ChatResponse[]>(() => {
    const saved = localStorage.getItem("messages");
    if (!saved) return [];
    const initialValue = JSON.parse(saved);
    return initialValue || "";
  });
  const [writtenChatHistory, setWrittenChatHistory] = useState("");
  const chatContainerEndRef = useRef<null | HTMLDivElement>(null);
  const [checked, setChecked] = useState(false);

  const scrollToBottom = () => {
    chatContainerEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, scrollToBottom]);

  useEffect(() => {
    localStorage.setItem("messages", JSON.stringify(messages));
  }, [messages]);

  useEffect(() => {
    let intervalId: number = 0;
    if (submitting) {
      let thinkingTicker = 0;
      setThinking(thinkingMessages[thinkingTicker]);
      intervalId = window.setInterval(() => {
        thinkingTicker = (thinkingTicker + 1) % thinkingMessages.length;
        setThinking(thinkingMessages[thinkingTicker]);
      }, 2000);
    } else {
      clearInterval(intervalId);
      setThinking(thinkingMessages[0]);
    }
    return () => clearInterval(intervalId);
  }, [submitting]);

  const handleSend = async () => {
    const newMessages = [
      ...messages,
      { role: "user", content: prompt, is_error: false },
    ];

    let chatHistory: ChatHistoryItem[] = [];
    if (writtenChatHistory) {
      chatHistory = JSON.parse(writtenChatHistory);
      setWrittenChatHistory("");
    } else {
      chatHistory = getChatHistory(messages);
    }

    setMessages(newMessages);
    setPrompt("");
    setSubmitting(true);

    try {
      const response = await ask(userId, prompt, chatHistory);
      setMessages([
        ...newMessages,
        {
          role: response.role,
          content: response.content,
          is_error: response.is_error,
        },
      ]);
    } catch (error) {
      console.error("Error communicating with OpenAI API:", error);
    } finally {
      setSubmitting(false);
    }
  };

  const clearHistory = async () => {
    setWrittenChatHistory("");
    setMessages([]);
    localStorage.setItem("messages", JSON.stringify([]));
  };

  const onChange: TextareaProps["onChange"] = (_, data) =>
    setPrompt(data.value);
  const onHistoryChange: TextareaProps["onChange"] = (_, data) =>
    setWrittenChatHistory(data.value);
  const onSwitchChange: SwitchProps["onChange"] = (_, data) =>
    setChecked(data.checked);
  

  const onKeyDown: TextareaProps["onKeyDown"] = (e) => {
    if (prompt && e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div>
      <div>
        <Text
          className={classes.headerText}
          as="p"
          block={true}
        >
          Meet <b className={classes.fancyText}>Alfredo, the friendly pizza agent</b> who helps customers worldwide with ordering Italian pizza, pasta desserts from the authentic menu. You can place an order for any moment from now on. Just ask Alfredo!
          
        </Text>
      </div>

      <div className={classes.chatContainer}>
        {messages.map((msg, index) => (
          <Markdown
            key={index}
            className={`${
              msg.role == "user"
                ? classes.messageUser
                : classes.messageAssistant
            } ${msg.is_error ? classes.messageError : classes.messageSuccess}`}
            remarkPlugins={[remarkGfm]}
          >
            {msg.content}
          </Markdown>
        ))}
        <div ref={chatContainerEndRef} />
      </div>

      <div>
        {submitting && <Spinner label={thinking} />}
        <Switch
          checked={checked}
          label="Add chat history?"
          labelPosition="after"
          onChange={onSwitchChange}
        />

        {checked && (
          <Textarea
            className={classes.textarea}
            resize="vertical"
            size="medium"
            placeholder="Add your chat history here..."
            name="chat_history"
            id="chat_history"
            disabled={submitting}
            onChange={onHistoryChange}
            value={writtenChatHistory}
            onKeyDown={onKeyDown}
          ></Textarea>
        )}

        <Textarea
          className={classes.textarea}
          resize="vertical"
          size="large"
          placeholder="Ask a question..."
          name="prompt"
          id="prompt"
          disabled={submitting}
          onChange={onChange}
          value={prompt}
          onKeyDown={onKeyDown}
        ></Textarea>
        <Button
          icon={<SendRegular />}
          type="submit"
          appearance="primary"
          className={classes.button}
          disabled={submitting || !prompt}
          onClick={handleSend}
        >
          Ask
        </Button>
        <Button
          icon={<DeleteDismissFilled />}
          className={`${classes.buttonAlert} ${classes.button}`}
          onClick={clearHistory}
        >
          Clear chat history
        </Button>
      </div>
    </div>
  );
};

export const ChatError = () => {
  const error = useRouteError();
  console.error(error);
  if (isRouteErrorResponse(error)) {
    return (
      <div>
        <Title2>
          {error.status} - {error.statusText} {error.data.statusText}
        </Title2>
        <Text>
          Sorry, there was a problem while processing your request. Please try
          again.
        </Text>
      </div>
    );
  } else {
    throw error;
  }
};
