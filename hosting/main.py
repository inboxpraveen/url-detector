from flask import Flask, render_template, request
from test import main as url_detector

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def detect_url():
    if request.method == "GET":
        return (render_template("index.html"))
    
    if request.method == "POST":
        input_url = request.form["url_search"]
        if not input_url.startswith('www.'):
            input_url = 'www.' + input_url
        if not input_url.startswith('https://'):
            input_url = 'https://' + input_url
        elif not input_url.startswith('http://'):
            input_url = 'http://' + input_url
        
        output = url_detector(input_url)
        if output == 1:
            return (render_template("safe.html"))
        elif output == -1:
            return (render_template("unsafe.html"))
        else:
            return ("<h1>something went wrong</h1>")

if __name__ == "__main__":
    app.run()
