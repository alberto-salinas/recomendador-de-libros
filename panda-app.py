from flask import Flask, render_template, request, session, redirect, url_for
import json
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

BOOK_RATINGS = 'data.json'

data = json.load(open(BOOK_RATINGS))

class Book:
	def __init__(self, name, rating):
		self.name = name
		self.rating = rating

@app.route("/", methods=["GET", "POST"])
def hello():

	if session.get("logged_in"):
		return redirect(url_for("userBookView"))

	error = None
	if request.method == "POST":
		name = str(request.form["username"])
		if name not in data:
			error = 'Could not find user'
			return render_template("login.html", error=error)
		else:
			session['logged_in'] = True
			session['currentUser'] = name
			return redirect(url_for("userBookView"))

	return render_template("login.html", error=error)

@app.route("/userBooks")
def userBookView():

	if not session.get("logged_in"):
		print "testing"
		return redirect(url_for("hello"))
	print "reneder my books"
	books = getUserBooks(session.get("currentUser"))
	return render_template("userBooks.html", 
		books=books)

def getUserBooks(name):
	readList = data[name]
	books = []
	for book in readList:
		entry = Book(book, str(data[name][book]))
		books.append(entry)

	return books

if __name__ == "__main__":
    app.run(port=9000)