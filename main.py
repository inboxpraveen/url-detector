import flask

app = flask.Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    # if flask.render.method == "GET":
    return (flask.render_template("index.html"))

if __name__ == "__main__":
    app.run()
