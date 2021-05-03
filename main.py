import requests
import smtplib
import time

MY_EMAIL = "" #Email adresinizi giriniz.
PASSWORD = ""         #Email şifrenizi giriniz.

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "" # Yukarıda linki olan siteden api keyi alın ve girin.
will_rain = False

weather_params = {
    "lat": 42.027973, # Konumuzun kordinatlarını girebilirsiniz.
    "lon": 35.151726,
    "appid": api_key,
    "exclude": "current,minutely,daily",
    "units": "metric",
}

response = requests.get(
    url=OWN_Endpoint,
    params=weather_params
)

response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Weather\n\n Today it will be rainy. Don't forget your umbrella."
        )
