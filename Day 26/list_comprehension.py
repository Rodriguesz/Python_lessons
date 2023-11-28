number =[1, 2, 3]
new_list = [n+1 for n in number]
new_list2 = [n / 2 for n in number]
# print(new_list)
# print(new_list2)

name = "Leonardo"

letter_list = [letter for letter in name]
# print(letter_list)

double_range = [n * 2 for n in range(1, 5)]
# print(double_range)

names =["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) <= 4]
# print(short_names)

long_names = [name.upper() for name in names if len(name) >=5]
print(long_names)
