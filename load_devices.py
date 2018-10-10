from __future__ import print_function
import os, sys

# logging
import logging
logger = logging.getLogger(__name__)
# suppress debug messages from other modules used.
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("communication_interface").setLevel(logging.WARNING)

# routines for setting up entities and permissions in the middleware
#sys.path.insert(0, '../messaging')
from ideam_messaging import *

devices
apps

def register():

    # devices and apps:
    devices = ["device" + str(i) for i in range(4)]
    apps = ["application" + str(i) for i in range(1)]

