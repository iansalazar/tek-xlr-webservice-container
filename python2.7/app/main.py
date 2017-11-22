from flask import Flask
import json

app = Flask(__name__)

@app.route("/epicstatus")
def epicstatus():
    dict = {'green': 8, 'red': 1}
    json_str = json.dumps(dict)
    return json_str

@app.route("/storystatus")
def storystatus():
    dict = {'green': 58, 'red': 1}
    json_str = json.dumps(dict)
    return json_str

@app.route("/defectstatus")
def defectstatus():
    dict = {'closed': 2, 'open': 1}
    json_str = json.dumps(dict)
    return json_str

@app.route("/featurestatus")
def featurestatus():
    dict = {'green': 19, 'red': 1}
    json_str = json.dumps(dict)
    return json_str

@app.route("/securitystatus")
def securitystatus():
    dict = {'issues': 1, 'critical': 0}
    json_str = json.dumps(dict)
    return json_str

@app.route("/testcasestatus")
def testcasestatus():
    dict = {'passed': 53, 'failed': 1}
    json_str = json.dumps(dict)
    return json_str

@app.route("/")
def hello():
    return "Hello from the TEK XLR Web service...."

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
