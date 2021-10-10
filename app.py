# import sys

import mysql.connector as mysql
from flask import Flask, render_template, request, jsonify,send_file
import file
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

@app.route('/admin')
def admin():
	output1 = file.df
	output2 = file.df1
	return render_template('adminpage.html', output1=output1, output2=output2)


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

		return 'OK sudess', 200






	# GET request
	else :

		message = {'greeting': 'Hello from Flask!'}
		return jsonify(message)  # serialize and use JSON headers






if __name__ == '__main__':
	# run!
	app.run(debug=True)