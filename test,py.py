import mysql.connector as mysql
import  pandas as pd
import openpyxl
db = mysql.connect(
		host="localhost",
		user="root",
		passwd="1234",
		database="testingdb",
		use_pure=True
	)

cursor = db.cursor()
query = "SELECT * FROM course"

cursor.execute("SELECT * FROM course")
results =cursor.fetchall()
print(results)
dresult_dataFrame = pd.read_sql(query,db)
print(dresult_dataFrame)

f1=dresult_dataFrame.to_csv("course.csv",index=False)

db.close()