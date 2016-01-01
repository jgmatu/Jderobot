#!/usr/bin/python

import sys, traceback, Ice
import jderobot

status = 0
ic = None
try:

    ic     = Ice.initialize(sys.argv)
    base   = ic.propertyToProxy("cameraA:default -h 0.0.0.0 -p 9999")
    camera = jderobot.CameraPrx.checkedCast(base)

    camRGB = jderobot.cameraClient(ic , "Cameraview.Camera.")
    camRGB.start()

    if not camRGB:
        raise RuntimeError("Invalid Proxy")

    while viewerself.isVisible():
        print ("Images....")
    	camRGB.getImage(rgb)
	viewer.display(rgb)
	viewer.displayFrameRate(camRGB->getRefreshRate());

except:
    traceback.print_exc()
    status = 1

if ic:
    # Clean up
    try:
        ic.destroy()
    except:
        traceback.print_exc()
        status = 1

sys.exit(status)
