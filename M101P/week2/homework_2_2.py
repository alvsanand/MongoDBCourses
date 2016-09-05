from pymongo import MongoClient
from bson.son import SON

db = MongoClient().students

pipeline = [
    {"$match": { "type": "homework"}},
    {"$group": {"_id": "$student_id", "worst_score": {"$min": "$score"}}},
    {"$unwind": "$worst_score"},
]

cursor = db.grades.aggregate(pipeline)

count = 0
for document in cursor:
    db.grades.delete_one({ "type": "homework", "student_id": document['_id'], "score": document['worst_score']})

    count = count + 1

print("Deleted: %d"%count)