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

@app.route("/tone")
def test():
    '''
    texts = [status.text for status in twitter.GetSearch(term="gop", count=10)]
    tones = []
    for text in texts:
        tones.append(tone_analyzer.tone(tone_input=text, sentences=True, content_type='text/plain'))
    '''
    with open('test.json') as data_file:
        tones = json.load(data_file)
    tones = [tone["document_tone"] for tone in tones]
    overall = {}
    for tweet in tones:
        for tone in tweet["tones"]:
            toneId = tone["tone_id"]
            overall[toneId] = overall.get(toneId, 0) + tone["score"]
    overall = [dict([(key, overall[key])]) for key in overall]
    response = {"overall": overall}
    return json.dumps(response)