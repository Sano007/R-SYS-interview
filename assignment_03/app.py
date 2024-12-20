import flask

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return flask.render_template("index.html")


if(__name__ == "__main__"):
    flask.url_for("static", filename="index.css")
    app.run(debug=True)