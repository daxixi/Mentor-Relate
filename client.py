import socket
import pickle
import sys
import os


key_words=sys.argv[1]
client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',1883))
key_words=pickle.dumps(key_words)
client.sendall(key_words)
outputs=client.recv(10240)
outputs=pickle.loads(outputs)
print(outputs)
