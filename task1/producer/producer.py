#!/usr/bin/env python
import pika
import sys
import time
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbitmq', port = 5672))
channel = connection.channel()

channel.queue_declare(queue='hello')

print "Producer started sending messages"

for line in sys.stdin:
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=line)
print "All messages sent"
time.sleep(8) 
#Time to checks in consumer's start.sh
connection.close()

