import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    api_version=os.getenv("AZURE_API_VERSION", "2024-05-13"),
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
)

def openai_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[{"role": "system", "content": "You are a nutritionist AI specialized in pregnancy."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
