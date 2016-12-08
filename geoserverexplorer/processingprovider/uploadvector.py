# -*- coding: utf-8 -*-
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
import os

try:
    from qgis.core import QGis
except ImportError:
    from qgis.core import Qgis as QGis

from geoserveralgorithm import GeoServerAlgorithm
from processing.core.parameters import ParameterVector, ParameterString
from processing.tools import dataobjects


class UploadVector(GeoServerAlgorithm):

    INPUT = 'INPUT'
    WORKSPACE = 'WORKSPACE'

    def processAlgorithm(self, progress):
        self.createCatalog()
        inputFilename = self.getParameterValue(self.INPUT)
        layer = dataobjects.getObjectFromUri(inputFilename)
        workspaceName = self.getParameterValue(self.WORKSPACE)
        filename = dataobjects.exportVectorLayer(layer)
        basefilename = os.path.basename(filename)
        basepathname = os.path.dirname(filename) + os.sep \
            + basefilename[:basefilename.find('.')]
        connection = {
            'shp': basepathname + '.shp',
            'shx': basepathname + '.shx',
            'dbf': basepathname + '.dbf',
            'prj': basepathname + '.prj',
            }

        workspace = self.catalog.get_workspace(workspaceName)
        self.catalog.create_featurestore(basefilename, connection, workspace)

    def defineCharacteristics(self):
        self.addBaseParameters()
        self.name = 'Upload vector'
        self.group = 'GeoServer tools'
        if QGis.QGIS_VERSION_INT < 29900:
            self.addParameter(ParameterVector(self.INPUT, 'Layer to import',
                              [ParameterVector.VECTOR_TYPE_ANY]))
        else:
            self.addParameter(ParameterVector(self.INPUT, 'Layer to import',
                              [dataobjects.TYPE_VECTOR_ANY]))

        self.addParameter(ParameterString(self.WORKSPACE, 'Workspace'))
