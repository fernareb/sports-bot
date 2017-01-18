# import required python packages
import requests
import json
# import bot_settings
from bot_settings import *
from slackclient import SlackClient
import sys

slack_client = SlackClient(SLACK_TOKEN)


def send_message(channel_id, message):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='Gary Payton',
        icon_url='http://i.imgur.com/vB8TtJt.png',
        as_user='false',
        type='message',
        subtype='bot_message'
    )


# api requests
r = requests.get(game_url)
results = r.json()
game_result = r.json()['game_tonight']
print(game_result)

if game_result is True:
    send_message(channel_id, game_message)
else:
    send_message(channel_id, no_game_message)
