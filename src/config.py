import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')

API_ID = config['Telegram']['API_ID']
API_HASH = config['Telegram']['API_HASH']
BOT_TOKEN = config['Telegram']['BOT_TOKEN']
SOURCE_GROUP = int(config['Telegram']['SOURCE_GROUP'])
DESTINATION_GROUP = int(config['Telegram']['DESTINATION_GROUP'])