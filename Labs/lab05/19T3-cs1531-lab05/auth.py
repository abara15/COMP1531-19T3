# Author: @abara15 (GitHub)
from flask import Flask, request
from json import dumps
import string
import random

APP = Flask(__name__)

def random_string(string_length=10):
    # Generates a random string of length string_length = 10.
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(string_length))

password = ""
secret = ""
token = random_string()

@APP.route('/user/create', methods=['POST'])
def create_user():
    global token
    global password
    global secret
    password = request.form['password']
    secret = request.form['secret']
    return dumps({
        'token' : token
    })

@APP.route('/user/connect', methods=['PUT'])
def connect_user():
    global token
    global password
    password = request.form['password']
    return dumps({
        'token' : token
    })

@APP.route('/user/secret', methods=['GET'])
def get_secret():
    global token
    # token = request.form['token']
    token = request.args['token']
    return dumps({
        'secret' : secret
    })

if __name__ == '__main__':
    APP.run(port=25000)