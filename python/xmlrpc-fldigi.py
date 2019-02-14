from xmlrpclib import ServerProxy, Error
# should be localhost below , using example.com avoids email spam filters.
fldigi = "http://localhost:7362"
server = ServerProxy(fldigi)
server.text.add_tx("ASDF^r")
server.main.tx()
