import datetime
import dropbox
import os
from twilio.rest import TwilioRestClient

def alert():
    #you can enter your own numbers in these two parameters to put them into your .bashrc
    myNumber = os.environ['MY_NUMBER']
    twilioNumber = os.environ['TWILIO_NUMBER']

    print myNumber

    client = TwilioRestClient()
    #message to send to user
    alert = "Alert: Movement has been detected!\nPlease check logs for the recording."

    message = client.messages.create(to = myNumber,
            from_= twilioNumber,
            body = alert)
