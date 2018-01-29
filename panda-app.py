from flask import Flask, render_template, request
import csv
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hola panda"

@app.route("/median")
def median():
	return render_template("median.html")

@app.route("/computeMedian", methods=['POST'])
def computeMedian():
	file = request.files['data_file']
	if not file:
		return "No file"

	content = file.stream.read().decode("utf-8") # un monton de bytes en formato UTF-8
	entriesAsString = str(content).split(',') # convertir bytes a primitivo string
	entriesAsInt = [int(entry) for entry in entriesAsString] # cambiar entradas a primitivo int

	average = sum(entriesAsInt)/len(entriesAsInt) #calcular promedio
	average = str(average) # convertir promedio a string

	return render_template("resultado.html", average=average)


if __name__ == "__main__":
    app.run(port=9000)