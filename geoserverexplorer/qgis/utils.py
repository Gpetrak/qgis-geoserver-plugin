# -*- coding: utf-8 -*-

#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
from builtins import str
import os
import uuid
import time

from qgis.PyQt.QtCore import QDir
from qgis.PyQt.QtWidgets import QMessageBox
from qgis.utils import iface

from geoserverexplorer.qgis import layers as qgislayers
from geoserverexplorer.qgis import uri as uri_utils

class UserCanceledOperation(Warning):
    pass

def checkLayers():
    layers = qgislayers.getAllLayers()
    if len(layers) == 0:
        QMessageBox.warning(iface.mainWindow(), 'QGIS layers needed',
            "No suitable layers can be found in your current QGIS project.\n"
            "You must open the layers in QGIS to be able to work with them.",
            QMessageBox.Ok)
        return False
    return True

def tempFolder():
    tempDir = os.path.join(str(QDir.tempPath()), "geoserverplugin")
    if not QDir(tempDir).exists():
        QDir().mkpath(tempDir)
    return str(os.path.abspath(tempDir))

def tempFilename(ext):
    path = tempFolder()
    ext = "" if ext is None else ext
    filename = path + os.sep + str(time.time())  + "." + ext
    return filename

def tempFilenameInTempFolder(basename):
    '''returns a temporary filename for a given file, putting it into a temp folder but not changing its basename'''
    path = tempFolder()
    folder = os.path.join(path, str(uuid.uuid4()).replace("-",""))
    mkdir(folder)
    filename =  os.path.join(folder, basename)
    return filename

def mkdir(newdir):
    if os.path.isdir(newdir):
        pass
    else:
        head, tail = os.path.split(newdir)
        if head and not os.path.isdir(head):
            mkdir(head)
        if tail:
            os.mkdir(newdir)

def isWindows():
    return os.name == 'nt'



