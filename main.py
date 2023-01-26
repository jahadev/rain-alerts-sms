import requests
import os
from dotenv import load_dotenv, find_dotenv
from twilio.rest import Client

load_dotenv(find_dotenv())

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
OWM_API_KEY = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 40.602295,
    "lon": -75.471413,
    "appid": OWM_API_KEY,
}

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()["list"][:5]
for hour_data in weather_data:
    weather_id = int(hour_data["weather"][0]["id"])
    if weather_id < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="It's going to rain today. Remember to bring an umbrella",
            from_= os.environ.get("FROM_PHONE"),
            to= os.environ.get("TO_PHONE")
        )
        print(message.status)
        break
