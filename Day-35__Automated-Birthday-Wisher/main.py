from datetime import datetime
import pandas
from random import randint
import smtplib

current_date = (datetime.now().month,datetime.now().day)

data = pandas.read_csv("birthdays.csv")

email = "enter your email here"
password = "enter your password here"

birthday_dict = {(data_row.month,data_row.day): data_row for (index,data_row) in data.iterrows()}

if current_date in birthday_dict:
    birthday_person = birthday_dict[current_date]
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as birthday_letter:
        content = birthday_letter.read()
        new_content = content.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email,password)
        connection.sendmail(from_addr=email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday\n\n{new_content}")


