# import sys

import mysql.connector as mysql
from flask import Flask, render_template, request, jsonify,send_file
import file
import  pandas as pd

import openpyxl
# from flask_mysqldb import MySQL
# import random, json
# from getpass import getpass
# from mysql.connector import connect, Error


app = Flask(__name__)

db = mysql.connect(
		host="localhost",
		user="root",
		passwd="1234",
		database="testingdb"
	)

cursor = db.cursor()

@app.route('/')
def index():
	# serve index template #
	return render_template('FrontPage.html')

@app.route('/preview')
def preview():
	# serve index template
	return render_template('preview.html')



@app.route('/download')
def download_file1():
	path1 = "t1-Financial Statement Analysis - Manaswee SamalList.csv"

	return send_file(path1, as_attachment=True)


@app.route('/download')
def download_file2():
	path2 = "t1-IT Consulting - Sriram RajagopalanList.csv"
	return send_file(path2, as_attachment=True)


@app.route('/submit', methods = ['POST','GET'])
def worker():
	if request.method == 'POST':
		print('Incoming..')
		print(request.get_json())# parse as JSON
		datas=request.get_json()
		s_id=request.json['id']
		s_name = request.json['name']
		course1 = request.json['course1']
		course2 = request.json['course2']
		course3 = request.json['course3']
		course4 = request.json['course4']
		course5 = request.json['course5']
		course6 = request.json['course6']
		course7 = request.json['course7']
		course8 = request.json['course8']
		course9 = request.json['course9']
		course10 = request.json['course10']
		course11 = request.json['course11']
		course12 = request.json['course12']
		course13 = request.json['course13']
		course14 = request.json['course14']
		course15 = request.json['course15']
		course16 = request.json['course16']
		course17 = request.json['course17']
		course18 = request.json['course18']
		course19 = request.json['course19']
		course20 = request.json['course20']

		query = """INSERT INTO course
				(id,name,course1,course2,course3,course4,course5,course6,course7,course8,course9,course10,course11,course12,course13,course14,course15,course16,course17,course18,course19,course20)
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
		values = (s_id, s_name, course1, course2, course3, course4, course5, course6, course7, course8, course9, course10, course11 , course12, course13, course14, course15, course16, course17, course18, course19, course20)

		print(datas)

		cursor.execute(query, values)

		db.commit()

		print(cursor.rowcount, "record inserted")

		query = "SELECT * FROM course"

		cursor.execute("SELECT * FROM course")
		results = cursor.fetchall()
		print(results)
		dresult_dataFrame = pd.read_sql(query, db)
		print(dresult_dataFrame)

		f1 = dresult_dataFrame.to_csv("course.csv", index=False)
		db.close()
		f = pd.read_csv('course.csv', header=None)
		f.columns = ['Regno', 'Name', 'sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'sub6', 'sub7', 'sub8', 'sub9', 'sub10',
					 'sub11',
					 'sub12', 'sub13', 'sub14', 'sub15', 'sub16', 'sub17', 'sub18', 'sub19', 'sub20']

		f.drop_duplicates(subset="Regno", keep='first', inplace=True)

		d = f.sort_values(by=['sub1', 'sub2', 'sub3'], ascending=True)
		SUBJECTList = ['t1-Financial Statement Analysis - Manaswee Samal', 't1-IT Consulting - Sriram Rajagopalan']
		for SUBJECTName in SUBJECTList:
			f1 = d[(d['sub1'] == SUBJECTName) | (d['sub2'] == SUBJECTName) | (d['sub3'] == SUBJECTName) | (
					d['sub4'] == SUBJECTName) |
				   (d['sub5'] == SUBJECTName) | (d['sub6'] == SUBJECTName) | (d['sub7'] == SUBJECTName) | (
						   d['sub8'] == SUBJECTName) | (d['sub9'] == SUBJECTName) |
				   (d['sub10'] == SUBJECTName) | (d['sub11'] == SUBJECTName) | (d['sub12'] == SUBJECTName) | (
						   d['sub13'] == SUBJECTName) | (d['sub14'] == SUBJECTName) |
				   (d['sub15'] == SUBJECTName) | (d['sub16'] == SUBJECTName) | (d['sub17'] == SUBJECTName) | (
						   d['sub18'] == SUBJECTName) | (d['sub19'] == SUBJECTName) |
				   (d['sub20'] == SUBJECTName)]

			f1.index.name = SUBJECTName
			f2 = f1.filter(['Name'])

			for i in range(len(SUBJECTList)):
				if SUBJECTList[i] == SUBJECTName:
					f2.to_csv(SUBJECTName + '.csv', encoding='utf-8', index=False)
					f4 = pd.read_csv(SUBJECTName + '.csv')
					f4 = f2.rename(columns={'Name': SUBJECTName}, inplace=False)
					f4.to_csv(SUBJECTName + 'List.csv', encoding='utf-8', index=False)
		l1 = pd.read_csv(SUBJECTList[0] + 'List.csv')
		l2 = pd.read_csv(SUBJECTList[1] + 'List.csv')

		global df
		global df1

		df = len(l1.index)
		df1 = len(l2.index)

		return 'OK sudess', 200

	# GET request
	else :

		message = {'greeting': 'Hello from Flask!'}
		return jsonify(message)  # serialize and use JSON headers


@app.route('/admin')
def admin():



	f = pd.read_csv('course.csv', header=None)
	f.columns = ['Regno', 'Name', 'sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'sub6', 'sub7', 'sub8', 'sub9', 'sub10',
				 'sub11',
				 'sub12', 'sub13', 'sub14', 'sub15', 'sub16', 'sub17', 'sub18', 'sub19', 'sub20']

	f.drop_duplicates(subset="Regno", keep='first', inplace=True)

	d = f.sort_values(by=['sub1', 'sub2', 'sub3'], ascending=True)
	SUBJECTList = ['t1-Financial Statement Analysis - Manaswee Samal', 't1-IT Consulting - Sriram Rajagopalan']
	for SUBJECTName in SUBJECTList:
		f1 = d[(d['sub1'] == SUBJECTName) | (d['sub2'] == SUBJECTName) | (d['sub3'] == SUBJECTName) | (
				d['sub4'] == SUBJECTName) |
			   (d['sub5'] == SUBJECTName) | (d['sub6'] == SUBJECTName) | (d['sub7'] == SUBJECTName) | (
					   d['sub8'] == SUBJECTName) | (d['sub9'] == SUBJECTName) |
			   (d['sub10'] == SUBJECTName) | (d['sub11'] == SUBJECTName) | (d['sub12'] == SUBJECTName) | (
					   d['sub13'] == SUBJECTName) | (d['sub14'] == SUBJECTName) |
			   (d['sub15'] == SUBJECTName) | (d['sub16'] == SUBJECTName) | (d['sub17'] == SUBJECTName) | (
					   d['sub18'] == SUBJECTName) | (d['sub19'] == SUBJECTName) |
			   (d['sub20'] == SUBJECTName)]

		f1.index.name = SUBJECTName
		f2 = f1.filter(['Name'])

		for i in range(len(SUBJECTList)):
			if SUBJECTList[i] == SUBJECTName:
				f2.to_csv(SUBJECTName + '.csv', encoding='utf-8', index=False)
				f4 = pd.read_csv(SUBJECTName + '.csv')
				f4 = f2.rename(columns={'Name': SUBJECTName}, inplace=False)
				f4.to_csv(SUBJECTName + 'List.csv', encoding='utf-8', index=False)
	l1 = pd.read_csv(SUBJECTList[0] + 'List.csv')
	l2 = pd.read_csv(SUBJECTList[1] + 'List.csv')

	global df
	global df1

	df = len(l1.index)
	df1 = len(l2.index)

	output1 = df
	output2 = df1

	return render_template('adminpage.html', output1=output1, output2=output2)




if __name__ == '__main__':
	# run!
	app.run(debug=True)