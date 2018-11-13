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

def registerThread(lock1,file1,lock2,file2,devicename):

    start_time = time.time()
    success, apikey = register(str(devicename))
    end_time=time.time()
    lock1.acquire()
    try:
        file1 = open("register.txt", "a+")
        file1.write(str(end_time-start_time))
        #print(str(end_time-start_time))
        file1.write("\n")
        file1.close()
    finally:
        lock1.release()

    start_time = time.time()
    success = deregister(str(devicename))
    end_time = time.time()
    lock2.acquire()
    try:
        file2 = open("deregister.txt", "a+")
        file2.write(str(end_time-start_time))
        file2.write("\n")
        #print(str(end_time-start_time))
        file2.close()
    finally:
        lock2.release()



def register_devices():

    #     # devices and apps:
    i=0

    for d in devices:
        start_time = time.time()
        success, apikey = register(d)
        elapsed_time = time.time() - start_time
        #print (success)
        i=i+1
        device_apikey.append(apikey)
        print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

def deregister_devices():
    for d in devices:
        start_time = time.time()
        success = deregister(d)
        elapsed_time = time.time() - start_time
        print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
        #print(success)

if __name__=='__main__':

    file1 = open("register.txt", "w+")
    file2 = open("deregister.txt", "w+")
    lock1 = Lock()
    lock2 = Lock()
    processes = []
    # Register device1
    for m in devices:
        p = Process(target=registerThread, args=(lock1, file1,lock2,file2,m))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    #print "-----------------------------------------------------"
    #register_devices()
    #deregister_devices()


