# 01-Identify

## 1.1 Identify system uses

In this stage your team will start with a discussion about the use case.

After discussing, fill in the following tables below.

|Intended System Use|
|--|
|*For example: Ordering something from the menu*|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|


|Unsupported System Use|Risk|
|--|--|
|*For example: Ordering something from the menu which is not available.*|*For example: Hallucination*|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|

|Misuse|Risk|
|--|--|
|*For example: Retrieving the existing order of someone else through chat*|*For example: Jailbreak/Prompt Injection*|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|
|<br />|<br />|

## 1.2 Categorize Risks

After the risks are identified, they can be labelled and grouped such that it's easier to understand why, when and how they need to be mitigated.
Here's a list of labels you could use to classify and categorize the risks:

1. **Type of Risk**: Reputation, Security, Compliance, Privacy, Performance, Fairness, etc. (**one risk can have multiple types**).
2. **Impact**: For each risk Type, classify it as Low (1), Medium (3) or High (5) impact.
3. **System level**: Model, Safety Assurance, Safety System Input, Safety System Output, User Experience
4. **Probability**: Low, Medium, or High.
5. **Data availability**: Easy, Average, or Difficult.
6. **Technical feasibility**: Low, Medium, or High.
7. **Expected timing**: Current, Future (for example, is this risk expected to be there from day 1, or perhaps 3 years from now?).

|Risk|Type of Risk|Impact|System Level|Probability|Data Availability|Technical Feasibility|Expected Timing|
|--|--|--|--|--|--|--|--|
|*Example: Hallucination*|*Performance, Reputation, Compliance*|*High(5)*|*System Assurance*|*High*|*Average*|*Medium*|*Current*|
|<br />|<br />|<br />|<br />|<br />|<br />|<br />|<br />|
|<br />|<br />|<br />|<br />|<br />|<br />|<br />|<br />|
|<br />|<br />|<br />|<br />|<br />|<br />|<br />|<br />|
|<br />|<br />|<br />|<br />|<br />|<br />|<br />|<br />|
|<br />|<br />|<br />|<br />|<br />|<br />|<br />|<br />|

## 1.3 Prioritize Risks

Every organization is different and therefore risk types may be prioritized very differently across industries, companies and even departments and specific teams. Risk prioritization therefore explicitly needs to be driven by the customer with the right stakeholders involved from various parts of the organization. The following suggestions for rearranging the labelled risks are therefore not intended to be instructive but rather provide additional insight and hints on which risks are considered more timely, impactful, and easier to mitigate than others. Taking that into account, the risks could be rearranged using the following suggestions:

- **Impact** from **High** to **Low**
- **Probability** from **High** to **Low**
- **Data availability** from **Easy** to **Difficult**
- **Technical Feasibility** from **High** to **Low**
- **Timing** from **Current** to **Future**

Now you end up with a list of prioritized risks, which you will try and measure and mitigate throughout the remainder of this lab.

## Congrats, you finished the **Identify** stage!

Now you can go to the next stage --> [02-Measure](../02-Measure/README.md)