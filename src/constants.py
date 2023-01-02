import os
import tweepy
import datetime

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
SCREEN_NAME = os.getenv('SCREEN_NAME', 'inu__bot')
API = tweepy.API(tweepy.OAuth2BearerHandler(os.getenv('TWITTER_BEARER')))
STARTED = datetime.datetime.utcnow()