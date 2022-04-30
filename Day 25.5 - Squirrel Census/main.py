# with open("weather_data.csv") as data_file:
#     data = data_file.read().splitlines()

# import csv
#
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     iterator = iter(data)
#     next(iterator)
#     for row in iterator:
#         temperatures.append(int(row[1]))
#     print(temperatures)
#     # for row in data:
#     #     print(row[1])
# data = pandas.read_csv("weather_data.csv")
#
# temp_list = data['temp'].to_list()
# #average = round(sum(temp_list) / len(temp_list), 2) Non-panda option
# # average = data['temp'].mean() #Panda option
# # print(average)
# #
# # print(data['temp'].max())
# #
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # print(data.condition)
#
#
# # monday = data[data.day == "Monday"]
# # print(monday.temp * 1.8 + 32)
# # print(data[data.temp == data.temp.max()])
#
#
# #Create a dataframe
#
# data_dict = {
#     "Students": ["Rob", "Chase", "Gidd"],
#     "scores": [76, 55, 63]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

#TODO For each color, total all, then export to new csv
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_data = data["Primary Fur Color"]

fur_data.value_counts().to_csv("Fur Color Count.csv")
