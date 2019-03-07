import mysql.connector
from datetime import date, datetime, timedelta

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="Github_Mining"
)

x=str(datetime.now())
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE Github_Mining")
mycursor.execute("CREATE TABLE IF NOT EXISTS File_Records (ID INT AUTO_INCREMENT PRIMARY KEY, TimeStamp  DATETIME,Repo_Name VARCHAR(255),File_Name Varchar(255), Total_Methods INT,Class_Name VARCHAR(255),Parent VARCHAR(255), Coupling INT, LOC INT,Total_Collaborator INT,Major_Collaborator Varchar(255))")

mycursor.execute("CREATE TABLE IF NOT EXISTS Project_Records (ID INT AUTO_INCREMENT PRIMARY KEY, TimeStamp DATETIME, CyclomaticComplexity INT, FraudDetection INT)")

sql = "INSERT INTO File_Records (TimeStamp,Repo_Name,Total_Methods,File_Name,Class_Name,Parent,Coupling,LOC,Total_Collaborator,Major_Collaborator) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=[
(x,'Bank Account',10,'File1',"Account",None,5,200,5,"niks"),
(x,'Bank Account',20,'File1',"Fixed",'Account',0,800,8,"niks"),
(x,'Bank Account',15,'File1',"Current",'Account',0,1000,6,"louis"),
(x,'Bank Account',20,'File1',"Saving",'Account',1,500,4,"faz"),
(x,'Bank Account',12,'File1',"Reserve",'Account',6,2000,3,'rish'),
(x,'Animals',7,'File2',"Animal Groups",None,3,100,2,'manp'),
(x,'Animals',12,'File2',"Mammals","Animal Groups",2,300,1,'prak'),
(x,'Animals',10,'File2',"Verteberates","Animal Groups",2,400,1,'rsha'),
(x,'Animals',9,'File2',"Insects","Animal Groups",2,450,2,'prak'),
(x,'Animals',15,'File2',"Reptiles","Animal Groups",2,350,1,'prak')
]
mycursor.executemany(sql, val)
mydb.commit()
#sqlQuery = "WITH RECURSIVE class_path AS ( SELECT Class_Name, Child Child_Class_Name, 1 lvl FROM File_Records WHERE Child IS NULL UNION ALL SELECT f.Class_Name, f.Child, lvl+1 FROM File_Records f INNER JOIN class_path cp ON cp.Class_Name = f.Child )"
#sqlQuery1="SELECT Class_Name,Child_Class,lvl FROM class_path cp ORDER BY lvl"

sql1 = 'INSERT INTO Project_Records(TimeStamp,CyclomaticComplexity,FraudDetection) VALUES (%s,%s,%s);'
val1=[
(x,15,4),
(x,14,4),
(x,14,2),
(x,14,0),
(x,13,0)
]
#mycursor.execute(sqlQuery)
#mycursor.execute(sqlQuery1)
#myresult = mycursor.fetchall()
#for x in myresult:
#  print(x)
mycursor.executemany(sql1,val1)
mydb.commit()