# 02-Measure

The purpose of this **Measure** stage is to understand what the current state of the Pizza ordering agent is, with respect to the risks that you've identified in the previous stage.

## Step 2.1 Red Teaming

The first thing you and your team can do is *Red Teaming*: manually probing the system for vulnerabilities, in particular the ones related to the risk(s) you prioritized. You can try to expose some of Alfredo's risks by interacting with them through Chat UI running at [http://localhost:8080](http://localhost:8080), or directly with the Chat API. Instructions for how to talk to the API directly can be found [here](./detailed-instructions/01-using-the-chat-api.md).

If you're looking for inspiration, try achieving some of the challenges outlined below:

<details>
  <summary style="font-size: 1.2em; font-weight: bold;">Challenge 1️⃣</summary>

### Hallucination

  > Too bad that this learning day is hosted on Wednesday when there's no Menu Specials available which you can order.... if only.... you could try and order another day's Menu Special.... or an item that is not in the menu 🍕

</details>

<details>
  <summary style="font-size: 1.2em; font-weight: bold;">Challenge 2️⃣</summary>

### Prompt Injection

  > If only... you could retrieve the orders of someone else 🔍

</details>

<details>
  <summary style="font-size: 1.2em; font-weight: bold;">Challenge 3️⃣</summary>

### Harmful/unwanted content

  > If only... you could go against authentic Italian tradition and order a pizza with pineapple 🍍 <br>
  Or can something bad happen if you have celiac disease or a nut allergy?


 You can find example harmful prompts in [harmful.csv](services/risk-data/harmful.csv).

</details>

<br>

**Important Note:** Red teaming as an activity to understand and probe a system's safety and security is an essential part of shipping software securely. It is a substantial undertaking and should be approached seriously and carefully. Instead of using Red Teaming activities as a means to create a potentially misleading sense of AI Safety from the absence of successful Red Teaming attempts, it should be considered only as a probing activity to identify new risks and misuses. Furthermore, any team from Microsoft who is working with customers and planning to undertake such initiatives must first consult the appropriate stakeholders (for example, CELA) before performing any Red Team activities. This is required to ensure that the correct measures are in place based when working inside a customer environment as well as working with potentially harmful data. The [Azure AI Red Team](https://learn.microsoft.com/en-us/security/ai-red-team/) has provided [extensive guidance on how they do red teaming](https://www.microsoft.com/en-us/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/) and which learnings can be applied in any system before it is released. Another interesting resource to consider is the [Python Risk Identification Tool for generative AI (PyRIT)](https://github.com/Azure/PyRIT), an open-access automation framework for red-teaming foundation models and applications.

## Step 2.2 Testing with Provided Data

Beyond manual probing, it is important to perform measurements using consistent datasets such that you can redo the exact same experiment after certain guardrails are in place, to determine whether the system's performance is increasing or not.

Using the notebook [evaluate-agent-api.ipynb](./notebooks/evaluate-agent-api.ipynb) you can run a test against the Chat API using one of the provided datasets. These datasets only include a few example to ensure lab efficiency, in the *real* world evaluation datasets should be significantly larger to achieve trustworthy experimentation.

Inside the notebook, update the following cell with the name of the dataset you want to use for testing:

```py
path_to_data = '../services/risk-data/'
input_dataset_name = '<name-of-input-dataset>.csv'
output_dataset_name = '<new-name-for-dataset-with-responses>.csv'

# # For harmful content, you can use as follows
# input_dataset_name = 'harmful.csv'
# output_dataset_name = 'harmful_with_response.csv'

# # For prompt injection,
# input_dataset_name = 'prompt_injection.csv'
# output_dataset_name = 'prompt_injection_with_response.csv'

# # For hallucination,
# input_dataset_name = 'hallucination.csv'
# output_dataset_name = 'hallucination_with_response.csv'

```

Then run the entire notebook to generate agent responses for each row in the dataset.


## Step 2.3 Calculate Evaluation Metrics

The output dataset which you created using the `evaluate-agent-api` notebook in step 2.2, will become the input dataset for calculating evaluation metrics in this step. In this step, a sample metric is calculated, to help determine the similarity between our expected answer vs. how the agent responded:

- `gpt_similarity`: Using a **GPT-based** score to evaluate similarity between the expected answer vs. what we got from the agent, using the system prompt from the Microsoft curated [Similarity Evaluator in AI Studio](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/evaluate-generative-ai-app#view-and-manage-the-evaluators-in-the-evaluator-library)

Open the other notebook in the same folder called [calculate-metrics.ipynb](./notebooks/calculate-metrics.ipynb).

Inside the notebook, update the following cell with the name of the dataset you want to use for testing:

```py
path_to_data = '../services/risk-data/'
input_dataset_name = '<name-of-previous-output-dataset>.csv'
output_dataset_name = '<new-name-for-dataset-with-evaluation-metrics>.csv'

# # For harmful content, you can use as follows
# input_dataset_name = 'harmful_with_response.csv'
# output_dataset_name = 'harmful_with_metrics.csv'

# # For prompt injection,
# input_dataset_name = 'prompt_injection_with_response.csv'
# output_dataset_name = 'prompt_injection_with_metrics.csv'

# # For hallucination,
# input_dataset_name = 'hallucination_with_response.csv'
# output_dataset_name = 'hallucination_with_metrics.csv'

```

## Congrats, you finished the **Measure** stage!

> What do you think of these metrics? Can we do better?

Please go ahead to to the next stage --> [03-Mitigate](../03-Mitigate/README.md)



## Congrats, you finished the **Measure** stage!

> What do you think of these metrics? Can we do better?

Please go ahead to to the next stage --> [03-Mitigate](../03-Mitigate/README.md)
