import sys
from pymongo import MongoClient

db = MongoClient().school

q = {"scores.type": "homework"}
s = {"score": 1}

cursor = db.students.find(q)

count = 0
for document in cursor:
    i = 0
    min = sys.maxint
    min_i = -1
    for s in document['scores']:
        if s["type"] == "homework" and s["score"] < min:
            min = s["score"]
            min_i = i
        i += 1

    if min_i > -1:
        count += 1
        document['scores'].pop(min_i)
        db.students.save(document)

    print("Updated: %d" % count)
