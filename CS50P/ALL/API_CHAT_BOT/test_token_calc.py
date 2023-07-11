import chat_bot_1

def test_word_count():
    response = "Hello, how are you?"
    expected_count = 4
    actual_count = chat_bot_1.tokens_calc(response)
    assert actual_count == expected_count

def test_empty_response():
    response = ""
    expected_count = 0
    actual_count = chat_bot_1.tokens_calc(response)
    assert actual_count == expected_count

def test_multiple_spaces():
    response = "This   has  multiple   spaces"
    expected_count = 4
    actual_count = chat_bot_1.tokens_calc(response)
    assert actual_count == expected_count
