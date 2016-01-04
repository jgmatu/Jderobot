#!/usr/bin/python

import sys, traceback, Ice
from PyQt4 import QtGui,QtCore
import easyiceconfig as EasyIce
import numpy as np
import jderobot
import sensors
import threading



ic = None
status = 0
try:

    ic          = EasyIce.initialize(sys.argv)
    basecamera  = ic.stringToProxy("cameraA:default -h 0.0.0.0 -p 9999 ")
    cameraProxy = jderobot.CameraPrx.checkedCast(basecamera)

    print(cameraProxy)
    
    if cameraProxy:

        image = cameraProxy.getImageData("RGB8")
        width = image.description.width
        height= image.description.height

        CameraDesc = cameraProxy.getCameraDescription()

        print(CameraDesc)

        trackImage = np.zeros((height, width,3), np.uint8)
        trackImage.shape = height, width, 3

        thresoldImage = np.zeros((height, width,1), np.uint8)
        thresoldImage.shape = height, width,

    else:

        print 'Interface camera not connected'
        status = 1

except:

    traceback.print_exc()
    exit()
    status = 1

if ic:
    # Clean up
    try:
        ic.destroy()
    except:
        traceback.print_exc()
        status = 1

sys.exit(status)
