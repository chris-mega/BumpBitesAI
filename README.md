# BumpBitesAI

## Setup
This project was developed using Python 3.12.8 and used Azure Container Instances, Azure OpenAI and Azure CosmosDB.

For a guide on how to deploy containers to Azure, go [here](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-deploy-app)

### Install dependencies.
- Recommended for local
    ```
    pip install .
    ```
- Recommended for Azure and Docker:
    ```
    pip install -r requirements.txt
    ```
## Run
Locally:
```
python app.py
```

Docker:
```
docker build -t bumpbitesai .
docker run -p 5000:5000 bumpbitesai 
```