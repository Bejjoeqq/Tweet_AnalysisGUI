import tweepy
import datetime
import re
def txtProc(txt):
	hasil = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", txt).split()).lower()
	return hasil
def getTweet(n=3):
	key = ""
	secretKey = ""
	token = ""
	tokenSecret = ""

	auth = tweepy.OAuthHandler(key,secretKey)
	auth.set_access_token(token,tokenSecret)
	api = tweepy.API(auth)

	tday=tday=datetime.date.today() - datetime.timedelta(days=5)
	search_words = "vaksin covid"
	date_since = str(tday)
	new_search = search_words + " -filter:retweets"

	tweets = tweepy.Cursor(api.search, q=new_search, lang="id", since=date_since).items(n)

	items = []
	for tweet in tweets:
		item = []
		item.append(tweet.id)
		item.append(tweet.user.screen_name)
		item.append(txtProc(tweet.text))
		item.append(tweet.created_at)
		items.append(item)
	return items