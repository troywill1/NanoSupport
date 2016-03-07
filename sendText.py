# Lesson 3.3b: Use Classes
# Mini-Project: Send Text

# It can be important for businesses to automate sending text messages. In
# this mini-project we'll use classes to send a text message using Twilio,
# a library we'll download from the Internet and add to Python.

# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient # -or
# from twilio import rest - how we have been from/import to this point

# Your code here.
# Find these values at https://twilio.com/user/account
account_sid = "ACd9d68547973cd487a15d2c6ea1ff1369"
auth_token = "acd4255b967a116ea62bd6ce9423a2ac"
client = TwilioRestClient(account_sid, auth_token)
# client = rest.TwilioRestClient(account_sid, auth_token) - see above

# The from_ number must be a valid Twilio phone number. The to number can be
# any outgoing number.
message = client.messages.create(to="+15126574319", from_="+15125804419",
                                     body="Bonjour, Troy!")
