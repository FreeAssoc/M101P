import pymongo
import sys

# establish a connection to the db (NOTE Connection class has been deprecated in driver)
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.school
scores = db.scores

def find():
  print "find, reporting for duty"

  query = { 'type' : 'exam' }

  try:
    cursor = scores.find(query)
  except:
    print "Unexpected error:", sys.exc_info()[0]

  sanity = 0
  for doc in cursor
    print doc
    sanity += 1
    if (sanity > 10):



def find_one():

  print "find_one, reporting for duty"
  query = {'student_id':10}

  try:
    doc = scores.find_one(query)
  except:
    print("Unexpected error:", sys.exc_info()[0]

  print doc
