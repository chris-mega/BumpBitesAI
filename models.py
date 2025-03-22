import os
from openai import AzureOpenAI
from google import genai
from dotenv import load_dotenv, find_dotenv

client = AzureOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    api_version=os.getenv("AZURE_API_VERSION", "2024-05-13"),
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
)

gclient = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def openai_response(prompt):
    response = client.completions.create(
        model="gpt-4o",
        store=True,
        messages=[{"role": "system", "content": "You are a nutritionist AI specialized in pregnancy."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def gemai_response(prompt):
    response = gclient.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text

