import argparse
from models import Authors, Quotes
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://userhw08:159357@cluster0.6opbneh.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi('1'))

db = client.test

data = {'name': {'Albert Einstein': '6564f0eb92f53b748450046e',
                'Steve Martin': '6564f0ec92f53b7484500472'},
       'tag_id':{'6564f0eb92f53b748450046e':['6564f0ec92f53b748450046f', '6564f0ec92f53b7484500470'],
              '6564f0ec92f53b7484500472': '6564f0ec92f53b7484500473'}}

tags = ["change", "deep-thoughts", "thinking", "world", "inspirational", "life", "live", "miracle", "miracles",
        "adulthood", "success", "value", "humor", "obvious", "simile"]

if __name__ == '__main__':
    while True:
        id_dict = data.get('name')
        id_qoutes = data.get('tag_id')
        input_list = []
        string = ''
        input_user = input('>>>:')
        for i in input_user.split():
            input_list.append(i)
        if input_list[0] == 'name:':
            input_list.pop(0)
            name_author =input_list[0] + ' ' + input_list[1]
            id_author = id_dict.get(name_author)
            tags = id_qoutes.get(id_author)
            for user in Quotes.objects():
                print(user.quote)
        if input_list[0] == 'tag:' or 'tags:':
            input_list.pop(0)
            for i in input_list:
                string += i
            for t in tags:
                if t in string:
                    for tags in Quotes.objects():
                        print(tags.tags)
        if input_user == 'end':
            break
        