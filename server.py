'''
Start HTTP server to proces incoming connections
'''

import datetime
import os
import random
import time
from socketserver import ThreadingMixIn
from threading import Thread
from http.server import BaseHTTPRequestHandler, HTTPServer

""" pymongo
    mongoengine
    A very good understanding of statistics incl. linear and logistic regression, probability, hypothesis testing and statistical confidence, cluster analysis;
Experience training and optimizing machine learning models and the accompanying algorithms and methods (e.g. Bayesian, Forest/Tree, SVM, SGD, Neural Nets e.g Keras/Theano/Tensorflow, boosting, logistic regression);
    Hadoop, Spark, Hive, Drill, Impala, Elastic search
    Strong mathematical background
    gRPC
    rest-api for mobile platform
    Redis, Celery, Django
    async python
    PyTest, Behave, CI (Jenkins), Gerrit, Qt - tests
    Django/DRF/Other RESTful frameworks
    Tornado web framework, Celery
    Pig, Hive, Hadoop/MapReduce
"""

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Threaded class"""
    pass

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("ThreadedHTTPServer.do_GET: PID {0} is processing...".format(os.getpid()))

        time.sleep(random.randrange(3))

        self.send_response(200)
        #self.headers({"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"})
        responceMessage = 'Server {0} V{1} responded with: {2}; on request: {3}'.format(self.server, self.server_version, self.responses, self.request)
        #responceMessage = 'Server ' + self.server + ' V' + self.server_version + ' responded with: ' + ' ' + self.responses + '; on request: ' + self.request
        self.wfile.write(responceMessage.encode())
        self.end_headers()



def run():
    serverAddress = ('localhost', 18081)
    print("HTTP Server starts on {0}".format(serverAddress))
    httpd = ThreadedHTTPServer(serverAddress, Handler)
    httpd.serve_forever()

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt as e:
        print("Interrupted by keyboard: {0}".format(e))