import pandas

data = pandas.read_csv("Day 25/squirrel challenge/squirrel_data.csv")
# returns all row that contains "Gray" in the "Primary Fur Color" collumn
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])


data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrel_count, black_squirrel_count, red_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Day 25/squirrel challenge/squirrel_count.csv")