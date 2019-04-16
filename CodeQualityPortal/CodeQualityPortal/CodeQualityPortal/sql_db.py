import mysql.connector
import datetime

def check_table():
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="password",
		database="Github_Mining"
	)
	mycursor = mydb.cursor()
	mycursor.execute("CREATE TABLE IF NOT EXISTS Url_Records(url VARCHAR(255),token Varchar(255))")
	mycursor.execute("Select url from Url_Records")
	return mycursor.fetchall()
def get_urls():
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="password",
		database="Github_Mining"
	)
	mycursor = mydb.cursor()
	mycursor.execute("CREATE TABLE IF NOT EXISTS Url_Records(url VARCHAR(255),token Varchar(255))")
	mycursor.execute("Select * from Url_Records")
	return mycursor.fetchall()

def save_url(u,tok):
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="password",
		database="Github_Mining"
	)

	mycursor = mydb.cursor()
	mycursor.execute("CREATE TABLE IF NOT EXISTS Url_Records(url VARCHAR(255),token Varchar(255))")
	sql = "INSERT INTO Url_Records(url,token) VALUES (%s,%s)"

	mycursor.execute("Select url from Url_Records")
	result = mycursor.fetchall()
#	print(type(result))
#	print("checkpoint")
	if any(u in s for s in result):
		print()
	else:
		y = (u, tok)
		mycursor.execute(sql, y)
		mydb.commit()

def mock_database_generator(class_objects,repo, major_collab, total_collab):
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="password",
	  database="Github_Mining"
	)

	time=str(datetime.datetime.now())
	mycursor = mydb.cursor()

	# mycursor.execute("CREATE DATABASE Github_Mining")
	mycursor.execute("CREATE TABLE IF NOT EXISTS File_Records (ID INT AUTO_INCREMENT PRIMARY KEY, TimeStamp  DATETIME,Repo_Name VARCHAR(255),File_Name Varchar(255), Total_Methods INT,Class_Name VARCHAR(255),Parent VARCHAR(255), Cyclomatic_Complexity INT , LOC INT, Total_Comments INT, Coupling INT)")

	mycursor.execute("CREATE TABLE IF NOT EXISTS Project_Records (ID INT AUTO_INCREMENT PRIMARY KEY, TimeStamp DATETIME, Repo_Name VARCHAR(255),Total_Collaborators INT, Major_Collaborator Varchar(255))")

	sql = "INSERT INTO File_Records (TimeStamp,Repo_Name,Total_Methods,File_Name,Class_Name,Parent,Cyclomatic_Complexity,LOC,Total_Comments,Coupling) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	for x in class_objects:
		#print(x)
		if not class_objects[x].parents:
			tup=(time,repo,class_objects[x].no_of_methods,class_objects[x].file_name,x,None,class_objects[x].cyclomatic_complexity,abs(class_objects[x].last_line-class_objects[x].first_line),class_objects[x].no_of_comments,class_objects[x].coupling)
			mycursor.execute(sql, tup)
		else:
			for par in class_objects[x].parents:
				tup=(time,repo,class_objects[x].no_of_methods,class_objects[x].file_name,x,par,class_objects[x].cyclomatic_complexity,abs(class_objects[x].last_line-class_objects[x].first_line),class_objects[x].no_of_comments,class_objects[x].coupling)
				mycursor.execute(sql,tup)
	mydb.commit()




	#sqlQuery = "WITH RECURSIVE class_path AS ( SELECT Class_Name, Child Child_Class_Name, 1 lvl FROM File_Records WHERE Child IS NULL UNION ALL SELECT f.Class_Name, f.Child, lvl+1 FROM File_Records f INNER JOIN class_path cp ON cp.Class_Name = f.Child )"
	#sqlQuery1="SELECT Class_Name,Child_Class,lvl FROM class_path cp ORDER BY lvl"

	sql1 = 'INSERT INTO Project_Records(TimeStamp,Repo_Name,Total_Collaborators,Major_Collaborator) VALUES (%s,%s,%s,%s);'
	tup1=(time,repo,total_collab,major_collab)
	mycursor.execute(sql1,tup1)
	#mycursor.execute(sqlQuery1)
	#myresult = mycursor.fetchall()
	#for x in myresult:
	#  print(x)
#	mycursor.executemany(sql1,val1)
	mydb.commit()
	sql2 = 'alter schema github_mining default collate utf8_bin;'
	mycursor.execute(sql2)
	sql3 = 'alter table github_mining.file_records CONVERT TO CHARACTER SET UTF8MB3;'
	mycursor.execute(sql3)
	sql4 = 'alter table github_mining.project_records CONVERT TO CHARACTER SET UTF8MB3;'
	mycursor.execute(sql4)