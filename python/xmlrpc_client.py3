from xmlrpc.client import ServerProxy

cl = ServerProxy('http://localhost:2121')

print(cl.readme())

