from tweepy import OAuthHandler,Stream,API
from tweepy.streaming import StreamListener
import sys
import json


consumer_key = 'zeHM8aLFlSK5cSnZxVO2pMvqI'
consumer_secret = 'rdg6BeUHA8adNXHABSvfiC8mnGTaAEQRKVjjNnKDeZ2NfNtXbk'
access_token = '128802124-avX5P9k9hduDeCmmpKmrxDqWwQU0rfx24oKkXXfq' 
access_token_secret = 'g9619OZDSO47J77PPaMCZhvMF5SXDmi2VabGo2VUWcZVw'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


class PrintListner(StreamListener):
	def on_status (self,status):
		if not status.text [:3] == 'RT':
			uprint (status.text)
			uprint (status.author.screen_name,
				status.created_at,
				status.source,
				'\n')

	def on_error(self,status_code):
		print ("Error code : {}".format(status_code))
		return True #keep stream alive

	def on_timeout (self):
		print ('Listner timed out !!!')
		return True
def print_to_terminal ():
	listner = PrintListner()
	stream = Stream (auth,listner)
	languages = ('en',)
	stream.sample(languages=languages)

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
	enc = file.encoding
	if enc == 'UTF-8':
		print(*objects, sep=sep, end=end, file=file)
	else:
		f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
		print(*map(f, objects), sep=sep, end=end, file=file)


def pull_down_tweets (screen_name):
	api = API (auth)
	tweets = api.user_timeline (screen_name = screen_name, count = 200)
	for tweet in tweets:
		print (json.dumps (tweet._json , indent = 4))



if __name__=='__main__':
	#print_to_terminal()
	pull_down_tweets(auth.username)
