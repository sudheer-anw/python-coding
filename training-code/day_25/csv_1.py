# with open ("day_25/weather_data.csv") as data_file:
#     data = data_file.read()
#     print(data)

# import csv

# with open("day_25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)

#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# import pandas

# data = pandas.read_csv("day_25/weather_data.csv")
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# average = sum(temp_list)/len(temp_list)
# print(average)

# print(data["temp"].mean())
# print(data["temp"].max())


# print(data[data.day =="Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday)
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)


# data_dict = {
#     "students":["malli","mani","siddi"],
#     "marks":[40,50,70]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("day_25/students.csv")


import pandas

data = pandas.read_csv("day_25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squralle_count = len(data[data["Primary Fur Color"]=="Gray"])
red_squralle_count = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squralle_count = len(data[data["Primary Fur Color"]=="Black"])
print(f"There are {gray_squralle_count} gray squralles in theis park")
print(f"There are {red_squralle_count} red squralles in theis park")
print(f"There are {black_squralle_count}black squralles in theis park")

data_dict = {
    "fur colour":["Grey","Cinnamon","Black"],
    "count":[2472,392,103]
}
data = pandas.DataFrame(data_dict)
data.to_csv("day_25/squralles.csv")

data = pandas.read_csv("day_25/squralles.csv")
print(data)




      




