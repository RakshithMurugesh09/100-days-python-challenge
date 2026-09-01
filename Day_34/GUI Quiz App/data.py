import requests

parameters = {
    'amount': 15,
    "difficulty": "easy",
    "type": "boolean"
}

url = "https://opentdb.com/api.php"

response = requests.get(url, params=parameters)
response.raise_for_status()

data = response.json()

questions = data['results']
