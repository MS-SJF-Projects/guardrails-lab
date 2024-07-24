# Create Azure OpenAI resource using the Azure Portal

1. Navigate to the [Azure portal](https://portal.azure.com) and login using your credentials.  

2. Click the menu icon on the top-left (1)

3. Select `Resource groups` (2)  

    <img src="images/rg-select.png" width="800">  

4. Select `Create`  

    <img src="images/rg-create.png" width="600">  

5. Enter a valid name for your resource group (e.g. *rg-agentlab*) and select a region (e.g. *Switzerland North*)  

    **Note:** The model availability changes from region to region so, while not strictly mandatory, it is always better to choose a resource group in the same region as the service you will deploy. See the [availability map](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#standard-deployment-model-availability).  

    <img src="images/rg-create-1.png"  width="600">  
   
6. Click the `review and create`button at the botton of the page and the click the `create` button once the validation passes.
7. Once the resource group is created, select it from the list of existing resource groups.
8. In the page dedicated to your new resource group, click the `create` button.  

    <img src="images/add-resource.png" width="1000">

9. In the **Marketplace** page, in the search box (1) type `azure openai` and select the first result on the list and click `create` `Azure OpenAI`(3).  

    <img src="images/add-azure-openai.png" width="800">  

10. In the **Create Azure OpenAI** as resource group select the one you have just created (1), select the same region you have chosen for the resource group (2), give a name to the resource (3) (e.g. *agentlab-llm*)and select `Standard S0` as pricing tier (4).   
    Once done, click the `Next` button at the bottom of the page.  

    <img src="images/add-openai-info.png" width="600">  

11. Click next until you reach the `Review + submit` step, then click the `Create` button at the bottom of the page.  

12. Once the operation has completed, click the `Go to resource` button.

    <img src="images/creation-completed.png" width="600"> 

13. In the just created OpenAI resource, click the  **Endpoint** link (1)

    <img src="images/created-azure-openai.png" width="1000">  


14. In the **Keys and Enpoint** page copy the value of both **Key 1** (1) and **Endpoint** (2) ❗ because you will need them later.

    <img src="images/key-and-endpoint.png" width="800"> 

15. Navigate back to the previous page and click the `Go to Azure OpenAI Studio`(2) button.
16. In the Azure OpenAI studio portal click the `Deployments` menu on the left (1) and then `Create new deployment`.  

    <img src="images/create-deployment.png" width="800"> 

17. On the **Deploy model** form use the following values. 
    1. `Select a model` = `gpt-4`
    2. `Deployment name` = Choose any compatible name and **make a note of it**❗(e.g. *agent-lab*) since you will need this info later.
    3. Set the `Tokens per Minute Rate Limit` to the maximum value of `40K`
    
    <img src="images/deployment-info.png" width="400">

18. Click the `Create` button and wait the deployment to complete.
19. You're done! Now return to configure the lab.







