import zmq


def test():
    return "It Works!"


def my_sum(a, b):
    return a+b


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5555")

while True:
    #  Wait for request from client
    message = socket.recv()
    print("Received request: %s" % message)

    try:
        r = eval(message)
        print(r)
        socket.send(bytearray(str(r), 'utf-8'))  # send returned value as bytearry to client
    except NameError:
        socket.send(b"Unknown command")
    except:
        socket.send(b"Unknown error")
