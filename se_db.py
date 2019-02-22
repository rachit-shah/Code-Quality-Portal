import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["SoftwareEngineeringProject"]
file_db = mydb["File Database"]
project_db = mydb["Project Database"]

file_dict = {"ID":"1001", "TimeStamp":"100", "ClassName":"Parent", "NumberOfMethods":"10","FileName":"ParentFile","Children":"Child", "Coupling":"5","LinesOfCodes":"1000"}

x=file_db.insert_one(file_dict)
print(x)

y = file_db.find_one()
print(type(y))
print(y)