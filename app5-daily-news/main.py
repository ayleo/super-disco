import requests
from send_email import send_email

api_key = "718540ed8be04ab2b8048c9bf564c651"
url = f"https://newsapi.org/v2/everything?q=microsoft&from=2024-03-14&sortBy=publishedAt&apiKey={api_key}&language=en"

# Make a request
response = requests.get(url)

# Get a JSON response
content = response.json()

body = ""
# Extract the title and description of the first 20 articles
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body = ("Subject: Today's News"
                + "\n" + body
                + "\n" + article["publishedAt"]
                + "\n" + article["title"]
                + "\n" + article["description"]
                + article["url"] + 2*"\n")
    else:
        continue
# # Extract the title and description of the first 20 articles
# titleNews = [article["title"] for article in content["articles"][0:20]]
# descriptionNews = [article["description"] for article in content["articles"][0:20]]
# message = "\n".join([f"Title: {titleNews[i]}\nDescription: {descriptionNews[i]}\n" for i in range(len(titleNews))]).encode("utf-8")

body = body.encode("utf-8")

send_email(message=body)