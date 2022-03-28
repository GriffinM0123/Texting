import win32com.client
from twilio.rest import Client


outlook = win32com.client.Dispatch("Outlook.Application")

outlook_ns = outlook.GetNamespace("MAPI")



myfolder = outlook_ns.Folders['Griffin_McGuckin1@baylor.edu'].Folders['Inbox']

messages = myfolder.Items

count = 0

for message in messages:

    count+=1

    #if message.UnRead:
     #   print(message.sender)
      #  print(message.subject)
#
 #       if 'absence' in message.subject:
  #          print("Found message with absence")
#
 #           Msg = outlook.CreateItem(0)
  #          Msg.Importance = 1
   #         Msg.Subject = 'Got your ' + message.subject + ' email'
    #        Msg.HTMLBody = "Hi" + message.sender +"\n" + " sorry you are not well"
#
 #           Msg.To = message.sender.GetExchangeUser().PrimarySmtpAddress
  #          Msg.ReadReceiptRequested = True
#
 #           Msg.Send()

accountSID = 'AC31a443f768547cfb55cc1feb94765730'

authToken = '8da4ab9e32bd8e07ac656d8dda05554a'

Client = Client(accountSID, authToken)

TwilioNumber = "+17622486473"

mycellphone = "+19703906757"


textmessage = Client.messages.create(to=mycellphone, from_=TwilioNumber, body=count)

print(textmessage.status)

