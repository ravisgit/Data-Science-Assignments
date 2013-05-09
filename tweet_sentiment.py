import sys
import json

scores = {} # initialize an empty dictionary
tweets =[]


def sent_lines(fp):
    sentiments = ""
    for line in fp:
	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	scores[term] = int(score)  # Convert the score to an integer.

def tweet_lines(fp):
	data = fp.readlines()
	
	for i in range(len(data)):
	    try:
		cdata = json.loads(data[i])
		if cdata["user"]["lang"] == "en":
			tweets.append(cdata["text"])	
	    except:
		pass


	for line in tweets:
	    tweetscore = 0
	    for word in line.split():
	        tweetscore = tweetscore + scores.get(word,0)
	    print tweetscore 

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_lines(sent_file)
    tweet_lines(tweet_file)

if __name__ == '__main__':
    main()
