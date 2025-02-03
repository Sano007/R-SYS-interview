import flask

from Backend.logger import logger
from Backend import APIConnector

app = flask.Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
	if(flask.request.method == 'GET'):
		return flask.render_template("index.html", message=None)
	
	logger.info(flask.request.form.to_dict())
	
	return flask.render_template("index.html", 
		city_a=flask.request.form['city-a'],
		city_b=flask.request.form['city-b'],
	)




if(__name__ == "__main__"):
	flask.url_for("static", filename="index.css")
	app.run(debug=True)