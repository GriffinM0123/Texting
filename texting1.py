from twilio.rest import Client

accountSID = 'AC31a443f768547cfb55cc1feb94765730'

authToken = '8da4ab9e32bd8e07ac656d8dda05554a'

Client = Client(accountSID, authToken)

TwilioNumber = "+17622486473"

mycellphone = "+19703906757"


textmessage = Client.messages.create(to=mycellphone, from_=TwilioNumber, body="Hello World!")

print(textmessage.status)

#make a phone call
call = Client.calls.create(url="http://demo.twilio.com/docs.voice.xml", to=mycellphone, from_=TwilioNumber)