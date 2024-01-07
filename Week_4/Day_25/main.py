# import csv
import pandas

# with open("./weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# data_list = data["temp"].to_list()
# print(data_list)
#
# average = sum(data_list) / len(data_list)
# print(average)
#
# print(data["temp"].max())

# print(data["condition"])

# print(type(data[data["day"] == "Friday"]))


# print(data[data["day"] == "Monday"])
# monday = data[data["day"] == "Monday"]["temp"]
# F = (monday * 9/5)+32

# data = pandas.DataFrame(data)
# data.to_csv("new_dara.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(data.groupby("Primary Fur Color").count())