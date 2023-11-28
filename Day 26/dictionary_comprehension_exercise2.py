weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
# def temp_f(temp_c):
#     temp_f = (temp_c*9/5)+32
#     return temp_f

# weather_f = {weekday:temp_f(temp_c) for (weekday, temp_c) in weather_c.items()}

weather_f ={weekday:(temp_c*9/5)+32 for (weekday, temp_c) in weather_c.items()}


print(weather_f)