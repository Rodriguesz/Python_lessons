import smtplib
import datetime as dt
import random

date = dt.datetime.now()
# is_monday = date.weekday() == 0
is_monday = True

if is_monday:
    with open("Day 32/quotes.txt", encoding="utf-8") as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes).encode("utf-8")
    print(quote)

    my_email = "leobruno2k18@gmail.com"
    password = "xoyx omok bhel nlww"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="venom.extreme682@gmail.com", 
            msg=f"Subject:Monday Motivation\n\n{quote}"
            )
