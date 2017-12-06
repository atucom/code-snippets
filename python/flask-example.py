#!/usr/bin/env python3
# Works in both 2 and 3
# Currently all this does is store data sent to /set/<datahere> 
# and retrieves data using /get/
from flask import Flask

app = Flask(__name__)

data_holder = []
@app.route("/")
def hello_world():
	return """This is the root page and Hello!
			<br>
			Store data using /set/<datahere>
			<br>
			Get a listing of the data using /get/
	"""

@app.route("/set/<data>")
def setdata(data):
	data_holder.append(data)
	coment = "You are setting the data:" + str(data)
	return coment

@app.route("/get/")
def getdata():
	return str(data_holder)

if __name__ == "__main__":
	app.run()