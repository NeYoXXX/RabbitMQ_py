import pika

#与MQ服务建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#创建队列
# （文档上表示，此操作是等幂的，如果在发送时创建了队列则在接收时不需要重新创建，如果创建也没问题，官方文档支持在此队列创建）
channel.queue_declare(queue = 'hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
