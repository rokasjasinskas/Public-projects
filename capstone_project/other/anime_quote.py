import requests

response = requests.get("https://animechan.xyz/api/random")
quote = response.json()
print(quote)
