import json
import urllib2

def getdata( url, headers = {} ):
    req = urllib2.Request(url, headers = headers)

    try:
        resp = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        raise Exception("Request to %s failed with error %s" % (url , str(e.code)))
    except urllib2.URLError, e:
        raise Exception("Request to %s failed with URLError =  %s" % (url , str(e.reason)))
    except httplib.HTTPException, e:
        raise Exception("Request to %s failed with HTTPException" % (url))
    except Exception:
        raise Exception("Request to %s failed with Exeption" % (url))

    respData = resp.read()

    return  json.loads(respData)
