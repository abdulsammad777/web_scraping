from flask import Flask, request, jsonify
from Whatsapp.wabot.wabot import *
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        bot = WABot(request.json)
        return bot.processing()

if(__name__) == '__main__':
    # testing = WABot(request.json)
    # testing.send_message('+923069029902', "Hello")
    app.run()