#!/usr/bin/python

import sys, traceback, Ice
import easyiceconfig as EasyIce
import numpy as np
import jderobot
from PyQt4.QtCore import *
from PyQt4.QtGui import *



# Mirate el GUI de jderobot ;) descansa ! :) felices reyes magos javi! : )
ic = None
status = 0
try:

    ic          = EasyIce.initialize(sys.argv)
    basecamera  = ic.stringToProxy("cameraA:default -h 0.0.0.0 -p 9999 ")
    cameraProxy = jderobot.CameraPrx.checkedCast(basecamera)



    app = QApplication(sys.argv)
    grview = QGraphicsView()
    scene = QGraphicsScene()

    while cameraProxy :

        image = cameraProxy.getImageData("RGB8")
        # Image data bytes pixels
        scene.addPixmap(QPixmap(image.pixelData))
        grview.setScene(scene)
        grview.show()

        print(image.pixelData)
        width = image.description.width
        height= image.description.height

        cameraDescription = cameraProxy.getCameraDescription()
        imageDescription  = cameraProxy.getImageDescription()

        trackImage = np.zeros((height, width,3), np.uint8)
        trackImage.shape = height, width, 3

        thresoldImage = np.zeros((height, width,1), np.uint8)
        thresoldImage.shape = height, width,

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

sys.exit(app.exec_())
