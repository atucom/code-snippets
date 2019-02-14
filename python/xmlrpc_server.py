from xmlrpc.server import SimpleXMLRPCServer

class TestClass:
	def __init__(self):
		self.var = 1
	def readme(self):
		return self.var

srv = SimpleXMLRPCServer(("localhost", 2121))
srv.register_introspection_functions()


srv.register_instance(TestClass)
srv.serve_forever()