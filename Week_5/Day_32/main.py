# import smtplib
#
# my_email = "caradelenteja@outlook.com"
# password = "murdaowuwjjipjgr"
#
# with smtplib.SMTP('smtp-mail.outlook.com', 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="alan.starrk@gmail.com",
#         msg="Subject: Week\n\nHello")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(year)

import smtplib
import datetime as dt
import random

my_email = "caradelenteja@outlook.com"
password = "xqkijdsdtbmthxdg"

now = dt.datetime.now()
current_day = now.weekday()

with open("quotes.txt") as quotes:
    data = quotes.readlines()

if current_day == 1:
    with smtplib.SMTP('smtp-mail.outlook.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="alan.starrk@gmail.com",
            msg=f"Subject: Week\n\n{random.choice(data)}")
