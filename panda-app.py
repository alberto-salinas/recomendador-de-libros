from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hola panda"

@app.route("/dataEntries")
def dataEntries():
	data = json.load(open("data.json"))
	return jsonify(data)


if __name__ == "__main__":
    app.run(port=9000)