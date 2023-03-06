from flask import Flask, render_template, request, flash, jsonify
app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

import requests, json, time, sys, os
url = "https://plicpad.herokuapp.com/notepad/xxxxx371"
response = requests.request("GET", url)
result = json.loads(response.text)
lixt = "Test"
lixt2 = "Test2"


import requests, sys
#from pprint import pprint
from bs4 import BeautifulSoup
import lxml, cchardet
#from lxml import etree

my_file = open("TandCountries.txt", "r"); data = my_file.read()
URLlinks = data.split("\n"); del URLlinks[-1]; 
# print(URLlinks); print(len(URLlinks)); print()
my_file.close() #----------------------------------------------------------------

print("{:<15} {:>6}".format("Country:", "Members:".ljust(10)))
print("- "*12)
session_object = requests.Session()
def TandemExtract(url):

	#response = requests.get(url)
	response = session_object.get(url)

	#---Using Soup---
	soup = BeautifulSoup(response.text, "lxml")
	NumberOfPeople = soup.select_one("#section_46gXRGW58g1s3kbJtvHTIG > div > div > div > div > h4").text #CssSelector
	NameCountry = soup.select_one("#section_46gXRGW58g1s3kbJtvHTIG > div > div > div > div > p:nth-child(3)").text
	#---Using Soup---

	#---Using regex---
	import re
	match = re.search(r"<p>Find more than</p><h4>(.*?)</h4><p>(.*?)</p>", response.text) 
	#---Using regex---

	#print()
	if NumberOfPeople != None:
	    return ("{:<14} {:>6}".format(NameCountry[19:], NumberOfPeople.ljust(10)))

	    #print(f"{match[2][19:]} MatchRegex :", match[1])
	else:
	    print("Element not found")

	#print(soup.prettify())

#Multi processin was here:
lixt = []
for link in URLlinks:
	result = TandemExtract(link)
	lixt.append(result)

print(lixt)




@app.route("/hello")
def index():
	flash("what's your name?")
	return render_template("index.html", lixt=lixt, lixt2=lixt2)

@app.route("/hello2")
def index2():
	flash("what's your name?")
	return render_template("index2.html", lixt=lixt, lixt2=lixt2)

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html", lixt=lixt, lixt2=lixt2)

@app.route("/update_lixt")
def update_lixt():
    response = requests.request("GET", url)
    result = json.loads(response.text)
    lixt = result['notes'][0]['note']
    lixt2 = result['notes'][1]['note']
    return jsonify(lixt=lixt, lixt2=lixt2)


if __name__ == '__main__':
    app.run()
