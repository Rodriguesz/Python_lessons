with open("Day 26/data overlap exercise/file1.txt") as file:
    list1 = file.readlines()
    new_list1 = [int(item.strip("\n")) for item in list1]
    
    
with open("Day 26/data overlap exercise/file2.txt") as file2:
    list2 = file2.readlines()
    new_list2 = [int(item.strip("\n")) for item in list2]

result = [n for n in new_list1 if n in new_list2]


# Write your code above 👆
print(result)
