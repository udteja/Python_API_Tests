import requests
import json
import FormeAPITest.src


def GetRequest(url, headers, parameter=None):
#    if parameter:
#        url = '?s=' + str(parameter)
    if parameter:
        resp = requests.request("GET", url, headers=headers, params={'s': json.dumps(parameter)})
    else:
        resp = requests.request("GET", url, headers=headers)
    return resp


def PostRequest(url, headers, payload):
    resp = requests.request("POST", url, headers=headers, data=payload)
    return resp
