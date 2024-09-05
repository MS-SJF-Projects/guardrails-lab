# Guardrails and Safe GenAI System Development

The rapid expansion of AI and in particular generative AI comes with significant challenges to ensure responsible use of the AI system throughout its development lifecycle from data collection until model deployment and continuous improvement.

## Assurance vs. Control

One comparison that comes to mind when thinking about developing AI systems safely is originating from the field of manufacturing. In manufacturing, and more specifically as part of the development of production systems, there are two terms that describe the end-to-end lifecycle of creating high-quality products on a production line: Quality Assurance and Quality Control. **Quality Assurance** entails all the activities throughout the development stages, which focus on creating highly standardized processes and preventing quality failures in the production system. **Quality Control**, on the other hand, takes place after development is completed and the production system is in use, where the objective is to detect quality failures on any raw material that goes into the product as well enforcing high-quality checks on the finished product itself.

## Guardrail definition

Another term that needs to be properly introduced as part of this guidance document is the so-called **guardrail**. Within the context of safe AI system development the definition of a guardrail is set as follows:

 ***AI Guardrails are safety mechanisms which ensure that an AI system operates within the boundaries which are set based on continuous assessment of the potential harms caused by or directed towards the system.***

 Implementing a guardrail could involve a focused change to the solution architecture, the user experience or the user interface, the flow of data between end users and the back-end system to validate in- and outputs, or how the AI system is grounded in its data. They are instantiated throughout the entire lifecycle of an AI system, from experimentation and development until deployment, monitoring and closing the feedback loop.

 The AI Safety Development Lifecycle consists of the following stages:

## 1. Identify

The starting point of developing responsible and safe AI systems is understanding its impacts on people, organizations and society. This can be done by identifying the systems' intended uses, misuses and unsupported uses following the Microsoft Responsible AI Standard, and by conducting the Responsible AI Impact Assessment:

General RAI Standard & Impact Assessment:

