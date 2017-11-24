from flask import Flask
import json

app = Flask(__name__)

@app.route("/epicstatus")
def epicstatus():
    details = [
		{"name":"DE1", "url":"http://www.google.com", "owner":"J. Doe", "status":"Green" , "teststart":"10/01/17", "testcasesassigned": 4, "executed": 4, "percentcomplete": 100, 
                 "passed": 4, "failed": 0, "defectslogged": 1, "open": 0, "resolved": 0, "closed": 1},
                {"name":"DE2", "url":"http://www.google.com", "owner":"J. Doe", "status":"Green", "teststart":"10/01/17", "testcasesassigned": 9, "executed": 9, "percentcomplete": 100, 
                 "passed": 9, "failed": 0, "defectslogged": 0, "open": 0, "resolved": 0, "closed": 0},
                {"name":"DE3", "url":"http://www.google.com", "owner":"J. Doe", "status":"Green", "teststart":"10/01/17", "testcasesassigned": 1, "executed": 1, "percentcomplete": 100,    
                 "passed": 1, "failed": 0, "defectslogged": 1, "open": 0, "resolved": 0, "closed": 1},
                {"name":"DE4", "url":"http://www.google.com", "owner":"J. Doe", "status":"Green", "teststart":"10/01/17", "testcasesassigned": 4, "executed": 4, "percentcomplete": 100,    
                 "passed": 4, "failed": 0, "defectslogged": 0, "open": 0, "resolved": 0, "closed": 0},
                {"name":"DE5", "url":"http://www.google.com", "owner":"J. Doe", "status":"Green", "teststart":"10/01/17", "testcasesassigned": 2, "executed": 2, "percentcomplete": 100,    
                 "passed": 9, "failed": 2, "defectslogged": 0, "open": 0, "resolved": 0, "closed": 0},
                {"name":"DE6", "url":"http://www.google.com", "owner":"J. Doe", "status":"Green", "teststart":"10/01/17", "testcasesassigned": 6, "executed": 6, "percentcomplete": 100,    
                 "passed": 6, "failed": 0, "defectslogged": 0, "open": 0, "resolved": 0, "closed": 0},
                {"name":"DE7", "url":"http://www.google.com", "owner":"J. Doe", "status":"Green", "teststart":"10/01/17", "testcasesassigned": 14, "executed": 14, "percentcomplete": 100,    
                 "passed": 14, "failed": 0, "defectslogged": 0, "open": 0, "resolved": 0, "closed": 0},
                {"name":"DE8", "url":"http://www.google.com", "owner":"J. Doe", "status":"Green", "teststart":"10/01/17", "testcasesassigned": 10, "executed": 10, "percentcomplete": 100,    
                 "passed": 10, "failed": 0, "defectslogged": 0, "open": 0, "resolved": 0, "closed": 0},
                {"name":"DE9", "url":"http://www.google.com", "owner":"J. Doe", "status":"Red", "teststart":"11/15/17", "testcasesassigned": 4, "executed": 4, "percentcomplete": 100,    
                 "passed": 4, "failed": 1, "defectslogged": 1, "open": 1, "resolved": 0, "closed": 0}
              ]
    json_str = json.dumps(details)
    return json_str

