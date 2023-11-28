import pika
from models import Contact
from datetime import datetime

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from faker import Faker

import json

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='task_mock', exchange_type='direct')
channel.queue_declare(queue='task_queue', durable=True)
channel.queue_bind(exchange='task_mock', queue='task_queue')

client = MongoClient("mongodb+srv://userhw08:159357@cluster0.6opbneh.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi('1'))

db = client.test

fake = Faker()

def main():
    for _ in range(15):
        Contact_User = Contact(fullname=fake.name(), email=fake.email())

        channel.basic_publish(
            exchange='task_mock',
            routing_key='task_queue',
            body=json.dumps(Contact_User).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(" [x] Sent %r" % Contact_User)
    connection.close()