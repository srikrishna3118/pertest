from __future__ import print_function
import os, sys
from multiprocessing import Process, Lock
# logging
import logging
import time
logger = logging.getLogger(__name__)
# suppress debug messages from other modules used.
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("communication_interface").setLevel(logging.WARNING)

# routines for setting up entities and permissions in the middleware
#sys.path.insert(0, '../messaging')
from ideam_messaging import *

devices = ["device" + str(i) for i in range(1)]
apps = ["application" + str(i) for i in range(1)]
device_apikey=[]



def register_devices():

    #     # devices and apps:

    for d in devices:
        start_time = time.time()
        success, apikey = register(d)
        elapsed_time = time.time() - start_time
        #print (success)
        device_apikey.append(apikey)
        print(apikey)
        print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

def deregister_devices():
    for d in devices:
        #start_time = time.time()
        success = deregister(d)
        #elapsed_time = time.time() - start_time
        #print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
        #print(success)


if __name__=='__main__':



    try:
        register_devices()
        file = open("10kb.txt", "r")
        print (device_apikey)
        i=0
        while i<1:
            publish(devices[0],device_apikey[0],str(file.read()))
            #publish(devices[0], device_apikey[0], "asd")
            #publish(devices[0], device_apikey[0], "asd")
            #publish(devices[0], device_apikey[0], "asd")
            i=i+1
            #time.sleep(3)
    finally:
        #time.sleep(10)
        #deregister_devices()
        pass

