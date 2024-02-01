import pandas
import datetime

today = datetime.datetime.today()
today_tuple = (today.month, today.day)

data = pandas.read_csv('birthdays.csv')
print(data)
birth_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birth_dict)