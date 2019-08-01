import os
import requests
from flask import Flask, request, jsonify
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

TOKEN = os.environ['TOKEN']
API_URL = f'https://api.telegram.org/bot{TOKEN}/'
CHAT_ID=-1001435572035

@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method == 'POST':
    parsed_request = request.get_json()

    order = parsed_request['order']
    send_message(order)

    return jsonify(parsed_request)

  return '<h1>Hello, bookstore bot!</h1>'

def send_message(message=''):
  url = API_URL + 'sendMessage'
  body = {
    'chat_id': CHAT_ID,
    'text': message
  }
  return requests.post(url, json=body)

def main():
  app.run()

if __name__ == '__main__':
  main()
