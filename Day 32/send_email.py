import smtplib

my_email = "leobruno2k18@gmail.com"
password = "xoyx omok bhel nlww"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="venom.extreme682@gmail.com", 
        msg="Subject:Hello\n\nThis is the body of my email"
        )

