#https://realpython.com/introduction-to-mongodb-and-python/
from pymongo import MongoClient
client = MongoClient()


client = MongoClient(host="localhost", port=27017)
client = MongoClient("mongodb://localhost:27017")

db = client.rptutorials

db = client["rptutorials"]



tutorial1 = {
     "title": "Working With JSON Data in Python",
     "author": "Lucas",
     "contributors": [
         "Aldren",
         "Dan",
         "Joanna"
     ],
     "url": "https://realpython.com/python-json/"
     }

tutorial = db.tutorial


result = tutorial.insert_one(tutorial1)
print(result)


tutorial2 = {
     "title": "Python's Requests Library (Guide)",
     "author": "Alex",
     "contributors": [
         "Aldren",
         "Brad",
         "Joanna"
     ],
     "url": "https://realpython.com/python-requests/"
 }

tutorial3 = {
     "title": "Object-Oriented Programming (OOP) in Python 3",
     "author": "David",
     "contributors": [
         "Aldren",
         "Joanna",
         "Jacob"
     ],
     "url": "https://realpython.com/python3-object-oriented-programming/"
 }

new_result = tutorial.insert_many([tutorial2, tutorial3])



print(f"Multiple tutorials: {new_result.inserted_ids}")
print("-----------CLOSED--------------")

print("pprint")
import pprint
print("-----------CLOSED--------------")
for doc in tutorial.find():
    pprint.pprint(doc)



import pprint

jon_tutorial = tutorial.find_one({"author": "Jon"})

pprint.pprint(jon_tutorial)

client.close()



import pprint
from pymongo import MongoClient

with MongoClient() as client:
    db = client.rptutorials
    for doc in db.tutorial.find():
        pprint.pprint(doc)




from mongoengine import connect
connect(db="rptutorials", host="localhost", port=27017)



from mongoengine import Document, ListField, StringField, URLField
print("-----------CLOSED--------------")
class Tutorial(Document):
     title = StringField(required=True, max_length=70)
     author = StringField(required=True, max_length=20)
     contributors = ListField(StringField(max_length=20))
     url = URLField(required=True)





tutorial1 = Tutorial(
title="Beautiful Soup: Build a Web Scraper With Python",
author="Martin",
contributors=["Aldren", "Geir Arne", "Jaya", "Joanna", "Mike"],
url="https://realpython.com/beautiful-soup-web-scraper-python/"
)

tutorial1.save()  # Insert the new tutorial


tutorial2 = Tutorial()
tutorial2.author = "Alex"
tutorial2.contributors = ["Aldren", "Jon", "Joanna"]
tutorial2.url = "https://realpython.com/convert-python-string-to-int/"
tutorial2.save()

print("-----------CLOSED--------------")
for doc in Tutorial.objects:
     print(doc.title)



for doc in Tutorial.objects(author="Alex"):
    print(doc.title)