import requests
from datetime import datetime
import smtplib

MY_LAT = 0
MY_LONG = 0
my_email = "caradelenteja@outlook.com"
password = ""


def iss_near():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])

    # TODO Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "America/Mexico_City",
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour

# TODO If the ISS is close to my current position and it is currently dark

if iss_near() and (hour >= sunset or hour <= sunrise):
    # TODO Then send me an email to tell me to look up.
    with smtplib.SMTP('smtp-mail.outlook.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="alan.starrk@gmail.com",
            msg="Subject:Look Up\n\nThe ISS is above you in the sky.")
