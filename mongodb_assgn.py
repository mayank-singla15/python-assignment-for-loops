'''Q1. What is MongoDB? Explain non-relational databases in short. In which scenarios it is preferred to use
MongoDB over SQL databases?

MongoDB is a NoSQL, document-oriented database used for storing high volumes of data. It stores data in JSON-like documents (called BSON – Binary JSON), which allows for flexible and dynamic schemas.

-Non-relational databases (or NoSQL databases) do not use traditional table-based relational schemas.
-They are best for scaling horizontally and handling unstructured or semi-structured data.

'''

''''Q2. State and Explain the features of MongoDB.Also,Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.

✅ 1. Document-Oriented Storage
MongoDB stores data in BSON format (Binary JSON) — flexible and schema-less.
No fixed schema — you can add/remove fields anytime.

Each document is like a row, and each collection is like a table.

✅ 2. Schema-less (Flexible Schema)
You can store different fields in different documents of the same collection.

✅ 3. Powerful Query Language
MongoDB supports rich queries using JSON-like syntax.

✅ 4. Indexing for Fast Performance
Indexes improve query speed.

✅ 5. Horizontal Scalability (Sharding)
MongoDB supports horizontal scaling by distributing data across multiple servers (shards).

✅ 6. Aggregation Framework
Used for advanced data processing like group, filter, project, etc.

✅ 7. High Availability with Replication
Replication ensures data redundancy and automatic failover.

✅ 8. Integration with Multiple Languages
MongoDB has drivers for Python, JavaScript, Java, C#, etc.

✅ 9. Map-Reduce Support (Advanced)
Used for custom aggregation and processing large volumes of data.

'''

from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus

# Encode the username and password
username = quote_plus("mayanksingla1506")
password = quote_plus("Singlaji@1")

# Properly formatted URI using f-string
uri = f"mongodb+srv://{username}:{password}@cluster0.nkblt1x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Test the connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db= client['mydb']
collection = db['users']

collection.drop()

# 2. INSERT DOCUMENTS (Schema-less, BSON format)
users = [
      {"name": "Mayank", "age": 22, "skills": ["Python", "Flask", "MongoDB"], "isAvailable": True},
    {"name": "Alice", "role": "Developer"},
    {"name": "Bob", "city": "New York", "age": 30},
    {"name": "Charlie", "age": 25, "skills": ["React", "Node"], "isAvailable": False}

]


collection.insert_many(users)
print('\n  Inserted Documents')

# 3. QUERYING (Find documents with conditions)
print('/n  Users aged above 20:')
for user in collection.find({'age':{'$gt':20}}):
    print(user)


print('\n Users with Flask in skils' )
 for user in collecion.find({"skills":"Flask" }):
    print(user)

# 4. INDEXING (Create index on name for faster lookup)

collection.create_index([('name',1)])
print('\n Index on name created')


# 5. UPDATE DOCUMENT

collection.update_one({'name':'Alice'},{'$set':{'city':'Pune'}})
print("\n Updated Alice's city to Pune")

# 6. AGGREGATION (Group by skill and count users)

print('\n Aggregation - Count users per skill')
pipeline = [
    {'$unwind':'$skills'},
    {'$group':{'_id':'$skills','count':{'$sum':1}}}

]

for result in collection.aggregate(pipeline):
    print(result)

# 7. FIND ALL DOCUMENTS (Final collection)

print('\n All Documents in users collection:')
for user in collection.find():
    print(user)


'''Q4. Using the database and the collection created in question number 2, write a code to insert one record,
and insert many records. Use the find() and find_one() methods to print the inserted record.'''

collection.drop()

one_user = {
    'name':'John Doe',
    'age':28,
    'skills':['Javascript','React'],
    'isAvailable':True
}

collection.insert_one(one_user)

many_users = [
    {"name": "Emily", "age": 24, "skills": ["Python", "Django"]},
    {"name": "Raj", "age": 30, "skills": ["Java", "Spring"], "city": "Mumbai"},
    {"name": "Sophia", "age": 26, "skills": ["Flutter", "Firebase"], "isAvailable": False}
]
collection.insert_many(many_users)

print(collection.find_one())

for doc in collection.find():
    print(doc)

'''Q5. Explain how you can use the find() method to query the MongoDB database. Write a simple code to
demonstrate this.

The find() method in MongoDB is used to retrieve multiple documents that match a specified query. It returns a cursor object, which you can iterate over to access the documents.''' 


if collection.count_documents({}) == 0:
    collection.insert_many([
        {"name": "Alice", "age": 24, "city": "New York"},
        {"name": "Bob", "age": 30, "city": "San Francisco"},
        {"name": "Charlie", "age": 22, "city": "Chicago"},
        {"name": "David", "age": 28, "city": "New York"}


    ])

# 1. Find all users
print('\n   All users:')
for user in collection.find():
    print(user)

# 2. Find users from New York
print('\n Users from New York:')
for user in collection.find({'city':'New York'}):
    print(user)

# 3. Find users aged above 25
print('\n Users aged above 25:')
for user in collection.find({'age':{'$gt':25}}):
    print(user)

# 4. Find users and project only name & age

print('\n Users with only name & age(no _id):')
for user in collection.find({},{'_id':0,'name':1,'age':1}):
    print(user)   


'''Q6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB.

The sort() method in MongoDB is used to arrange the result of a query in either ascending or descending order based on one or more fields.

'''

if collection.count_documents({}) == 0:
    collection.insert_many([
        {"name": "Alice", "age": 24},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 22},
        {"name": "David", "age": 28}

    ])
# 1. Sort users by age in ASCENDING order
print('\n Users sorted by age (ascending):')
for user in collection.find().sort('age',1):
    print(user)


# 2. Sort users by age in DESCENDING order

print('\n Users sortedby age (descending)')
for user in collection.find().sort('age',-1):
    print(user)    


'''Q7. Explain why delete_one(), delete_many(), and drop() is used.

-These methods are used to remove documents or entire collections from a MongoDB database.
🔹 1. delete_one()
Deletes only the first document that matches the filter (even if multiple match).

'''  

collection.delete_one({ "name": "Alice" })

'''🔹 2. delete_many()
Deletes all documents that match the given filter condition.'''

collection.delete_many({ "city": "Delhi"})

'''🔹 3. drop()
Completely removes the entire collection from the database.'''
collection.drop()
    