import requests
import json

query = input("What type of news are you interested in? ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2023-06-15&sortBy=publishedAt&apiKey=9b26984f12a94bbdbd2a1a73132ed3e5"

r = requests.get(url)

news = json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("--------------------------------------")