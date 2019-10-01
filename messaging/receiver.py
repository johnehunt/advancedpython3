import stomp


class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)

    def on_message(self, headers, message):
        print('received a message "%s"' % message)


print('Starting Receiver')
hosts = [('localhost', 61616)]
conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.start()

print('Connecting to Message Broker')
conn.connect('admin', 'admin', wait=True)

print('Subscribing to queue/test')
conn.subscribe(destination='/queue/test', id=1, ack='auto')

input('Press enter to quit (Receiver)\n')
conn.disconnect()
