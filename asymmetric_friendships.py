import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()
mapper_result = {}
# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    mapper_result.setdefault(record[0],[])
    mapper_result[record[0]].append(record[1])  
    mr.emit_intermediate(record[0], record[1])

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    for friend in list_of_values:
        friend_list = mapper_result.get(friend,None)
        if friend_list == None or key not in friend_list:
          mr.emit((key, friend))  
          mr.emit((friend, key))
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
