#!/usr/bin/env python3
from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def redir():
    return redirect('http://google.com')



if __name__ == '__main__':
    app.run(debug=True)
