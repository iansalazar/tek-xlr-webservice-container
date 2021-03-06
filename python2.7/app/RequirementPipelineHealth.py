import json
from threading import Thread
import DataOps

global requirement_epics
requirement_epics = []

class requirement_health_thread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global requirement_epics
        epics = []

        pagesize = 100
        fetch = 'true'
        query = 'query=(Project.Name%20=%20"DX%20SANDBOX")'
        headers = {'content-type': 'application/json', 'Authorization': 'Basic aWFzYWxhemFyQHRla3N5c3RlbXMuY29tOnBhbmNobzEyMw=='}
        address = 'https://sandbox.rallydev.com'
        params = '/slm/webservice/v2.0/portfolioitem/epic?fetch=' + fetch + '&start=1&pagesize=' + str(pagesize) + '&' + query
        print "getting requirement_epics"
        epicresults = DataOps.getdata( address + params, headers )

        for key in epicresults['QueryResult']['Results']:
            getfeatures(str(key['FormattedID']), str(key['Name']), epics, str(key['Children']['_ref']))

        print "got requirement_epipcs"
        requirement_epics = epics

def getfeatures( epic_id, epic_name, epics, url ):
    headers = {'content-type': 'application/json', 'Authorization': 'Basic aWFzYWxhemFyQHRla3N5c3RlbXMuY29tOnBhbmNobzEyMw=='}
    queryresults = DataOps.getdata( url, headers )

    for key in queryresults['QueryResult']['Results']:
        Total = 0
        Undefined = 0
        Defined = 0
        dict = {'Epic': '', 'EpicName': '', 'Feature': '', 'FeatureName': '', 'Owner': '', 'Status': 'Green', 'TotalUserStories': 0,
                'UndefinedUserStories': 0,
                'DefinedUserStories': 0}

        dict['Epic'] = epic_id
        dict['EpicName'] = epic_name
        dict['Feature'] = str(key['FormattedID'])
        dict['FeatureName'] = str(key['Name'])

        if key['Owner']:
            dict['Owner'] = key['Owner']['_refObjectName']
        else:
            dict['Owner'] = 'Unassigned'

        Total, Undefined, Defined = getuserstoryinfo(key['UserStories']['_ref'])

        dict['TotalUserStories'] = Total
        dict['UndefinedUserStories'] = Undefined
        dict['DefinedUserStories'] = Defined
        epics.append(dict)

def getuserstoryinfo(url):
    count = 0
    undefined = 0
    defined = 0
    headers = {'content-type': 'application/json', 'Authorization': 'Basic aWFzYWxhemFyQHRla3N5c3RlbXMuY29tOnBhbmNobzEyMw=='}

    queryresults = DataOps.getdata( url, headers )

    for key in queryresults['QueryResult']['Results']:
        count = count + 1

        if key['FlowState']['_refObjectName'] == 'Defined':
            defined = defined + 1

        if key['FlowState']['_refObjectName'] == 'Undefined':
            undefined = undefined + 1

    return count, undefined, defined
