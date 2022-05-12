import datetime as dt
import pandas as pd
import smtplib
import random

MY_EMAIL = "TestingEmailSMTP1@gmail.com"
PASSWORD = ""

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

now = dt.datetime.now()
month = now.month
day = now.day

df = pd.read_csv("birthdays.csv")
b_dict = df.to_dict('records')

letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# 2. Check if today matches a birthday in the birthdays.csv
for record in b_dict:
    if record['month'] == month and record['day'] == day:
        name = record['name']
        with open(f"letter_templates/{random.choice(letter_list)}") as file:
            msg = file.read()
            msg = msg.replace("[NAME]", name)

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=record['email'],
                msg=f"Subject:Happy Birthday!\n\n{msg}"
            )
        print(f"Email sent to {name}!")
