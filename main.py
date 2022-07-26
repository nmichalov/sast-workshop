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
    user_id = request.cookies.get('UserID')
    return "<p>Welcome to our app %s!" % user_id 

@app.route("/code_injection_1", methods = ['GET', 'POST'])
def code_injection_1():
    filename = request.args.get("filename")
    if filename in ["config","system"]:
        _download_git(filename)

def _download_git(filename):
        os.system("git clone --quiet %s" % (filename))

@app.route("/code_injection_2", methods = ['GET', 'POST'])
def code_injection_2():
    approved_files = {'c' : "config", 's' : "system"}
    filename = request.args.get("filename")
    target_file = approved_files.get(filename)
    _download_git_2(target_file)

def _download_git_2(filename):
        os.system("git clone --quiet %s" % (filename))

@app.route("/code_injection_3", methods = ['GET', 'POST'])
def code_injection_3():
    filename = request.args.get("filename")
    approved_files = []
    approved_files.append(filename)
    target_file = approved_files[0]
    _download_git_3(target_file)

def _download_git_3(filename):
        os.system("git clone --quiet %s" % (filename))