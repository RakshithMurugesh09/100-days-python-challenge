from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all("tr", class_="athing")

article_data = []

for article in articles:
    title_tag = article.select_one(".titleline a")
    score_tag = article.find_next_sibling("tr").select_one(".score")

    article_data.append({
        "title": title_tag.text,
        "link": title_tag.get("href"),
        "upvotes": int(score_tag.text.split()[0]) if score_tag else 0
    })

top_article = max(article_data, key=lambda article: article["upvotes"])

print(f"Title   : {top_article['title']}")
print(f"Link    : {top_article['link']}")
print(f"Upvotes : {top_article['upvotes']}")