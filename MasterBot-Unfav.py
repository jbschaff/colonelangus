import requests
from requests_oauthlib import OAuth1
 
CONSUMER_KEY = "mAOjtj7xDvTUWbIgxxAOKEgdN"
CONSUMER_SECRET = "unIDsRM7STbsuPhX4UOpZtIPCmRzU4xPBvKT7rGpBP2zg7eBHB"
 
OAUTH_TOKEN = "2350833008-n6pA4DO5u24xzv86YKIZkhEEVXhIL7C5z1LfD1j"
OAUTH_TOKEN_SECRET = "nEheLzxfcTflBod0ywQCkFhlw2Cgz6jaqbebxcsLgbmv1"
 
def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth
 
if __name__ == "__main__":
        oauth = get_oauth()
         
        for i in xrange(10):
            # get favorites tweet data (maximum 200 per call, "count=200"
            r = requests.get(url="https://api.twitter.com/1.1/favorites/list.json?count=200", auth=oauth)
                    # store fav_ids in a list
            fav_ids = [fav['id'] for fav in r.json()]
            # loop through each fav id and remove from twitter
            for fav in fav_ids :
                data = {'id' : fav}
                response = requests.post(url="https://api.twitter.com/1.1/favorites/destroy.json",auth=oauth,data=data)
            print i