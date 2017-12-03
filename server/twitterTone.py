from flask import Flask
from watson_developer_cloud import ToneAnalyzerV3
import twitter as twitterClient
import json

with open('keys.json') as data_file:
    data = json.load(data_file)

tone_analyzer = ToneAnalyzerV3(
  username=data["username"],
  password=data["password"],
  version='2017-09-26'
)

twitter = twitterClient.Api(consumer_key=data["consumer_key"],
                  consumer_secret=data["consumer_secret"],
                  access_token_key=data["access_token_key"],
                  access_token_secret=data["access_token_secret"],
                  sleep_on_rate_limit=False)

app = Flask(__name__)


@app.route("/tone/<term>")
def test(term):
    term = term.lower()
    raw = "q={}%20-filter%3Aretweets%20AND%20-filter%3Areplies&count=50&tweet_mode=extended&result_type=mixed".format(term)
    tweets = [{
        "text": status.full_text, 
        "user": status.user.name, 
        "userImage": status.user.profile_image_url, 
        "id_str": str(status.user.id),
        "screen_name": status.user.screen_name,
        "tweet_id": status.id_str
        } for status in twitter.GetSearch(raw_query=raw)]
    #with open('twitterTest.json') as data:
        #tweets = json.load(data)
    tones = []
    for tweet in tweets:
        tones.append(tone_analyzer.tone(tone_input=tweet["text"], sentences=True, content_type='text/plain'))
    #with open('test.json') as data_file:
        #tones = json.load(data_file)
    tones = [tone["document_tone"] for tone in tones]
    overall = {}
    toneNames = {}
    for tweet in tones:
        for tone in tweet["tones"]:
            toneId = tone["tone_id"]
            overall[toneId] = overall.get(toneId, 0) + tone["score"]
            toneNames[toneId] = tone["tone_name"]
    overall = [{"tone_name": toneNames[key], "score": overall[key]} for key in overall]
    individual = []
    i = 0
    for tweet in tweets:
        tweet["tones"] = tones[i]["tones"]
        i = i + 1
    response = {"overall": overall, "individual": tweets}
    return json.dumps(response)
