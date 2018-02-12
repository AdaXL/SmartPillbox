import fbchat
from getpass import getpass
username = str('YiciJing')
client = fbchat.Client(username, 'dajidanzyc1992')
no_of_friends = int(1)
for i in range(no_of_friends):
    name = str('John Zhang')
    friends = client.searchForUsers(name)  # return a list of names
    friend = friends[0]
    msg = str(123)
    fbchat.models.ImageAttachment
    sent = client.send(fbchat.models.Message(text = msg), friend.uid)
    sent2 = client.sendLocalImage('/home/yici/Desktop/02-651/IOT/E-T.jpg', None ,friend.uid)
    if sent:
        print("Message sent successfully!")
