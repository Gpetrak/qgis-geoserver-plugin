# -*- coding: utf-8 -*-
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
import os
from qgis.PyQt.QtGui import QIcon
from processing.core.AlgorithmProvider import AlgorithmProvider
from processing.core.ProcessingConfig import Setting, ProcessingConfig
from geoserverexplorer.processingprovider.uploadvector import UploadVector
from geoserverexplorer.processingprovider.uploadraster import UploadRaster
from geoserverexplorer.processingprovider.createstyle import CreateStyle
from geoserverexplorer.processingprovider.createworkspace import CreateWorkspace
from geoserverexplorer.processingprovider.deleteworkspace import DeleteWorkspace
from geoserverexplorer.processingprovider.deletedatastore import DeleteDatastore

class GeoServerProvider(AlgorithmProvider):

    MY_DUMMY_SETTING = 'MY_DUMMY_SETTING'

    def __init__(self):
        AlgorithmProvider.__init__(self)

        self.activate = True

        # Load algorithms
        self.alglist = [
            UploadVector(),
            UploadRaster(),
            CreateWorkspace(),
            DeleteWorkspace(),
            DeleteDatastore(),
            CreateStyle(),
            ]
        for alg in self.alglist:
            alg.provider = self

    def initializeSettings(self):
        AlgorithmProvider.initializeSettings(self)

    def unload(self):
        AlgorithmProvider.unload(self)

    def getName(self):
        return 'geoserver'

    def getDescription(self):
        return 'GeoServer tools'

    def getIcon(self):
        return QIcon(os.path.dirname(__file__) + "/../images/geoserver.png")

    def _loadAlgorithms(self):
        self.algs = self.alglist
