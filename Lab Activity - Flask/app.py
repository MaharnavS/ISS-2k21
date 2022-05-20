#!/usr/bin/env python3
#Author: Maharnav Singhal

from flask import *

app = Flask(__name__)

@app.route('/calc/sum', methods=['POST', 'GET'])
def SUM():
	if request.method == 'GET':
		return """
		<html> 
		<body> 
			<form action = "http://localhost:5000/calc/sum" method = "post" > 
			<p> Enter 1st Number </p> 
			<p><input type = "text" name = "num1" /></p>  
			<p> Enter 2nd Number </p> 
			<p><input type = "text" name = "num2" /></p> 
			<p><input type = "submit" value="submit" /></p>
			</form> 
		</body> 
		</html>"""
	
	if request.method == 'POST':
		num1 = request.form['num1']
		num2 = request.form['num2']
		if num1.isdigit() and num2.isdigit():
			return '%s' % (int(num1) + int(num2))
		return 'Datatype error: entered values were not int'
	
@app.route('/calc/multiply', methods=['POST', 'GET'])
def MULTIPLY():
	if request.method == 'GET':
		return """
		<html> 
		<body> 
			<form action = "http://localhost:5000/calc/multiply" method = "post" > 
			<p> Enter 1st Number </p> 
			<p><input type = "text" name = "num1" /></p>  
			<p> Enter 2nd Number </p> 
			<p><input type = "text" name = "num2" /></p> 
			<p><input type = "submit" value="submit" /></p>
			</form> 
		</body> 
		</html>"""
	
	if request.method == 'POST':
		num1 = request.form['num1']
		num2 = request.form['num2']
		if num1.isdigit() and num2.isdigit():
			return '%s' % (int(num1) * int(num2))
		return 'Datatype error: entered values were not int'
	
if __name__ == '__main__':
	app.run(debug=True)