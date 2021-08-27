
from flask import Flask, render_template
from flask import request
from flask_cors import CORS, cross_origin
# import pandas as pd

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=["GET"])
def main():
    return render_template('index.html')

@app.route("/saveData", methods=["POST"])
@cross_origin()
def saveData():
	form = request.form
	factvalue = form["factvalue"]
	elt = form["elt"]
	company = form["company"]
	finstat = form["finstat"]

	# data4 = form["factvalue"]
	print('company name',factvalue)
	print(elt)
	print(company) 
	# print("data[1]")
	# print(data[1])
	return "Data Collected Successfuly !!"

#rendering the HTML page which has the button
# @app.route('/json')
# def json():
#     return render_template('json.html')

#background process happening without any refreshing
# @app.route('/background_process_test')
# def background_process_test():
#     print ("Hello")
#     return ("nothing")
# request is a part of Flask's HTTP requests
# from flask import request
# import csv

# # methods is an array that's used in Flask which requests' methods are
# # allowed to be performed in this route.
# @app.route('/save-comment', methods=['POST'])
# def save_comment():
#     # This is to make sure the HTTP method is POST and not any other
#     if request.method == 'POST':
#         # request.form is a dictionary that contains the form sent through
#         # the HTTP request. This work by getting the name="xxx" attribute of
#         # the html form field. So, if you want to get the name, your input
#         # should be something like this: <input type="text" name="name" />.
#         finstat = request.form['finstat']
#         elt = request.form['elt']

#         # This array is the fields your csv file has and in the following code
#         # you'll see how it will be used. Change it to your actual csv's fields.
#         fieldnames = ['finstat', 'elt']

#         # We repeat the same step as the reading, but with "w" to indicate
#         # the file is going to be written.
#         with open('nameList.csv','w') as inFile:
#             # DictWriter will help you write the file easily by treating the
#             # csv as a python's class and will allow you to work with
#             # dictionaries instead of having to add the csv manually.
#             writer = csv.DictWriter(inFile, fieldnames=fieldnames)

#             # writerow() will write a row in your csv file
#             writer.writerow({'finstat': finstat, 'elt': elt})

#         # And you return a text or a template, but if you don't return anything
#         # this code will never work.
#         return 'Thanks for your input!'
  
if __name__ == "__main__":
  app.debug = True
  app.run()