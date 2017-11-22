from flask import Flask
import json

app = Flask(__name__)

@app.route("/epicstatus")
def epicstatus():
    dict = {'green': 8, 'red': 1}
    json_str = json.dumps(dict)
    return json_str

@app.route("/epicstatusdetail")
def epicstatusdetail():
    details = [{"name":"DE1","url":"http://www.google.com"},{"owner":"J. Doe","status":"Green"},{"test-start":"10/01/17","test-cases-assigned": 4,"executed": 4, "percent-compete": 100, 
                "passed": 4, "failed": 4, "defects-logged": 1, "open": 0, "resolved": 0, "closed": 1 },
               {"name":"DE2","url":"http://www.google.com"},{"owner":"J. Doe","status":"Green"},{"test-start":"10/01/17","test-cases-assigned": 9,"executed": 9, "percent-compete": 100, 
                "passed": 9, "failed": 0, "defects-logged": 0, "open": 0, "resolved": 0, "closed": 0 }
                ]
    json_str = json.dumps(details)
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
