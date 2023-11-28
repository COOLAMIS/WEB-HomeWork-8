from mongoengine import *

connect(host="mongodb+srv://userhw08:159357@cluster0.6opbneh.mongodb.net/?retryWrites=true&w=majority", ssl=True)
              
class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=50)
    description = StringField(max_length=120)

class Quotes(Document):
    quote = StringField(max_length=150, required=True)
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=70))
    meta = {'allow_inheritance': True}

class TextPost(Quotes):
    content = StringField()

