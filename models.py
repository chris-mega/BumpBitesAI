from openai import OpenAI
from google import genai

client = OpenAI(
    api_key="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"
)

client = genai.Client(api_key="AIzaSyDVw8Y8S_CKNMJ4mg9WuPXy_E7GtyEk1As")

def openai_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[{"role": "system", "content": "You are a nutritionist AI specialized in pregnancy."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def gemai_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text

