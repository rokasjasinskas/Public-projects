import pytest
from chat_bot_1 import api_answer

@pytest.fixture
def chat_history():
    return [
        {"role": "system", "content": "I am bobby", "name": "bobby"},
        {"role": "user", "content": "What is your name?"},
    ]

def test_api_answer(chat_history):
    message = "What is your name?"
    expected_response = "My name is bobby. I am an AI chatbot. How may I assist you today?"

    response = api_answer(message, chat_history)

    assert response == expected_response

def test_chat_simulation(chat_history):
    message = "Can you provide some information about the chatbot?"
    expected_response = "Sure! This chatbot is powered by AI and can provide assistance and information on various topics. Feel free to ask any questions you have!"

    response = api_answer(message, chat_history)

    assert response == expected_response

def test_arithmetic_operation(chat_history):
    message = "2+2"
    expected_response = "The result of the arithmetic operation 2+2 is 4."

    response = api_answer(message, chat_history)

    assert response == expected_response
