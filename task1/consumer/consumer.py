#!/usr/bin/env python
import pika

from pymongo import MongoClient
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbitmq', port = 5672))
channel = connection.channel()

channel.queue_declare(queue='hello')

dbConnection = MongoClient(host = 'database', port = 27017)
db = dbConnection.myDatabase
collection = db.myCollection

print '[*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    collection.save({"message":body})


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()

