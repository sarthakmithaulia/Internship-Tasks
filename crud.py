import pymongo
#create from crud operations
if __name__ == "__main__":
    print("create first doc")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    database= client["task1"]
    collection= database["collection of my tasks"]
    dictionary={"name":"sarthak","age":20}
    dictionary={"name":"piyush","age":21}
    collection.insert_one(dictionary)
    
#read from crud operations
find= collection.find_one({"name":"piyush"})
print(find)

find1= collection.find()
for item in find1:
    print(item)
    
#update from crud operations
prev={"name":"piyush"}
next1={"$set":{"age":24}}
collection.update_one(prev,next1)

#delete from crud operations
rec={"name":"piyush"}
collection.delete_one(rec)