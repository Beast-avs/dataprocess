import requests
import urllib

class HTTPclient:
    def __init__(self):
        self.dbg = "DEBUG"

    def sendRequest(self, request):
        headers = request['headers']
        uri = request['uri']
        user = request['user']
        pwd = request['pwd']
        data = request['data']

        #print("HTTPclient.sendRequest: headers: {0}; uri: {1}; user/pwd: {2}/{3}; data: {4}".format(headers, uri, user, pwd, data))
        try:
            response = requests.get(uri, auth=(user, pwd), headers=headers, data=data)
        except requests.exceptions.ConnectionError as e:
            return "Connection Error for '{0}': {1}".format(uri, e)

        # Check for HTTP codes other than 200
        if response.status_code != 200:
            print('ERROR. Status:' + str(response.status_code) + 'Headers:' + str(
                response.headers) + 'Error Response:' + str(response.json()))
            return
        else:
            return response