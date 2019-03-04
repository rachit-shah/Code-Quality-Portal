import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["SoftwareEngineeringProject"]
file_db = mydb["File Database"]
project_db = mydb["Project Database"]

file_dict = [
{ "ID":"1001", "TimeStamp":100, "ClassName":"Bank Account", "NumberOfMethods":10,"FileName":"Account","Children":["Fixed","Current","Saving","Reserve"], "Coupling":5,"LinesOfCodes":200},
{ "ID":"1002", "TimeStamp":200, "ClassName":"Fixed Deposit", "NumberOfMethods":20,"FileName":"Fixed","Children":None, "Coupling":0,"LinesOfCodes":800},
{ "ID":"1003", "TimeStamp":300, "ClassName":"Current Account", "NumberOfMethods":15,"FileName":"Current","Children":None, "Coupling":0,"LinesOfCodes":1000},
{ "ID":"1004", "TimeStamp":400, "ClassName":"Saving Account", "NumberOfMethods":20,"FileName":"Saving","Children":None, "Coupling":1,"LinesOfCodes":500},
{ "ID":"1005", "TimeStamp":500, "ClassName":"Reserve Account", "NumberOfMethods":12,"FileName":"Reserve","Children":None, "Coupling":6,"LinesOfCodes":40000},
{ "ID":"1006", "TimeStamp":600, "ClassName":"Animals", "NumberOfMethods":7,"FileName":"Animals","Children":["Mammals","Verteberates","Insects","Reptiles"], "Coupling":3,"LinesOfCodes":100},
{ "ID":"1007", "TimeStamp":700, "ClassName":"Mammals", "NumberOfMethods":15,"FileName":"Mammals","Children":None, "Coupling":2,"LinesOfCodes":1200},
{ "ID":"1008", "TimeStamp":800, "ClassName":"Verteberates", "NumberOfMethods":10,"FileName":"Verteberates","Children":None, "Coupling":2,"LinesOfCodes":900},
{ "ID":"1009", "TimeStamp":900, "ClassName":"Insects", "NumberOfMethods":8,"FileName":"Insects","Children":None, "Coupling":3,"LinesOfCodes":500},
{ "ID":"1010", "TimeStamp":1000, "ClassName":"Reptiles", "NumberOfMethods":9,"FileName":"Reptiles","Children":None, "Coupling":1,"LinesOfCodes":400},
]

project_dict = [
{"ID":"101","Time Stamp":100,"Cyclomatic Complexity":15,"Fault Detection Per Test":4},
{"ID":"102","Time Stamp":200,"Cyclomatic Complexity":14,"Fault Detection Per Test":4},
{"ID":"103","Time Stamp":300,"Cyclomatic Complexity":14,"Fault Detection Per Test":2},
{"ID":"104","Time Stamp":400,"Cyclomatic Complexity":14,"Fault Detection Per Test":0},
{"ID":"105","Time Stamp":500,"Cyclomatic Complexity":13,"Fault Detection Per Test":0},
]

x = file_db.delete_many({})
x=file_db.insert_many(file_dict)
print(x)

y = file_db.find_one()
print(type(y))
print(y)

x = project_db.delete_many({})
x=project_db.insert_many(project_dict)
print(x)

y = project_db.find_one()
print(type(y))
print(y)