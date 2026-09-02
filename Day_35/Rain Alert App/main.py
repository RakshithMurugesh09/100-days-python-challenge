import os
import requests
import datetime

API_KEY = os.environ.get("WEATHER_API_KEY")
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
MY_LAT = 12.9570
MY_LONG = 77.5609

URL = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "units": "metric"
}


def send_telegram_message(message):

    telegram_params = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
    }

    response = requests.get(url=f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
                            params=telegram_params, timeout=5)
    response.raise_for_status()
    data = response.json()
    return data

def send_telegram_stickers():

    requests.get(
            url=f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendSticker",
            params={
                "chat_id": TELEGRAM_CHAT_ID,
                "sticker": "CAACAgUAAxkBAAMSapg4jPfRUxcTUoSSWXe77gnwwskAAk0IAAJCtnFUXQFZLdsmkuc9BA"
            },
            timeout=5
        )

def weather_api():
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    city = data["city"]["name"]
    today = datetime.date.today()

    weather_report = []
    will_rain = False

    for forecast in data["list"]:
        forecast_date = forecast["dt_txt"].split(" ")[0]

        if forecast_date == today.strftime("%Y-%m-%d"):
            time = forecast["dt_txt"].split(" ")[1][:5]
            description = forecast["weather"][0]["description"].title()
            temp = forecast["main"]["temp"]
            condition_code = forecast["weather"][0]["id"]

            weather_report.append(
                f"🕒 {time}\n"
                f"🌡️ Temp: {temp}°C\n"
                f"🌤️ Weather: {description}\n"
                f"🆔 Code: {condition_code}\n"
            )

            if condition_code < 700:
                will_rain = True

    message = (
        f"📍 Weather Forecast for {city}\n"
        f"📅 {today}\n\n"
        + "\n".join(weather_report)
    )

    send_telegram_message(message)

    if will_rain:
        send_telegram_message(
            "🌧️ Rain is expected today!\n"
            "☂️ Don't forget your umbrella."
        )
        send_telegram_stickers()

    print("✅ Weather report sent to Telegram.")

weather_api()