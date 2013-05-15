import sys
import json

scores =  {} # initialize an empty dictionary
tweets =[]
ustweets = {}
allwords = {}


happy_words = """
["blessed","blest","blissful","blithe","captivate","captivated",
"cheerful","cheer","chipper","chirpy","content","contented","convivial","delight","ecstatic"," elated","exultant","flying high","gay","glad","gleeful","glee","gratified","gratify","jolly","joyful","joyous","jubilant",
"laughing","laugh","haha","light","lively","looking good","merry","mirthful","cloud nine","overjoyed","overjoy","joy","peace","peaceful","peppy","perky","playful",
"pleasant","pleased","sparkling","sunny","spirit","thrilled",
"vigorous","tickle","upbeat","thrill","wonder","exuberant",
"festive","glad","jocular","joy","birth","party","booz","drink","dance","haha","lol","funny","happy"]
"""

states = """[
   {
      "name":"ALABAMA",
      "abbreviation":"AL"
   },
   {
      "name":"ALASKA",
      "abbreviation":"AK"
   },
   {
      "name":"AMERICAN SAMOA",
      "abbreviation":"AS"
   },
   {
      "name":"ARIZONA",
      "abbreviation":"AZ"
   },
   {
      "name":"ARKANSAS",
      "abbreviation":"AR"
   },
   {
      "name":"CALIFORNIA",
      "abbreviation":"CA"
   },
   {
      "name":"COLORADO",
      "abbreviation":"CO"
   },
   {
      "name":"CONNECTICUT",
      "abbreviation":"CT"
   },
   {
      "name":"DELAWARE",
      "abbreviation":"DE"
   },
   {
      "name":"DISTRICT OF COLUMBIA",
      "abbreviation":"DC"
   },
   {
      "name":"FEDERATED STATES OF MICRONESIA",
      "abbreviation":"FM"
   },
   {
      "name":"FLORIDA",
      "abbreviation":"FL"
   },
   {
      "name":"GEORGIA",
      "abbreviation":"GA"
   },
   {
      "name":"GUAM",
      "abbreviation":"GU"
   },
   {
      "name":"HAWAII",
      "abbreviation":"HI"
   },
   {
      "name":"IDAHO",
      "abbreviation":"ID"
   },
   {
      "name":"ILLINOIS",
      "abbreviation":"IL"
   },
   {
      "name":"INDIANA",
      "abbreviation":"IN"
   },
   {
      "name":"IOWA",
      "abbreviation":"IA"
   },
   {
      "name":"KANSAS",
      "abbreviation":"KS"
   },
   {
      "name":"KENTUCKY",
      "abbreviation":"KY"
   },
   {
      "name":"LOUISIANA",
      "abbreviation":"LA"
   },
   {
      "name":"MAINE",
      "abbreviation":"ME"
   },
   {
      "name":"MARSHALL ISLANDS",
      "abbreviation":"MH"
   },
   {
      "name":"MARYLAND",
      "abbreviation":"MD"
   },
   {
      "name":"MASSACHUSETTS",
      "abbreviation":"MA"
   },
   {
      "name":"MICHIGAN",
      "abbreviation":"MI"
   },
   {
      "name":"MINNESOTA",
      "abbreviation":"MN"
   },
   {
      "name":"MISSISSIPPI",
      "abbreviation":"MS"
   },
   {
      "name":"MISSOURI",
      "abbreviation":"MO"
   },
   {
      "name":"MONTANA",
      "abbreviation":"MT"
   },
   {
      "name":"NEBRASKA",
      "abbreviation":"NE"
   },
   {
      "name":"NEVADA",
      "abbreviation":"NV"
   },
   {
      "name":"NEW HAMPSHIRE",
      "abbreviation":"NH"
   },
   {
      "name":"NEW JERSEY",
      "abbreviation":"NJ"
   },
   {
      "name":"NEW MEXICO",
      "abbreviation":"NM"
   },
   {
      "name":"NEW YORK",
      "abbreviation":"NY"
   },
   {
      "name":"NORTH CAROLINA",
      "abbreviation":"NC"
   },
   {
      "name":"NORTH DAKOTA",
      "abbreviation":"ND"
   },
   {
      "name":"NORTHERN MARIANA ISLANDS",
      "abbreviation":"MP"
   },
   {
      "name":"OHIO",
      "abbreviation":"OH"
   },
   {
      "name":"OKLAHOMA",
      "abbreviation":"OK"
   },
   {
      "name":"OREGON",
      "abbreviation":"OR"
   },
   {
      "name":"PALAU",
      "abbreviation":"PW"
   },
   {
      "name":"PENNSYLVANIA",
      "abbreviation":"PA"
   },
   {
      "name":"PUERTO RICO",
      "abbreviation":"PR"
   },
   {
      "name":"RHODE ISLAND",
      "abbreviation":"RI"
   },
   {
      "name":"SOUTH CAROLINA",
      "abbreviation":"SC"
   },
   {
      "name":"SOUTH DAKOTA",
      "abbreviation":"SD"
   },
   {
      "name":"TENNESSEE",
      "abbreviation":"TN"
   },
   {
      "name":"TEXAS",
      "abbreviation":"TX"
   },
   {
      "name":"UTAH",
      "abbreviation":"UT"
   },
   {
      "name":"VERMONT",
      "abbreviation":"VT"
   },
   {
      "name":"VIRGIN ISLANDS",
      "abbreviation":"VI"
   },
   {
      "name":"VIRGINIA",
      "abbreviation":"VA"
   },
   {
      "name":"WASHINGTON",
      "abbreviation":"WA"
   },
   {
      "name":"WEST VIRGINIA",
      "abbreviation":"WV"
   },
   {
      "name":"WISCONSIN",
      "abbreviation":"WI"
   },
   {
      "name":"WYOMING",
      "abbreviation":"WY"
   }
]"""


def sent_lines(fp):
    sentiments = ""
    for line in fp:
	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	scores[term] = int(score)  # Convert the score to an integer.

def tweet_lines(fp):
	

        statesList = json.loads(states)
	happywords = json.loads(happy_words)

	data = fp.readlines()
	
	for i in range(len(data)):
	    try:
		cdata = json.loads(data[i])
		location = str(cdata["user"]["location"])
		
		for state in statesList:
		    if location.find(state["name"]) >= 0 or location.find(state["abbreviation"]) >=0:
		      try: 	
			  ustweets[state["abbreviation"]].append(cdata["text"])			     	
		      except:
			  twts = []
			  twts.append(cdata["text"])  	
			  ustweets[state["abbreviation"]] = twts	
	    except:
		pass


	for statetweet in ustweets.keys():
		for line in ustweets[statetweet]:
		    tweetscore = 0
		    for word in line.split():		
			try:				
				if scores.get(word,0) != 0:
				   if happywords.index(word) >=0: 
					   try:
					       allwords[statetweet] =  allwords[statetweet] + 1			
					   except:
					       allwords[statetweet] = 1
			except:
				pass
			

	for state in sorted(allwords, key = allwords.get,reverse=True)[:10]:
	    print state	


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_lines(sent_file)
    tweet_lines(tweet_file)

if __name__ == '__main__':
    main()
