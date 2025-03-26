import requests

api_key = "0052838b238b4443ae73d02e57b3aa1b"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2025-02-26&sortBy=publishedAt&apiKey="
       "0052838b238b4443ae73d02e57b3aa1b")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])