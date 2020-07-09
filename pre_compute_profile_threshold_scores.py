import json
import requests

with open("data/actual/twitter_timeline_385.json", "r") as f:
    data = json.load(f)

# tweets = data["1217043540208783362"][0]["full_text"]
# rc = data["1217043540208783362"][0]["retweet_count"]

adoptor_preference_user = {}
retweet_norm = {}
max_overall = 0
count = 1
for each_user in data:
    print(count)
    count += 1
    hate_tweets = 0
    all_tweets = 0
    max_rt = 0
    for each_tweet in data[each_user]:
        tweet_data = each_tweet["full_text"]
        retweet_count = each_tweet["retweet_count"]
        retweet_count += 1
        if retweet_count > max_rt:
            max_rt = retweet_count
        json_ = {'input_tweet': tweet_data, "model": "D"}
        r = requests.post(url="http://0.0.0.0:8090/api/predict_single",
                          data=json.dumps(json_),
                          headers={
                              'Content-Type': 'application/json',
                              'Accept': 'application/json'
                          })
        label = json.loads(r.text)["pred_class"]
        if label == 0 or label == 1:
            hate_tweets += 1
        all_tweets += 1
    if all_tweets and hate_tweets:
        ratio = hate_tweets / all_tweets
    else:
        ratio = 0
    if max_rt > max_overall:
        max_overall = max_rt
    adoptor_preference_user[each_user] = ratio
    retweet_norm[each_user] = max_rt
for each_user in retweet_norm:
    retweet_norm[each_user] = retweet_norm[each_user] / max_overall
