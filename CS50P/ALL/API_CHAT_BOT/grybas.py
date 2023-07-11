import os
import openai
import sys
import dotenv

dotenv.load_dotenv()

max_token = 50

openai.api_key = os.getenv("API_CODE")
ai_name = "Grybas"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"I am {ai_name}", "name": f"{ai_name}"},
        {"role": "user", "content": f"Your name is {ai_name}"},
        {"role": "system", "content": f"AI chat bot name is {ai_name}", "name": f"{ai_name}"},
        {"role": "user", "content": "What is your name?"},
        {"role": "system", "content": f"I am {ai_name}", "name": f"{ai_name}"},
        {"role": "user", "content": f"Your name is {ai_name}"},
        {"role": "system", "content": f"yes you are right. As a chatbot I like to call myself {ai_name}", "name": f"{ai_name}"},
        {"role": "user", "content": f"What is your name?"},

    ],
    temperature=0.2,
    n=1,
    stop=None,
    max_tokens= max_token,
    presence_penalty=-2,
    frequency_penalty=-2,
)

# Accessing the assistant's response
assistant_response = completion.choices[0].message["content"]
print(assistant_response)
