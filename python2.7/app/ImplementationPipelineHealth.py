import json
from threading import Thread
import DataOps

global implementation_epics
implementation_epics = []

class implementation_health_thread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global implementation_epics
        epics = []

        pagesize = 100
        fetch = 'true'
        query = 'query=(Project.Name%20=%20"DX%20SANDBOX")'
        headers = {'content-type': 'application/json', 'Authorization': 'Basic aWFzYWxhemFyQHRla3N5c3RlbXMuY29tOnBhbmNobzEyMw=='}
        address = 'https://sandbox.rallydev.com'
        params = '/slm/webservice/v2.0/portfolioitem/epic?fetch=' + fetch + '&start=1&pagesize=' + str(pagesize) + '&' + query
        print "getting implementation_epics"
        epicresults = DataOps.getdata( address + params, headers )

        for key in epicresults['QueryResult']['Results']:
            getfeatures(str(key['FormattedID']), str(key['Name']), epics, str(key['Children']['_ref']))

        print "got implementation_epipcs"
        implementation_epics = epics

def getfeatures( epic_id, epic_name, epics, url ):
    headers = {'content-type': 'application/json', 'Authorization': 'Basic aWFzYWxhemFyQHRla3N5c3RlbXMuY29tOnBhbmNobzEyMw=='}
    queryresults = DataOps.getdata( url, headers )

    for key in queryresults['QueryResult']['Results']:
        Total = 0
        Defined = 0
        InProgress = 0
        Demoed = 0
        dict = {'Epic': '', 'EpicName': '', 'Feature': '', 'FeatureName': '', 'Owner': '', 'Status': 'Green', 'TotalUserStories': 0,
                'DefinedUserStories': 0, 'UserStoriesInProgress': 0, 'DemoedUserStories': 0}

        dict['Epic'] = epic_id
        dict['EpicName'] = epic_name
        dict['Feature'] = str(key['FormattedID'])
        dict['FeatureName'] = str(key['Name'])

        if key['Owner']:
            dict['Owner'] = key['Owner']['_refObjectName']
        else:
            dict['Owner'] = 'Unassigned'

        Total, Defined, InProgress, Demoed = getuserstoryinfo(key['UserStories']['_ref'])

        dict['TotalUserStories'] = Total
        dict['DefinedUserStories'] = Defined
        dict['UserStoriesInProgress'] = InProgress
        dict['DemoedUserStories'] = Demoed

	epics.append(dict)

def getuserstoryinfo(url):
    count = 0
    defined = 0
    inprogress = 0
    demoed = 0
    headers = {'content-type': 'application/json', 'Authorization': 'Basic aWFzYWxhemFyQHRla3N5c3RlbXMuY29tOnBhbmNobzEyMw=='}

    queryresults = DataOps.getdata( url, headers )

    for key in queryresults['QueryResult']['Results']:
        count = count + 1

        if key['FlowState']['_refObjectName'] == 'Defined':
            defined = defined + 1

        if key['FlowState']['_refObjectName'] == 'In-Progress':
            inprogress = inprogress + 1

        if key['FlowState']['_refObjectName'] == 'Accepted':
            demoed = demoed + 1

    return count, defined, inprogress, demoed
