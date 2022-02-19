from random import random
import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Deliverer of JUSTICE'
email['to'] = input("Who shall the email be sent to: ")
email['subject'] = f'You won DESPAIR, JUSTICE SHALL PREVAIL 2022 '

num = int(input("How many emails: "))

email.set_content('I AM HERE TO DECLARE YOUR FATE- REPENTANCE. REPRENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER REPENT SINNER ')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # some hello method to the server
    smtp.starttls()  # connects us securely to the server
    smtp.login('robot.ken.d@gmail.com', '159258357456k')

    for i in range(num):
        smtp.send_message(email)
    print("All good boss man!")
