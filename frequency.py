import sys
import json
import re

scores = {} # initialize an empty dictionary
tweets =[]
allwordscores =[]
tweetsdict = {}
tweetwordcount = {}
'''
pen_ult_result = {}
final_result={}
'''

def sent_lines(fp):
    sentiments = ""
    for line in fp:
	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	scores[term] = int(score)  # Convert the score to an integer.

def tweet_lines(fp):
	data = fp.readlines()
	alltweetcount = 0
	
	for i in range(len(data)):
	    try:
		cdata = json.loads(data[i])
		tweets.append(cdata["text"])
	    except:
		pass


	for line in tweets:
	    words = []	
	    tweetscore = 0
	    for word in line.split():
		words.append(word)
	        tweetscore = tweetscore + scores.get(word,0)
	   # print tweetscore 
	    tweet_score(words,tweetscore)

	for word in tweetwordcount.keys():
	    alltweetcount = alltweetcount + int(tweetwordcount[word]) 		

	#print str(alltweetcount)	

	for word in tweetwordcount.keys():
	   # print str(int(tweetwordcount[word]))	
	    print word + " "+ str(float(int(tweetwordcount[word])/alltweetcount))	
'''
	for word in tweetsdict.keys():
	    # print word + ":" + str(tweetsdict[word]/tweetwordcount[word])
	     pen_ult_result[word] = float(tweetsdict[word]/tweetwordcount[word])	
	
	for word in pen_ult_result.keys():
	    try:
		scores[word] = scores[word]
	    except:
		final_result[word] = pen_ult_result[word]
 	     
	for word in final_result.keys():
	    print word + " " + str(round(final_result[word],3))
'''

def tweet_score(tweetwords,score):
	for word in tweetwords:
	    wrd = word.encode('utf-8').lower() 	
	    if not re.match('.*[^a-z].*',wrd):	
	       #allwordscores.append(wrd + ":" + str(score))
	       if wrd in tweetsdict:		
	       	  tweetsdict[wrd] = tweetsdict[wrd] + score
		  tweetwordcount[wrd] = tweetwordcount[wrd] + 1		
	       else:
		  tweetsdict[wrd] =  score			
		  tweetwordcount[wrd] = 1
	   	

def main():
   # sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
   # sent_lines(sent_file)
    tweet_lines(tweet_file)

if __name__ == '__main__':
    main()
