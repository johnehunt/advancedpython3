import time
import stomp

hosts = [('localhost', 61616)]
conn = stomp.Connection(host_and_ports=hosts)

conn.start()
conn.connect('admin', 'admin', wait=True)

conn.send(body='Hello World' + time.time(), destination='/queue/test')

input('Press enter (publisher) to quit')

conn.disconnect()
