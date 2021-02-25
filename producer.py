import pika
import json

params = pika.URLParameters(
    "amqps://mhxyppjb:VwK96Emr2dpRfbmiPFcLNoVKecyQQy8o@lionfish.rmq.cloudamqp.com/mhxyppjb"
)

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()

channel.queue_declare(queue="anotheradmin")


def publish(method, body):
    for i in range(10):
        print("Im in publish", body)
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="",
        routing_key="anotheradmin",
        body=json.dumps(body),
        properties=properties,
    )
