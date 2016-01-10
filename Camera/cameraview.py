#!/usr/bin/python

import sys, traceback, Ice
import easyiceconfig as EasyIce
import numpy as np
import jderobot
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import matplotlib.pyplot as plt



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
    cameraDescription = cameraProxy.getCameraDescription()

    while cameraProxy :

        image = cameraProxy.getImageData("RGB8")
        imageDescription  = cameraProxy.getImageDescription()

        width = image.description.width
        height= image.description.height

        img = np.zeros((height , width , 3) , np.uint8)
        img = np.frombuffer(image.pixelData , dtype=np.uint8)
        img.shape = height, width, 3

        plt.imshow(img,aspect="auto")
        plt.show()
        scene.addPixmap(QPixmap(img))
        grview.setScene(scene)
        grview.show()

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
