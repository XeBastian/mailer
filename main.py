import smtplib
from email.mime.text import MIMEText
import datetime as dt
import random
from typing import List, Any

sender = "" #add your email here
senderPassword = "" #add the password here
f'''
For the password, first go to your test email account and manage it. 
Click on security tab and enable 2FA
Search for App Passwords and add an app under 'Other Section'
once done, copy the password and paste it above under {senderPassword}
'''
subject = "Testing sending from Code"
body = "Hey Ernest, I am doing this just to send you the email and remind you 20 years later " \
       "that you did this on your computer directly from code.The year is 2023 and today is Friday 12 May "
receiver = "ernestsebah@gmail.com"

# connection = smtplib.SMTP("smtp.google.com")

# create the message
message = MIMEText(body)
message["From"] = sender
message["To"] = receiver
message["Subject"] = subject


# connect and send the email
def send_email(mail_body):
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.login(sender, senderPassword)
        server.sendmail(sender, receiver, MIMEText(mail_body).as_string())


#


lines: list[str] = []

with open("quotes.txt", "r") as file:
    # noinspection PyRedeclaration
    lines = [line.strip() for line in file]


def send_friday_mail():
    print(dt.datetime.now().weekday())
    now = dt.datetime.now().weekday()

    if now == 4:
        mail_body = lines[random.randint(0, len(lines))]
        send_email(f"A Motivational Quote as you drink today \n\n{mail_body}")
        print("Email Sent successfully!")


send_friday_mail()
