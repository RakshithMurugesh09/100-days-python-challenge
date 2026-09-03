import requests
from datetime import datetime, timedelta
import os


TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ALPHAVANTAGE_API = os.getenv("ALPHAVANTAGE_API")
STOCK = "IBM"
COMPANY_NAME = "IBM"
NEWS_API = os.getenv("NEWS_API")
alphavantage_url = 'https://www.alphavantage.co/query'
news_url = 'https://newsapi.org/v2/everything'


# STEP 1: Get stocks

def get_stocks():
    stock_params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": ALPHAVANTAGE_API,
    }

    stock_data = requests.get(alphavantage_url, params=stock_params)
    stock_data.raise_for_status()
    stocks = stock_data.json()["Time Series (Daily)"]
    return stocks

# STEP 2 Get news.

def get_news():
    news_params = {
        "q": COMPANY_NAME,
        "from": yesterday_formatted,
        "to": day_before_yesterday_formatted,
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": 3,
        "apiKey": NEWS_API,
    }
    request = requests.get(news_url, params=news_params)
    request.raise_for_status()
    news_data = request.json()['articles']

    return news_data


# Get dates needed

today = datetime.now()

yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

yesterday_formatted = yesterday.strftime("%m-%d-%Y")
day_before_yesterday_formatted = day_before_yesterday.strftime("%m-%d-%Y")

stock_yesterday = get_stocks()[yesterday_formatted]["4. close"]
stock_day_before_yesterday = get_stocks()[day_before_yesterday_formatted]["4. close"]

price_difference = float(stock_yesterday) - float(stock_day_before_yesterday)
percent_diff = abs(price_difference / float(stock_yesterday) * 100)


# STEP 3: Send a message

def send_telegram_message(message):
    parameters = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
    }

    response = requests.post(url=f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", params=parameters)
    response.raise_for_status()
    data = response.json()
    return data


if percent_diff >= 1:
    for article in range(3):
        title = get_news()[article]['title']
        brief = get_news()[article]['description']
        message = f"{STOCK}: \n Headline: {title} \n Brief: {brief}"
        send_telegram_message(message)

else:
    send_telegram_message("No significant change")