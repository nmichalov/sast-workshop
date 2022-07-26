from flask import Flask, request
import os
import sys

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

# 
@app.route("/xss_1", methods = ['GET'])
def xss_1():
    file_data = open("config/static_values.csv", "r")
    username = file_data.readlines()
    # username = request.environ.get("XSS")
    return "<p>Welcome to our app %s!" % username 

# reflected xss
@app.route("/xss_2", methods = ['GET'])
def xss_2():
    username = request.args.get("username")
    return "<p>Welcome to our app %s!" % username

@app.route("/xss_3", methods = ['GET'])
def xss_3():
    username = 'user'
    return "<p>Welcome to our app %s!" % username 

@app.route("/code_injection_1", methods = ['GET', 'POST'])
def code_injection_1():
    filename = request.args.get("filename")
    if filename in ["config","system"]:
        _download_git(filename)

def _download_git(filename):
        os.system("git clone --quiet %s" % (filename))
