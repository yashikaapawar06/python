import smtplib
import random
import os
import pandas as pd
import datetime as dt


my_email = <your-email>
password = <your-app-password>
text_files_path = 'letter_templates'
text_files = os.listdir(text_files_path)

bday_data = pd.read_csv("birthdays.csv")
bday_list = bday_data.to_dict(orient="records")


now = dt.datetime.now()
date = now.day

def read_file():
    with open(f"letter_templates/{letter_to_send}", "r") as letter:
        letter_content = letter.read()
        return letter_content

for items in bday_list:
    if items['day'] == date:
        letter_to_send = random.choice(text_files)
        letter_content = read_file()
        letter_with_name = letter_content.replace("[NAME]",items['name'])
        name = items['name']  #catching hold of items['name'] in a variable so that it can re used when we need to revert the changes in the letters
        with open(f"letter_templates/{letter_to_send}","w") as final_letter:
            final_letter.write(letter_with_name)

letter_content = read_file()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email, to_addrs=<mail-of-the-recipient>,
                        msg=letter_content)

with open(f"letter_templates/{letter_to_send}","w") as message:
    revert_letter_changes = letter_content.replace(name,"[NAME]")
    message.write(revert_letter_changes)
