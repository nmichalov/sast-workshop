from flask import Flask, request
import os
import sys
import traceback

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/code_injection_1", methods = ['GET', 'POST'])
def code_injection_1():
    filename = request.args.get("filename")
    os.system("git clone --quiet %s" % (filename))

@app.route("/xss", methods = ['GET'])
def xss():
    username = request.args.get("username")
    return "<p>Welcome to our app %s!" % username

@app.route("/info_leak", methods = ['GET'])
def info_leak():
    try:
        val = x[1]
    except Exception:
         return traceback.print_last()