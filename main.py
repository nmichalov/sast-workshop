from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/xss_1", methods = ['GET'])
def xss_1():
    username = request.environ.get("XSS")
    return "<p>Welcome to our app %s!" % username 

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
    new_command = request.arg.get("command")
    eval("%s" % new_command)