import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    #for field in record:
      mr.emit_intermediate(record[1], record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    orders = []
    list_items = []
    for v in list_of_values:
      if v[0] == "order":
          orders.append(v)
      else:
          list_items.append(v)

    for v in list_items:
        mr.emit((orders[0]+ v))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
