"""
    A simple example of accessing and writing to a MongoDB.

    Mainly followed the tutorial at:
        http://api.mongodb.org/python/current/tutorial.html
"""

# Before we start, make sure that you have the PyMongo distribution installed.
# It is also assumed that a MongoDB instance is running on the default host and
# port.
import pymongo

# The first step when working with PyMongo is to create a MongoClient to the
# running mongod instance. The below code will connect to the default host and
# port.
from pymongo import MongoClient
client = MongoClient()

# A single instance of MongoDB can support multiple independent databases.
db = client['test_database_01']

# A collection is a group of documents stored in MongoDB, and can be thought of
# as roughly the equivalent of a table in a relational database.
collection = db['test_collection_01']

# An important note abut collections (and databases) in MongoDB is that they
# are created lazily. None of the above commands have actually performed any
# operations on the MongoDB server.
#
# Let's change this, and populate our database with some data.
test = {
    'one': 1,
    'two': 2
}
test_id = collection.insert(test)

# When a document is inserted a special key, "_id", is automatically added if
# the document doesn't already contain an "_id" key. The value of the "_id"
# must be unique across the collection. insert() returns the value of the "_id"
# of the inserted document.

# After inserting the first document, the "collection" collection has actually
# been created on the server. We can verify this by listing all of the
# collections in our database.
print "We have the following collection names: {}.".format(db.collection_names())


print "After creating a test object, let us read it, and print it out."
result = collection.find_one({'_id': test_id})
print result
