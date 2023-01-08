from flask import Flask, render_template, request
from test import main as url_detector

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def detect_url():
    if request.method == "GET":
        return (render_template("index.html"))
    
    if request.method == "POST":
        output = url_detector(request.form["url_search"])
        if output == 1:
            return (render_template("safe.html"))
        elif output == -1:
            return (render_template("unsafe.html"))
        else:
            return ("<h1>something went wrong</h1>")

if __name__ == "__main__":
    app.run()
