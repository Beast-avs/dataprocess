'''
Client that sends several connections to server.


Parameters:
    - serverIP:port - connection settings
    - user:pwd - user credentials if server accepts AUTH
'''

import logging
import os
from multiprocessing import Pool
import time
from random import randrange
import sys
from lib.HTTPclient import HTTPclient


def makeRequest(request):
    destination = 'localhost:8080'
    ip, port = destination.split(':')
    sleeptime = randrange(5)
    result = None
    client = HTTPclient()
    print("client dict: {0}".format(client.__dict__))
    try:
        result = "Request on '{0}':'{1}' is '{2}'. Sleep for {3}".format(ip, port, request, sleeptime)
        req = {"headers":{"Content-Type": "application/json", "Accept": "application/json"},
                   "uri":"http://{0}:{1}".format(ip, port),
                   "user":"user1", "pwd":"pwd123",
                   #"data":"{\"name\":\"test_{0}\", \"attributes\":[{\"key1\":\"val1\"}, {\"key2\":\"val2\"}]}".format(request)}
                    "data":"test_{0}".format(request)}
        resp = client.sendRequest(req)
        print("Response is: {0}".format(resp))
        pass
    except:
        result = "Error: {0}".format(sys.exc_info())
        pass
    finally:
        time.sleep(sleeptime)
        print(result)

def processSuccess(data):
    #print("PID: {0}; data is: {1}".format(os.getpid(), data))
    pass

if __name__ == '__main__':
    source = ['one', 'two', 'three', '1', '2', '3','a','b','c','d']
    poolLength = 2
    pool = Pool(processes=poolLength)
    responces = [pool.apply_async(makeRequest, (source[i], ), callback=processSuccess) for i in range(len(source))]
    #taskNum = 0
    for i in responces:
        i.wait()
        #if ((taskNum == len(source)-2) and taskNum < 20):
        #    print("Added 5 more tasks, {0}".format(taskNum))
        #    for k in list(range(5)):
        #        responces.append(pool.apply_async(makeRequest, (source.append("Added {0}".format(k)),), callback=processSuccess))
        #taskNum+=1