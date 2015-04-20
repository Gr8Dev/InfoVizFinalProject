#!/usr/bin/python

import requests, json, csv

def getGenders(name):
	url = ""
	cnt = 0
	url = "name[0]=" + name
		

	req = requests.get("http://api.genderize.io?" + url)
	result = json.loads(req.text)
	#print(result)
	
	if result["gender"] is not None:
		gen = result["gender"]
	else:
		gen = "None"


	return gen


with open('cleanedupFan4.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	fieldnames = ['NAME', 'Gender']
	writer = csv.DictWriter((open('fan_gender_I.csv', 'w')), fieldnames)
	writer.writeheader()
	for row in reader:
		name = row['NAME']
		#print(name)
		tokens = name.split(' ')
		fname = tokens[0]
		#print(fname)
		gender = getGenders(fname)
		#print(gender)
		writer.writerow({'NAME' : name, 'Gender' : gender})
