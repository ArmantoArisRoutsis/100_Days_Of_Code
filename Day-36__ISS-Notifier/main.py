import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 37.983810
MY_LNG = 23.727539
#Add your email
MY_EMAIL = "name@email.com"
#Add your email password
MY_PASSWORD = "PASSWORD12345"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["longitude"]

    iss_position = (longitude,latitude)

    if MY_LAT - 5 <= iss_position <= MY_LAT +5 and MY_LNG - 5 <= iss_position <= MY_LNG +5:
        return True

def is_night():
    parameters = {
        "lat":MY_LAT,"lng":MY_LNG,"formatted":0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    print(data)

    time_now = datetime.now().hour()
    if time_now >= sunset or time_now<= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up!\n\nThe ISS is above you!"
        )