import requests
from send_email import send_email

topic = "tesla"
date = "2025-03-02"

api_key = "0052838b238b4443ae73d02e57b3aa1b"
url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       f"from={date}&sortBy=publishedAt&" \
       "apiKey=0052838b238b4443ae73d02e57b3aa1b&" \
       "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    title, description = article["title"], article["description"]

    if title and description is not None:       # f"Subject: Today's news on {topic.title()}"
        body = (
                "Subject: Today's news" + "\n" \
                + body + title + "\n" \
                + description + "\n" \
                + article["url"] + 2*"\n")

body = body.encode("utf-8")
send_email(message=body)