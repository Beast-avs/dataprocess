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


def makeRequest(request):
    destination = 'localhost:8080'
    ip, port = destination.split(':')
    sleeptime = randrange(5)
    result = None
    try:
        result = "Request on '{0}':'{1}' is '{2}'. Sleep for {3}".format(ip, port, request, sleeptime)
        pass
    except:
        result = "Error on '{0}':'{1}' is '{2}'. Sleep for {3}. Error: {4}".format(ip, port, request, sleeptime, sys.exc_info())
        pass
    finally:
        time.sleep(sleeptime)
        print(result)

def processSuccess(data):
    print("PID: {0}; data is: {1}".format(os.getpid(), data))

if __name__ == '__main__':
    source = ['one', 'two', 'three', '1', '2', '3','a','b','c','d']
    poolLength = 2
    pool = Pool(processes=poolLength)
    responces = [pool.apply_async(makeRequest, (source[i], ), callback=processSuccess) for i in range(len(source))]
    taskNum = 0
    for i in responces:
        i.wait()
        if ((taskNum == len(source)-2) and taskNum < 20):
            print("Added 5 more tasks, {0}".format(taskNum))
            for k in list(range(5)):
                responces.append(pool.apply_async(makeRequest, (source.append("Added {0}".format(k)),), callback=processSuccess))
        taskNum+=1