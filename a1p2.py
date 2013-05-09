import sys
import json

afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
sentiments = ""
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.


#----retrieving tweets--------------

data = open("output.json").readlines()
tweets =[]


for i in range(len(data)):
    try:
	cdata = json.loads(data[i])
	if cdata["user"]["lang"] == "en":
		tweets.append(cdata["text"])		
    except:
	pass

#------end of retrieving tweets----------


for line in tweets:
	tweetscore = 0
	for word in line.split():
		tweetscore = tweetscore + scores.get(word,0)
	print tweetscore 

