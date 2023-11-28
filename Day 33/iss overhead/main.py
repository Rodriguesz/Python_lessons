import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -22.751070 # Your latitude
MY_LONG = -47.333260 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # iss_latitude = -22.751070 
    # iss_longitude = -47.333260

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_dark():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }
    
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    

    # time_now = datetime(day=11, month=9, year=2000, hour=22)
    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour < sunrise:
        return True


while True:
    time.sleep(secs=60)
    #If the ISS is close to my current position
    # and it is currently dark
    if is_iss_overhead() and is_dark():
        # Then send me an email to tell me to look up.

        my_email = "leobruno2k18@gmail.com"
        password = "xoyx omok bhel nlww"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs="venom.extreme682@gmail.com", 
                msg="Subject:Heeeey, look up!\n\nThe iss is abouve you =D"
                )

# BONUS: run the code every 60 seconds.



