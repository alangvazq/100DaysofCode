import datetime as dt
import pandas
import os
import random
import smtplib

# TODO Check if today matches a birthday in the birthdays.csv

my_email = "caradelenteja@outlook.com"
password = ""

now = dt.datetime.now()
today = now.day
month = now.month

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict()

# TODO If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
#  name from birthdays.csv

os.chdir("D:/GitHub/100DaysofCode/Week_5/Day_32/Challenge/letter_templates")
a = os.getcwd()
file = random.randint(1, 3)
text = f"letter_{file}.txt"
o = open(text, "r")

# TODO Send the letter generated in step 3 to that person's email address.

for day in range(len(data_dict["day"])):
    if data_dict["day"][day] == today and data_dict["month"][day] == month:
        with smtplib.SMTP('smtp-mail.outlook.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=f"{data_dict["email"][day]}",
                msg=f"Subject: Happy Birthday\n\n{o.read().replace("[NAME]", f"{data_dict["name"][day]}")}")
