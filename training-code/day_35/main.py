from twilio.rest import Client

account_sid = 'AC159c751fc2cc3480e9b45b5ad9cb61c7'
auth_token = '60a9a7509ebb03f8a8c7455f6e889f7c'  
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+17083407309', 
  body='what are you doing',
  to='+916281459844' 
)

print(message.sid)










