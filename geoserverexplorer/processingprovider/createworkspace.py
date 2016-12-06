# -*- coding: utf-8 -*-
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
from processing.core.parameters import ParameterString
from processing.core.outputs import OutputString
from geoserverexplorer.processingprovider.geoserveralgorithm import GeoServerAlgorithm


class CreateWorkspace(GeoServerAlgorithm):

    WORKSPACE = 'WORKSPACE'
    WORKSPACEURI = 'WORKSPACEURI'

    def processAlgorithm(self, progress):
        self.createCatalog()
        workspaceName = self.getParameterValue(self.WORKSPACE)
        workspaceUri = self.getParameterValue(self.WORKSPACEURI)
        self.catalog.create_workspace(workspaceName, workspaceUri)

    def defineCharacteristics(self):
        self.addBaseParameters()
        self.name = 'Create workspace'
        self.group = 'GeoServer tools'
        self.addParameter(ParameterString(self.WORKSPACE, 'Workspace'))
        self.addParameter(ParameterString(self.WORKSPACEURI, 'Workspace URI'))
        self.addOutput(OutputString(self.WORKSPACE, 'Workspace'))
