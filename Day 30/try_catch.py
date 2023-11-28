
#? Try catch exception
# #try to do this
# try:
#     file = open("Day 30/file_that_not_exist.txt")
#     a_dictionary = {"key": "value"}
#     # print(a_dictionary["key"])
#     print(a_dictionary["fefefefe"])
# #do this if there was an exception
# except FileNotFoundError:
#     file = open("Day 30/file_that_not_exist.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# #do this if there was no error
# else:
#     print("There was no error")
# #do it regardless of the result
# finally:
#     file.close()
#     print("End of code")

#? Raising erros
height = float(input("Height: "))
weight = int(input("Weight: "))


if height >= 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2