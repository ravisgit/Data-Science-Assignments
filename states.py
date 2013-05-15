import sys
import json

def states(state_file):
    statesInfo = state_file.read()	
    print statesInfo  
    result = json.loads(statesInfo)
    for state in statesInfo:
	print state["name"] 		
	  	


def main():
    sent_file = open(sys.argv[1])
    states(sent_file)

if __name__ == '__main__':
    main()
