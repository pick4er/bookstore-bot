import os
import requests
from flask import Flask, request, jsonify
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

TOKEN = os.environ['TOKEN']
API_URL = f'https://api.telegram.org/bot{TOKEN}/'

@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method == 'POST':
    parsed_request = request.get_json()

    message = parsed_request['message']
    chat_id = message['chat']['id']
    message_text = message['text']
    send_message(chat_id, message_text)

    return jsonify(parsed_request)

  return '<h1>Hello, bookstore bot!</h1>'

def send_message(chat_id, message=''):
  url = API_URL + 'sendMessage'
  body = {
    'chat_id': chat_id,
    'text': message,
  }
  return requests.post(url, json=body)

def main():
  app.run()

if __name__ == '__main__':
  main()
