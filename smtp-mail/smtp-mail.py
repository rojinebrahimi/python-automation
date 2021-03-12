#!/usr/bin/python
import smtplib as sl
import re
from email.mime.text import MIMEText


# -- Validates the entered email address ------------------------------
def validate_email(email):
    valid = False
    regex = '[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'
    if re.search(regex, email):
        valid = True
    return valid


# -- Fetches user input for the email to send -------------------------
sender_mail = input("Enter the sending mail address, please: ")
gmail_password = input("Enter your Gmail password: ")
receiver_mail = input("Enter the receiving mail address, please: ")


# -- SMTP server configuration ----------------------------------------
smtp_server = 'smtp.gmail.com'
port = 587

if validate_email(sender_mail) and validate_email(receiver_mail):
    subject = input("Enter the subject of the mail, please: ")
    text = input("Enter the text message which should be sent: ")

    mail_message = MIMEText(text)
    mail_message['Subject'] = subject
    mail_message['From'] = sender_mail
    mail_message['To'] = receiver_mail

    server = sl.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_mail, gmail_password)
    try:
        server.sendmail(sender_mail, receiver_mail, mail_message.as_string())
        print(f"\n{'📗'} Mail was sent successfully.")
        server.quit()
    except sl.SMTPException as e:
        print(e)
        print(f"\n{'🛑'} The mail can not be send.")

else:
    print(f"\n{'🛑'} Entered mails are not in correct format.")
    exit()
