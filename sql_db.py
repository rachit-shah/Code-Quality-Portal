import mysql.connector
from datetime import date, datetime, timedelta

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="Github_Mining"
)

x=str(datetime.now())
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE Github_Mining")
mycursor.execute("CREATE TABLE File_Records (ID INT AUTO_INCREMENT PRIMARY KEY, TimeStamp  DATETIME,Repo_Name VARCHAR(255), Total_Methods INT,File_Name VARCHAR(255),Level INT,Children VARCHAR(255), Coupling INT, LOC INT)")

mycursor.execute("CREATE TABLE Project_Records(ID INT AUTO_INCREMENT PRIMARY KEY, TimeStamp DATATIME, CyclomaticComplexity INT, FraudDetection INT)")

sql = "INSERT INTO File_Records (TimeStamp,Repo_Name,Total_Methods,File_Name,Level,Children,Coupling,LOC) VALUES (%s, %s,%d,%s,%d,%s,%d,%d)"
val=[
(x,'Bank Account',10,"Account",1,'Fixed,Current,Saving,Reserve',5,200)
(x,'Bank Account',20,"Fixed",2,'',0,800)
(x,'Bank Account',15,"Current",2,'',0,1000)
(x,'Bank Account',20,"Saving",2,'',1,500)
(x,'Bank Account',12,"Reserve",2,'',6,2000)
(x,'Animals',7,"Animal Groups",1,'Mammals,Veteberates,Insects,Reptiles',3,100)
(x,'Animals',12,"Mammals",2,'',2,300)
(x,'Animals',10,"Verteberates",2,'',2,400)
(x,'Animals',9,"Insects",2,'',4,450)
(x,'Animals',15,"Reptiles",2,'',2,350)
]
sql1 = 'INSERT INTO Project_Records(TimeStamp,CyclomaticComplexity,FraudDetection) VALUES (%s,%d,%d)'
val1=[
(x,15,4)
(x,14,4)
(x,14,2)
(x,14,0)
(x,13,0)
]
mycursor.executemany(sql, val)
mycursor.executemany(sql1,val1)
mydb.commit()