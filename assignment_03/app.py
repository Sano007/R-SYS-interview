import flask

app = flask.Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
	if(flask.request.method == 'GET'):
		return flask.render_template("index.html", message=None)
	
	print(flask.request.form.to_dict())
	return flask.render_template("index.html", message='<h1>Hello World!</h1>')




if(__name__ == "__main__"):
	flask.url_for("static", filename="index.css")
	app.run(debug=True)