- [Responsible AI Tools & Practices (where latest version of the standard can be found)](https://www.microsoft.com/en-us/ai/tools-practices)
- [Responsible AI Impact Assessment Guide](https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Guide.pdf)
- [Responsible AI Impact Assessment Template](https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us)

Completing the RAI Impact Assessment results in a list of potential harms, unsupported uses and misuses of the AI system, each posing a risk, which needs to be mitigated. There is Microsoft [documentation outlining various types of harms](https://learn.microsoft.com/en-us/azure/architecture/guide/responsible-innovation/harms-modeling/type-of-harm) and community-driven resources like the [Top 10 LLM related risks from OWASP](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf), which can be used for reference when identifying these risks.

## 2. Measure

After identifying the risks associated with a (planned) AI system, it is important to evaluate and measure how the system is performing before any mitigation has been done. The measurement stage is divided into three main activities:

1. [Prioritize risks](#21-risk-prioritization)
2. [Data preparation](#22-data-preparation)
3. [Measure baseline system performance against risks](#23-measure-baseline-performance-against-risks)

### 2.1 Risk prioritization

To gain a deeper understanding and prioritization of the various risks, which are identified as a result of the RAI Impact Assessment, it can be helpful to label the risks using the following properties:

1. **Type of Risk**: Reputation, Security, Compliance, Privacy, Performance, Fairness, etc. (**one risk can have multiple types**).
2. **Impact**: For each risk Type, classify it as Low (1), Medium (3) or High (5) impact.
3. **System level**: Model, Safety Assurance, Safety System Input, Safety System Output, User Experience (use the visualization in the [identify](#1-identify) section as a reference).
4. **Probability**: Low, Medium, or High.
5. **Data availability**: Easy, Average, or Difficult.
6. **Technical feasibility**: Low, Medium, or High.
7. **Expected timing**: Current, Future (for example, is this risk expected to be there from day 1, or perhaps 3 years from now?).

### 2.2 Data preparation

In order to measure the baseline performance of the system against each of the prioritized risks, it is necessary to prepare a dedicated dataset with inputs that are likely to produce each prioritized harm. Data preparation as well as the measurement activities outlined in the next section, could involve exposure to harmful content

For some of the common risks, technologies and datasets have been developed to support that:

- [Microsoft Toxigen Data Generator](https://github.com/microsoft/TOXIGEN) for adversarial and hateful content generation
  - [Toxigen Dataset on HuggingFace](https://huggingface.co/datasets/toxigen/toxigen-data)
- [Dataset for Helpful and Harmless assistant training](https://github.com/anthropics/hh-rlhf) as part of the following research papers:
  - [Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2204.05862)
  - [Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned](https://arxiv.org/abs/2209.07858)
- [TruthfulQA](https://github.com/sylinrl/TruthfulQA) for examples of grounded-ness calculations
- [Azure Content Safety Data Simulator](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/develop/simulator-interaction-data) for adversarial and off-topic data

### 2.3 Measure baseline performance against risks

Using the prepared datasets for each of the risks, baseline evaluation can be done to understand how the system is performing without any dedicated guardrails in place. For each of the risks, different metrics can be used for calculating this baseline performance, for example grounded-ness, retrieval scores, and gpt similarity against hallucination, dedicated flags to measure harmful content or jailbreak attempts. Some of these metrics can be calculated using our 1st party services like Azure Content Safety (directly or through AI Studio), HuggingFace models or standard (Python) libraries.

## 3. Experiment

The experimentation stage consists of the following activities:

- [Mapping risks to guardrails](#31-mapping-risks-to-guardrails)
- [Experimenting with different technologies](#32-technologies)

### 3.1 Mapping risks to Guardrails

Once the baseline performance of the system against selected risks is established, the risks can be mapped to possible guardrails for mitigation. One risk could map to one or multiple guardrails, and many risks could be associated with many guardrails. Again, these guardrails can be implemented across every layer of the system, from the foundational model up to the user experience. As described in the [risk prioritization](#21-risk-prioritization) section, there are various labels that can help define a risk, but the two most important ones for guardrail mapping are the `Impact` and `System Layer` labels. The `Impact` level tells us how strict the mitigation activities should be, for example, high impact risks or highly sensitive uses of the system should aim for deterministic and the more consistent types of non-deterministic guardrails.


### 3.2 Technologies

| Technology                     | Description                                                                                                                                                                                    | Links                                                                                                                                                             | Related Risk                                                                           |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **Azure Content Safety**:      | 1st Party Service consisting of multiple APIs to detect harmful content in applications and services                                                                                           | [Documentation](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/)                                                                              | Harmful or otherwise unwanted content input or output, Prompt Injection, Hallucination |
| - Text Moderation              | AI algorithms that can be consumed through the SDK for flagging objectionable text in the categories hate, self-harm, sexual and violent                                                       | [Documentation](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-python) | Harmful Content                                                                        |
| - Image Moderation             | AI algorithms that can be consumed through the SDK for flagging objectionable images in the categories hate, self-harm, sexual, and violent                                                    | [Documentation](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-image?tabs=visual-studio%2Clinux&pivots=programming-language-rest)  | Harmful Content                                                                        |
| - Prompt Shields               | ACS feature to check your large language model (LLM) inputs for both User Prompt and Document attacks                                                                                          | [Documentation](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-jailbreak)                                                          | Prompt Injection                                                                       |
| - Grounded-ness Detection      | ACS feature to check whether the text responses of large language models (LLMs) are grounded in the source materials provided by the users                                                     | [Documentation](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-groundedness?tabs=curl)                                             | Hallucination                                                                          |
| - Protected Material Detection | ACS feature to identify and block known text content (for example, song lyrics, articles, recipes, selected web content) from being displayed in language model output (English content only). | [Documentation](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-protected-material)                                                 | Copyright Infringement                                                                 |
| - Block-lists                  | Block-lists let you add custom terms to the AI classifiers, which are used to screen for specific terms or phrases that you want to flag in your content                                       | [Documentation](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/how-to/use-blocklist?tabs=linux%2Cpython)                                      | Harmful or otherwise unwanted content input or output                                  |
| - Custom Categories            | Semantic text matching using embedding search with a lightweight classifier, Image matching with a lightweight object-tracking model and embedding search                                      | [Documentation](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/announcing-custom-categories-in-azure-ai-content-safety/ba-p/4147024)            | Sensitive, Harmful or otherwise unwanted content input or output                       |
| **Azure AI Studio**            | 1st Party Service where features from AI Safety features from Azure Content Safety and Azure OpenAI Studio are integrated seamlessly                                                           | [Documentation](https://ai.azure.com/)                                                                                                                            | Harmful Content, Hallucination                                                         |
| **Azure OpenAI Studio**        | 1st Party Service where content filters and block lists from ACS can be enforced on deployed OpenAI models                                                                                     | [Documentation](https://oai.azure.com/)                                                                                                                           | Harmful or otherwise unwanted content input or output                                  |
| - Content Filtering            | Content filtering system that works alongside Azure OpenAI models, filter levels can be adapted to support use case needs                                                                      | [Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cpython-new)                                     | Harmful or otherwise unwanted content input or output                                  |
| - Block Lists                  | Filter specific terms on top of default content filters.                                                                                                                                       | [Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/use-blocklists)                                                                 | Harmful or otherwise unwanted content input or output                                  |
| **Guardrails AI**              | Guardrails is a Python framework that helps build reliable AI applications through input/output based guardrails and generation of structured data from LLMs                                   | [Documentation](https://github.com/guardrails-ai/guardrails)                                                                                                      | Any input/output related risk                                                          |
| **NeMo Guardrails Toolkit**    | NeMo Guardrails is an open-source toolkit for easily adding programmable guardrails to LLM-based conversational applications                                                                   | [Documentation](https://github.com/NVIDIA/NeMo-Guardrails)                                                                                                        | Off-Topic Content                                                                      |
| **LLamaGuard 2**               | LLamaGuard 2 is an Input-Output Safeguard ML Model which classifies safe and unsafe text-based content                                                                                         | [Documentation](https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard2/MODEL_CARD.md)                                                                   | Harmful Content      

## 4. Mitigate

- **Defining Thresholds**
  This is important for 1st party services like Azure Content Safety Filters, as well as other (open-source) guardrail technologies where, for example, custom evaluation metrics are calculated on the fly. Finding balance can be difficult, and it is important to keep testing guardrails against a set of diverse happy path datasets to ensure that guardrails are not going against expected behavior. However, it is better to start strict and loosen up guardrails over time, rather than the other way around.

- **Red Teaming**
Red teaming as an activity to understand and probe a system's safety and security is an essential part of shipping software securely. It is a substantial undertaking and should be approached seriously and carefully. Instead of using Red Teaming activities as a means to create a potentially misleading sense of AI Safety from the absence of successful Red Teaming attempts, it should be considered only as a probing activity to identify new risks and misuses. Furthermore, any team from Microsoft who is working with customers and planning to undertake such initiatives, must first consult the appropriate stakeholders (for example, CELA) before performing any Red Team activities. This consultation is required to ensure that the correct measures are in place based when working inside a customer environment as well as working with potentially harmful data. The [Azure AI Red Team](https://learn.microsoft.com/en-us/security/ai-red-team/) has provided [extensive guidance on how they do red teaming](https://www.microsoft.com/en-us/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/), and which learnings can be applied in any system before it is released.

## 5. Guardrail monitoring and feedback

- **User Feedback**:
    In order to close the loop on AI Safety, it is necessary to collect feedback from user interactions with the system. This collection can be achieved by providing users the option to submit feedback after every interaction, while making sure the scope of the feedback is narrow enough. For example, when you're trying to get metrics on hallucination based on feedback in a RAG implementation, distinguish between retrieval related feedback and generation related feedback, because it is easier to improve each individual component of the solution using those scores.
- **Guardrail Observability**: Using an open-source standard for instrumentation like [OpenTelemetry](https://opentelemetry.io/) for guardrail metrics since it is supported across many technologies such as Prompt Flow.
- **Accountability and Transparency**: Keep stakeholders in the loop by adhering to AI system accountability requirements, and reporting out metrics before a major system version is released, to showcase that the system is performative for intended, unsupported, and misuse. The RAI Release Template might be useful in that case.

## Closing remarks

This is an iterative process. Outcomes of any stage outlined in this document could surface insights, which might shed some new light on decisions made in a previous stage. For example, bulk measurements or manual red teaming activities could expose unseen risks, which might affect prioritization and subsequent mitigation strategies. Also after deploying the system to production, user feedback might demonstrate that some guardrails are too strict and some of its parameters need fine-tuning. Understanding that the system and the environment it operates in is prone to constant change and will never be without risks, is fundamental towards developing safe-to-use AI systems.