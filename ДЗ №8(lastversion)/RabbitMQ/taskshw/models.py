from mongoengine import *

connect(host="mongodb+srv://userhw08:159357@cluster0.6opbneh.mongodb.net/?retryWrites=true&w=majority", ssl=True)
              
class Contact(Document):
    fullname = StringField()
    email = StringField(max_length=50)