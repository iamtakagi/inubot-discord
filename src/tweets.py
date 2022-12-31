from constants import SCREEN_NAME, API
import os
import random

def fetch_tweets() -> None:
    tweets = []
    max_id = None

    while True:
        tw = ""
        if max_id:
            try:
                tw = API.user_timeline(
                    screen_name=SCREEN_NAME, trim_user=True, include_rts=False, count=200, max_id=max_id)
            except Exception:
                pass
        else:
            try:
                tw = API.user_timeline(
                    screen_name=SCREEN_NAME, trim_user=True, include_rts=False, count=200)
            except Exception:
                pass
        if len(tw) < 1:
            break
        max_id = tw[-1].id - 1
        [tweets.append(tweet.text.replace("\n", ""))
            for tweet in tw if "http" not in tweet.text and "@" not in tweet.text]

    print("done")
    print(f"{len(tweets)}tweets")

    if os.path.isfile("data/tweets.txt"):
        with open("data/tweets.txt", mode='r+') as current:
            current.truncate(0)
            current.close()

    with open("data/tweets.txt", "w") as f:
        f.write("\n".join(tweets))

def load_tweets() -> str or list: 
    if not os.path.isfile("data/tweets.txt"):
        return []
    with open("data/tweets.txt", "r") as f:
        tweets = f.read()
    return tweets


def load_tweets_line() -> list[str]: 
    if not os.path.isfile("data/tweets.txt"):
        return []
    with open("data/tweets.txt", "r") as f:
        tweets = [s.strip() for s in f.readlines()]
        tweets = list(filter(None, tweets))
        tweets = [t.replace(' ', '') for t in tweets]
    return tweets


def get_random_tweet() -> str: 
    return random.choice(load_tweets_line())
