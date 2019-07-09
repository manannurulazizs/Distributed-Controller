import pexpect
import time
import pika
import threading

def subs ():
  url = 'amqp://cuvzmrst:QxvOG1o9BnghrJdjq1AV1eSHbDN73vLD@dinosaur.rmq.cloudamqp.com/cuvzmrst'

  params = pika.URLParameters(url)
  connection = pika.BlockingConnection(params)
  channel = connection.channel()
  channel.queue_declare(queue='migration', durable=True)

  def callback(ch, method, properties, body):
    pxpct.sendline("py net.get('switch"+body[16]+"').start([Controller1])")
    pxpct.expect('mininet>')
    print("Switch migration : %r" % body)
    time.sleep(body.count(b'.'))
    print("")
    ch.basic_ack(delivery_tag = method.delivery_tag)

  channel.basic_qos(prefetch_count=1)
  channel.basic_consume(callback,
                      queue='migration')

  channel.start_consuming()

def subs2 ():
  url = 'amqp://cuvzmrst:QxvOG1o9BnghrJdjq1AV1eSHbDN73vLD@dinosaur.rmq.cloudamqp.com/cuvzmrst'

  params = pika.URLParameters(url)
  connection = pika.BlockingConnection(params)
  channel = connection.channel()
  channel.queue_declare(queue='migration2', durable=True)

  def callback(ch, method, properties, body):
    pxpct.sendline("py net.get('switch"+body[16]+"').start([Controller2])")
    pxpct.expect('mininet>')
    print("Switch migration : %r" % body)
    time.sleep(body.count(b'.'))
    print("")
    ch.basic_ack(delivery_tag = method.delivery_tag)

  channel.basic_qos(prefetch_count=1)
  channel.basic_consume(callback,
                      queue='migration2')

  channel.start_consuming()

if __name__=="__main__":
    threading._start_new_thread(subs, ())
    threading._start_new_thread(subs2, ())
    global pxpct
    pxpct = pexpect.spawn('python',['Topologi.py'])
    pxpct.expect('mininet>')
    pxpct.sendline("py net.get('switch1').start([Controller1])")
    pxpct.expect('mininet>')
    pxpct.sendline("py net.get('switch2').start([Controller1])")
    pxpct.expect('mininet>')
    pxpct.sendline("py net.get('switch3').start([Controller2])")
    pxpct.expect('mininet>')
    pxpct.sendline("py net.get('switch4').start([Controller2])")
    pxpct.expect('mininet>')

    pxpct.sendline('xterm h1 h8')
    pxpct.expect('mininet>')

    while True:
        pass
