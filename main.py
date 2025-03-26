import requests
from send_email import send_email

api_key = "0052838b238b4443ae73d02e57b3aa1b"
url = ("https://newsapi.org/v2/everything?q=tesla&" \
       "from=2025-02-26&sortBy=publishedAt&apiKey=" \
       "0052838b238b4443ae73d02e57b3aa1b")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    title, description = article["title"], article["description"]

    if title and description is not None:
        body = body + title + "\n" + description + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)