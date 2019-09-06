import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True) # durable参数消息持久化
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag) # 消息确认


channel.basic_qos(prefetch_count=1)  # 公平派遣
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()