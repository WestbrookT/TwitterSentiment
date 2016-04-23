import tweepy, pickle




token = 'YHAvhwQJ83PtPXg9ZMTOrQvYV'

secret_key = 'dJG4yNLqJVc4ALm3yEoV8YYTVYRWCt9onTkaRURRQrhq6xxZp6'



# for i in api.search('texas')['statuses']:
#
#     print(i['user'])
#     print(i['place'])
#     print(i['text'])


class Sentiment:

    token = ''
    key = ''
    _auth = tweepy.OAuthHandler('a', 'a')
    api = tweepy.API


    c = open('classifier.py', 'rb')

    classifier = pickle.load(c)

    c.close()

    def __init__(self, token, key):
        self.token = token
        self.key = key
        auth = tweepy.OAuthHandler(token, key)
        self.api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

    def prepare(self, text):
        out = ({word : True for word in text.split()})
        return out

    def classify(self, text):
        return self.classifier.classify(self.prepare(text))

    def get_statuses(self, phrase):
       return self.api.search(phrase, count=100)['statuses']

    def get_tweets(self, phrase):
        out = []
        for i in self.get_statuses(phrase):

            out.append(i['text'])
        return out

    def twitter_sentiment(self, phrase):
        out = 0
        total = 0
        for i in self.get_tweets(phrase):
            sentiment = self.classify(i)
            if sentiment == 'pos':
                out += 1
            total += 1
        return out/total

#http://finance.yahoo.com/d/quotes.csv?s=GOOG&f=ae


#sent = Sentiment(token, secret_key)

#print(sent.twitter_sentiment("donald trump"))

#EXAMPLES:
# sent = Sentiment(token, secret_key)
#
# print(sent.classify('happy'))

