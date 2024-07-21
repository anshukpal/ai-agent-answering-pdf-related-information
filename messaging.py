import requests
import json
import os

def post_message_to_slack(text):
    try:
        data={
        'token': os.environ.get('ZANIA_HELP_SLACK_APP_KEY'),
        'channel': 'C07DCG6M9MG',
        'text': text
        }
        response = requests.post('https://slack.com/api/chat.postMessage', data=data)
        return response.json()
    except Exception as e:
        print(e)