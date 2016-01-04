import zmq
import json
import numpy as np


class NumpyEncoder(json.JSONEncoder):
    """ Extends JSONEncoder to serialize numpy arrays.
    To use this encoder: json.dumps(<numpy_array>, cls=NumpyEncoder)

    http://stackoverflow.com/questions/3488934/simplejson-and-numpy-array
    """

    def default(self, obj):
        """If input object is an ndarray it will be converted into a dict
        holding dtype, shape and the data.

        :param obj: object to be encoded
        """
        if isinstance(obj, np.ndarray):
            if obj.flags['C_CONTIGUOUS']:
                obj_data = obj.data
            else:
                cont_obj = np.ascontiguousarray(obj)
                assert(cont_obj.flags['C_CONTIGUOUS'])
                obj_data = cont_obj.data
            data_json = obj_data.tolist()
            # data_b64 = base64.b64encode(obj_data)
            return dict(__ndarray__=data_json, dtype=str(obj.dtype), shape=obj.shape)
        # Let the base class default method raise the TypeError
        return json.JSONEncoder(self, obj)


class Test:
    def __init__(self):
        self.var_int = 42
        self.var_double = 12.34
        self.var_string = "Hello World!"
        self.var_bool = True
        self.var_nparray = np.array([1, 2, 3, 4, 5])

    @staticmethod
    def test():
        return "It Works!"

    @staticmethod
    def my_sum(a, b):
        return a+b


# create test object
test = Test()

# open socket for TCP communication
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5555")

while True:
    #  Wait for request from client
    message = socket.recv()
    print("Received request: %s" % message)

    try:
        r = eval(message)
        print("Return value: ", r)
        print("Type: ", type(r))
        socket.send(bytearray(json.dumps(r, cls=NumpyEncoder), 'utf-8'))
    except NameError:
        print("except NameError")
        socket.send(b"Unknown command")
    except SyntaxError:
        print("except SyntaxError")
        socket.send(b"Invalid syntax")
    except:
        print("except")
        socket.send(b"Unknown error")
