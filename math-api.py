from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
import heapq
import json
import math

app = Flask(__name__)
app.run(debug=True)
CORS(app)

@app.route("/", methods=['GET'])

def index():
    return "Welcome to CodezUp"


@app.route("/min", methods=['POST'])

def getMin():
	#data = request.form.get('value')
	data = request.get_json()
	if not "value" in data.keys():
		return jsonify(status="error", message="Please provide value key which contains list of numbers"), 400
	newlist = data['value'].split(",")
	if not "quantifier" in data.keys():
		return jsonify(status="error", message="Please provide quantifier key which contains a numbers"), 400
	quantifier = int(data['quantifier'])
	data2 = []
	for j in newlist:
		data2.append(int(j))
	data2.sort()
	result = []
	if quantifier > len(data2):
		return jsonify(status="success", minimum=data2), 200	
	for i in range(0, quantifier):
		result.append(data2[i])
	return jsonify(status="success", minimum=result), 200

@app.route("/max", methods=['POST'])

def getMax():
	#data = request.form.get('value')
	data = request.get_json()
	if not "value" in data.keys():
		return jsonify(status="error", message="Please provide value key which contains list of numbers"), 400
	newlist = data['value'].split(",")
	if not "quantifier" in data.keys():
		return jsonify(status="error", message="Please provide quantifier key which contains a numbers"), 400
	quantifier = int(data['quantifier'])
	data2 = []
	for j in newlist:
		data2.append(int(j))
	data2.sort(reverse=True)
	result = []
	if quantifier > len(data2):
		return jsonify(status="success", minimum=data2), 200	
	for i in range(0, quantifier):
		result.append(data2[i])
	return jsonify(status="success", minimum=result), 200

@app.route("/avg", methods=["POST"])
def getAvg():
	data = request.get_json()
	if not "value" in data.keys():
	    return jsonify(status="error", message="Please provide value key which contains list of numbers"), 400
	values = data["value"].split(",")
	data2 = []
	for j in values:
		data2.append(int(j))
	return jsonify(status="success", average=sum(data2)/len(data2)), 200

@app.route("/median", methods=["POST"])
def getMedian():
	data = request.get_json()
	if not "value" in data.keys():
	    return jsonify(status="error", message="Please provide value key which contains list of numbers"), 400
	values = data["value"].split(",")

	data2 = []
	for j in values:
		data2.append(int(j))
	values = sorted(data2)
	median = 0

	if len(values) % 2 == 0:
		midValue = values[len(values)//2]
		midValueBefore = values[len(values)//2 + 1]
		median = (midValue + midValueBefore)/2
	else:
		median = values[len(values)//2]
	return jsonify(status="success", median=median), 200

if __name__ == "__main__":
        app.run()
