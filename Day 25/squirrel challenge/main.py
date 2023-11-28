import pandas

data = pandas.read_csv("Day 25/squirrel challenge/squirrel_data.csv")

# print(data["Primary Fur Color"])

black = 0
gray = 0
cinnamon = 0

fur_data = data["Primary Fur Color"]

for row in fur_data:
    if row == "Black":
        black +=1
    elif row == "Gray":
        gray +=1
    elif row == "Cinnamon":
        cinnamon +=1

data_dict = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [black, gray, cinnamon]
}

data = pandas.DataFrame(data_dict)

data.to_csv("Day 25/squirrel challenge/new_data.csv")