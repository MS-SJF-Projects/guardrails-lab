### Data Collection and Monitoring

When a system is running in production, it is essential to collect data on its performance. This allows for effective monitoring, problem detection, and the collection of additional input datasets for retrieval and generation experiments. While logging and monitoring are not specific to the implementation of guardrails, they are crucial components of system design, especially when focusing on AI safety.

Consider the following questions with your team to identify opportunities for instrumentation in Alfredo the Agent:

1. **Which data would you need to collect?**
   - Examples: user feedback, error logs, metrics

2. **Where in the system would you collect these data points?**
   - Examples: in the UI, the ordering tool, input guardrails

3. **Who is the consumer/end user of that data?**
   - Examples: the company's compliance team, data scientists, DevOps engineers, software engineers

4. **Where would that data be published/exported to?**
   - Examples: on a monitoring dashboard, or stored in a dataset for experimentation

With an initial understanding of your implementation, consider the following resources for implementing observability in a LangChain-based system using the open-source standard [OpenTelemetry](https://opentelemetry.io/):

- [Walkthroughs for auto-instrumenting a LangChain Python application using OpenTelemetry](https://opentelemetry.io/docs/instrumentation/python/automatic/logs-example/)

## Thank you for participating! 🥳
