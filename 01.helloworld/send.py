import pika

#与MQ服务建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#创建队列
channel.queue_declare(queue = 'hello')

channel.basic_publish(exchange = '',
                      routing_key = 'hello',
                      body = 'Hello World!' )
print("send'Hello World!'")

connection.close()