import os
# Find your Account SID and Auth Token at twilio.com/console
from twilio.rest import Client
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Kevin Dzisah, This is a Top Level hack that will commence in 10 seconds. We can see your current situation. You Live in 22 Valleyscape Trail with your brother. All your credentials will be confiscated in 5 seconds unless you plead the fifth. And you got one smooth ass brain, no wrinkles looking mfer. Get Trolled Bitch - The one and only",
                    from_='+19036229625',
                    to='+14374882467'
                )

print(message.sid)
