import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Ken Dzisah'
email['to'] = input("Who shall the email be sent to: ")
email['subject'] = 'Undecided'


email.set_content(html.substitute({'name': "Noob", }), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # some hello method to the server
    smtp.starttls()  # connects us securely to the server
    smtp.login('robot.ken.d@gmail.com', '159258357456k')
    smtp.send_message(email)
    print("All good boss man!")
