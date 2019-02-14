#!/usr/bin/env python3
from xmlrpc import ServerProxy

#This only works if the remote python xmlrpc server ran the .register_introspection_functions()
#you can also get help documentation for the method (if it exists) by running:
#ServerProxy('http://localhost:2121').system.methodHelp('METHODNAMEHERE')
ServerProxy('http://localhost:2121').system.listMethods()