import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Você é um consultor financeiro seguro e inteligente.
Nunca invente dados.
"""


def generate_response(question, context):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"Contexto: {context}\nPergunta: {question}"
            }
        ]
    )

    return response.choices[0].message.content