# input from comand line with API key and botname
# API joint with openait CHAT GPT
# User in input as first message
# chatgpt answers with remembering his name
# user continue conversation
# chat gpt answers
# all the time count tokens which was used
# program should stop if it is too long = used too much tokens
# if pressed ctrl+d print bye and print number of tokens
#
#

# imports:
import os
import openai
import sys
import dotenv

dotenv.load_dotenv()

openai.api_key = os.getenv("API_CODE")
ai_name = sys.argv[1]

max_token = 50


def main():
    def user_input():
        message = input("User: ")
        return message

    print(f"Starting chat with {ai_name}!")
    print("Press Ctrl+D (Cmd+D on Mac) to exit.")

    token_count = 0
    global max_token
    try:
        message = user_input()
        while token_count < max_token:
            response = api_answer(message)
            token_count += tokens_calc(response)

            print(f"AI: {response}")
            message = user_input()

    except (EOFError, KeyboardInterrupt):
        the_end(token_count)


def tokens_calc(response):
    word_count = len(response.split())
    return word_count


def api_answer(message, chat_history=[]):
    global max_token
    global ai_name
    chat_history = [
        {"role": "system", "content": f"I am {ai_name}", "name": f"{ai_name}"},
        {"role": "user", "content": f"Your name is {ai_name}"},
        {
            "role": "system",
            "content": f"AI chat bot name is {ai_name}",
            "name": f"{ai_name}",
        },
        {"role": "user", "content": "As a ChatBot you should identify as {ai_name}"},
        {
            "role": "system",
            "content": f"As a ChatBot i identify as {ai_name}",
            "name": f"{ai_name}",
        },
        {"role": "user", "content": "What is your name?"},
        {"role": "system", "content": f"I am {ai_name}", "name": f"{ai_name}"},
        {"role": "user", "content": f"Your name is {ai_name}"},
        {
            "role": "system",
            "content": f"yes you are right. As a chatbot I like to call myself {ai_name}",
            "name": f"{ai_name}",
        },
        {"role": "user", "content": message},
    ]
    chat_history.append({"role": "user", "content": message})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history,
        temperature=0.2,
        n=1,
        stop=None,
        max_tokens=max_token,
        presence_penalty=-2,
        frequency_penalty=0,
    )
    response = completion.choices[0].message["content"]
    chat_history.append({"role": "system", "content": response.strip()})

    return response


def the_end(token_count):
    global max_token
    print(f"\nBye: {token_count}")
    sys.exit(0)


if __name__ == "__main__":
    main()
