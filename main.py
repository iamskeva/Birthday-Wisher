import smtplib
import pandas as pd
import datetime as dt
import random

today = dt.datetime.now()
today_tuple = (today.month, today.day)

my_email = "example@email.com"
password = "sample_password"
SENDER = "Example_Sender"

data = pd.read_csv("birthdays.csv")
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
birthdays_dict = {(data_row["month"], data_row["day"]):  data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        send_letter = content.replace("[NAME]", birthdays_dict[today_tuple]["name"]).replace("[SENDER]", SENDER)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="send_example@email.com",
                            msg=f"Subject:Happy Birthday \n\n{send_letter}"
                            )


