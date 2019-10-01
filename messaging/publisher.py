import time
import stomp

print('Starting Publisher')
hosts = [('localhost', 61616)]
conn = stomp.Connection(host_and_ports=hosts)
conn.start()

print('Connecting to Message broker')
conn.connect('admin', 'admin', wait=True)

print('Publishing a message to /queue/test')
conn.send(body='Hello World - ' + str(time.time()), destination='/queue/test')

input('Press enter (publisher) to quit')

conn.disconnect()
