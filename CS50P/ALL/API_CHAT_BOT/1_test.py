import openai
import sys
import dotenv
import os


dotenv.load_dotenv()
api_code = os.getenv("API_CODE")

openai.api_key = api_code
chatbot_name = sys.argv[1]

def send_message(message, chat_history=[]):
    chat_history.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )
    chat_history.append({"role": "assistant", "content": response.choices[0].message.content.strip()})
    return response.choices[0].message.content.strip()

def main():
    print(f"Starting chat with {chatbot_name}!")
    print("Press Ctrl+D (Cmd+D on Mac) to exit.")

    message = input("You: ")
    token_count = 0

    try:
        while message:
            response = send_message(message)
            token_count += response.count(" ")
            print(f"{chatbot_name}: {response}")
            message = input("You: ")

    except (EOFError, KeyboardInterrupt):
        print(f"\nBye! Total tokens used: {token_count}")

if __name__ == "__main__":
    main()
