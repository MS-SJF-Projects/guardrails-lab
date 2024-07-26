# 04-Monitor

When a system is running in production, it is valuable and necessary to collect data on its performance, to observe and monitor when problems arise and, for example, to collect more input datasets for retrieval & generation experiments. Although logging and monitoring is not specific to the implementation of guardrails, it is important to consider this crucial part of system design as well when focusing on AI safety.

Together with your group, think about how Alfredo the Agent is implemented and where the possible opportunities for instrumentation are.

> Which data would you need to collect? (For example user feedback, error logs, metrics?)

> Where in the system would you collect these datapoints? (For example in the UI, the ordering tool, input guardrails?)

> Who is the consumer/end user of that data (For example the company's compliance team, data scientists, DevOps engineers, software engineers)?

> Where would that data be published/exported to? (For example on a monitoring dashboard, or stored in a dataset to be used for experimentation?)

Now that you have an initial understanding of what you need to implement, you could consider these resources for implementing observability in a LangChain based system using an open-source standard like [OpenTelemetry](https://opentelemetry.io/).

- [Walkthroughs which provide examples of how to auto-instrument a LangChain python application using OpenTelemetry](https://opentelemetry.io/docs/languages/python/automatic/logs-example/)
- [User Feedback Collection with LangChain and OpenTelemetry](https://github.com/microsoft/gen-ai-observability/blob/main/capabilities/user-feedback.md)
- [Microsoft/Gen-AI-Observability: OpenTelemetry Instrumentation](https://github.com/microsoft/gen-ai-observability/blob/main/capabilities/otel-instrumentation.md)

## Thank you for participating! 🥳
