#!/usr/bin/env python
#@atucom
#This script will take two arguments from the command line and run them as 
# a fuction name and argument. This allows you to specify function names to
#be explicity run. Weird trick, but could be useful in the future.

import sys

def myfunc(arg):
	print("yolo" + arg)

def main():
	modulename = sys.modules[__name__]
	#funcname = 'myfunc'
	funcname = sys.argv[1]
	#arg = 'qwerty'
	arg = sys.argv[2]


	try:
	    func = getattr(modulename, funcname)
	except AttributeError:
	    print 'function not found "%s" (%s)' % (funcname, arg)
	else:
	    func(arg)

if __name__ == '__main__':
	main()
