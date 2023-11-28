# with open("Day 25/weather_data.csv") as csv_file:
#     data = csv_file.readlines()
#     print(data)

#? working with csv files with csv librarie
# import csv

# with open("Day 25/weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

#? using pandas
import pandas 

data = pandas.read_csv("Day 25/weather_data.csv")

# temp = data["temp"]

# print(type(data)) #? RETURN DATAFRAME
# print(type(temp)) #? RETURN SERIES

# data_dict = data.to_dict() #? creates a dictionary for each collumn
# print(data_dict)

# temp_list = data["temp"].to_list()

#? Calculating avarage temperature
# normal method
# avg_temp = sum(temp_list) / len(temp_list)
# print(f"Avg temp: {avg_temp}")

#with pandas
# print(data["temp"].mean())

#? getting the maximum value of a collumn
# print(data["temp"].max())

#? Get data in Columns
# same results
# print(data["condition"])
# print(data.condition)

#? Get data in Row
# returns the row where de collumn "day" is equal "Monday"
# print(data[data.day == "Monday"])

#? Getting row where the temperature was at its maximum
# print(data[data.temp == data.temp.max()])

#? saving a row in to a variable
# monday = data[data.day == "Monday"]
# # converting the temperature in celsius to farenheit
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

#? Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Leonardo"],
    "scores": [76, 56, 100]
}

data = pandas.DataFrame(data_dict)
#it creates a csv file and the input is the path
data.to_csv("Day 25/new_data.csv")