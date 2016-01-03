#!/usr/bin/python

import sys, traceback, Ice
import easyiceconfig as EasyIce
import jderobot
import sensors
from PyQt4 import QtGui,QtCore

ic = None
status = 0

try:
    ic = EasyIce.initialize(sys.argv)
    properties  = ic.getProperties()
    basecamera  = ic.propertyToProxy("cameraA:default -h 0.0.0.0 -p 9999")
    cameraProxy = jderobot.CameraPrx.checkedCast(basecamera)

    if cameraProxy:
        image = cameraProxy.getImageData("RGB8")
        height= image.description.height
        width = image.description.width

        trackImage = np.zeros((height, width,3), np.uint8)
        trackImage.shape = height, width, 3

        thresoldImage = np.zeros((height, width,1), np.uint8)
        thresoldImage.shape = height, width,

    else:
        print 'Interface camera not connected'
        status = 1

except:
    traceback.print_exc()
    status = 1

sys.exit(status)