@app.route("/storystatus")
def storystatus():
    details = [
                {"name":"Story1", "url":"http://www.google.com", "owner":"J. Doe", "status":"Green" , "teststart":"10/01/17", "testcasesassigned": 4, "executed": 4, "percentcomplete": 100,
                 "passed": 4, "failed": 0, "defectslogged": 1, "open": 0, "resolved": 0, "closed": 1},
                {"name":"Story2", "url":"http://www.google.com", "owner":"J. Doe", "status":"Green", "teststart":"10/01/17", "testcasesassigned": 9, "executed": 9, "percentcomplete": 100,
                 "passed": 9, "failed": 0, "defectslogged": 0, "open": 0, "resolved": 0, "closed": 0},
                {"name":"Story3", "url":"http://www.google.com", "owner":"J. Doe", "status":"Green", "teststart":"10/01/17", "testcasesassigned": 1, "executed": 1, "percentcomplete": 100,
                 "passed": 1, "failed": 0, "defectslogged": 1, "open": 0, "resolved": 0, "closed": 1},
                {"name":"Story4", "url":"http://www.google.com", "owner":"J. Doe", "status":"Green", "teststart":"10/01/17", "testcasesassigned": 4, "executed": 4, "percentcomplete": 100,
                 "passed": 4, "failed": 0, "defectslogged": 0, "open": 0, "resolved": 0, "closed": 0},
                {"name":"Story5", "url":"http://www.google.com", "owner":"J. Doe", "status":"Green", "teststart":"10/01/17", "testcasesassigned": 2, "executed": 2, "percentcomplete": 100,
                 "passed": 9, "failed": 2, "defectslogged": 0, "open": 0, "resolved": 0, "closed": 0},
                {"name":"Story6", "url":"http://www.google.com", "owner":"J. Doe", "status":"Green", "teststart":"10/01/17", "testcasesassigned": 6, "executed": 6, "percentcomplete": 100,
                 "passed": 6, "failed": 0, "defectslogged": 0, "open": 0, "resolved": 0, "closed": 0},
                {"name":"Story7", "url":"http://www.google.com", "owner":"J. Doe", "status":"Green", "teststart":"10/01/17", "testcasesassigned": 14, "executed": 14, "percentcomplete": 100,
                 "passed": 14, "failed": 0, "defectslogged": 0, "open": 0, "resolved": 0, "closed": 0},
                {"name":"Story8", "url":"http://www.google.com", "owner":"J. Doe", "status":"Green", "teststart":"10/01/17", "testcasesassigned": 10, "executed": 10, "percentcomplete": 100,
                 "passed": 10, "failed": 0, "defectslogged": 0, "open": 0, "resolved": 0, "closed": 0},
                {"name":"Story9", "url":"http://www.google.com", "owner":"J. Doe", "status":"Red", "teststart":"11/15/17", "testcasesassigned": 4, "executed": 4, "percentcomplete": 100,
                 "passed": 3, "failed": 1, "defectslogged": 1, "open": 1, "resolved": 0, "closed": 0},
                {"name":"Story10", "url":"http://www.google.com", "owner":"J. Doe", "status":"Red", "teststart":"11/15/17", "testcasesassigned": 6, "executed": 6, "percentcomplete": 100,
                 "passed": 3, "failed": 3, "defectslogged": 3, "open": 3, "resolved": 0, "closed": 0},
                {"name":"Story11", "url":"http://www.google.com", "owner":"J. Doe", "status":"Red", "teststart":"11/15/17", "testcasesassigned": 4, "executed": 4, "percentcomplete": 100,
                 "passed": 3, "failed": 1, "defectslogged": 1, "open": 1, "resolved": 0, "closed": 0},
                {"name":"Story12", "url":"http://www.google.com", "owner":"J. Doe", "status":"Red", "teststart":"11/15/17", "testcasesassigned": 8, "executed": 8, "percentcomplete": 100,
                 "passed": 4, "failed": 4, "defectslogged": 4, "open": 4, "resolved": 0, "closed": 0}
              ]
    json_str = json.dumps(details)
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

@app.route("/featuresinprogress")
def featuresinprogress():
    details = [ 
                {"description":"Feature 1 Description", "stories": 4},
		{"description":"Feature 2 Description", "stories": 1},
		{"description":"Feature 3 Description", "stories": 2},
		{"description":"Feature 4 Description", "stories": 7},
		{"description":"Feature 5 Description", "stories": 3},
		{"description":"Feature 6 Description", "stories": 8},
		{"description":"Feature 7 Description", "stories": 5},
		{"description":"Feature 8 Description", "stories": 9}
              ]

    json_str = json.dumps(details)
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
