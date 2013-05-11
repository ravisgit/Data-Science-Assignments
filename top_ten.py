import sys
import json
import re

scores = {} # initialize an empty dictionary
hashtagsCollection =[]
hashtagsDictionary = {}
result = []

def tweet_lines(fp):
	data = fp.readlines()
	
	for i in range(len(data)):
	    try:
		cdata = json.loads(data[i])
		hashtagsCollection.append(cdata["entities"]["hashtags"])
	    except:
		pass

        for hashtags in hashtagsCollection:
	    if len(hashtags) > 0:
	       for hashtag in hashtags:
		hstext = hashtag["text"].encode('utf-8').lower()
		try: 
		  hashtagsDictionary[hstext] = hashtagsDictionary[hstext] + 1
		except:  
		  hashtagsDictionary[hstext] = 1	
	
		 		  
	result = sorted(hashtagsDictionary, key = hashtagsDictionary.get,reverse=True)[:10]  
	
	for hashtag in result:
	    print hashtag + " " + str(float(hashtagsDictionary[hashtag]))	  	

def main():
    tweet_file = open(sys.argv[1])
    tweet_lines(tweet_file)

if __name__ == '__main__':
    main()
