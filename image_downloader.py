import requests

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Cat_poster_1.jpg/520px-Cat_poster_1.jpg"

response = requests.get(url)

with open("image.jpg", "wb") as file:
    file.write(response.content)