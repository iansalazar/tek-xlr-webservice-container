from flask import Flask
import json

app = Flask(__name__)

@app.route("/epicstatus")
def epicstatus():
    dict = {'green': 8, 'red': 1}
    json_str = json.dumps(dict)
    return json_str

@app.route("/")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 2.7 (default)"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
