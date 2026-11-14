from bs4 import BeautifulSoup
import requests

url = "https://www.billboard.com/charts/hot-100/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

song_names = soup.select("li ul li h3")



