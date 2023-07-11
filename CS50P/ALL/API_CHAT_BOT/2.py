def tokens_calc (response):
    word_count = len(response.split())
    return word_count

response = "My name is bob"

print(tokens_calc(response))
