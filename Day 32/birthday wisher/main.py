##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import smtplib
import datetime as dt
import random
import pandas as pd

# date = dt.datetime.now()
date = dt.datetime(day=11, month=9, year=2000)
month = date.month
day = date.day

birthdays = pd.read_csv("Day 32/birthday wisher/birthdays.csv")

for index, row in birthdays.iterrows():
    if row["month"] == month and row["day"] == day:
        name = row["name"].title()
        person_email = row["email"]
        with open(f"Day 32/birthday wisher/letter_templates/letter_{random.randint(1, 3)}.txt") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", name)
        
        my_email = "leobruno2k18@gmail.com"
        password = "xoyx omok bhel nlww"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=person_email,
                msg=f"Subject:Happy birthday!!!!\n\n{letter}"
                )
