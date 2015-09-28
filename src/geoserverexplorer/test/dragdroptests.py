#===============================================================================
# import unittest
# import os
# from geoserverexplorer.test.utils import PT1, WORKSPACE, WORKSPACEB, STYLE, PT2, PT3,\
#     GROUP, GEOLOGY_GROUP, LANDUSE, GEOFORMS, PUBLIC_SCHEMA
# from geoserverexplorer.test.integrationtest import ExplorerIntegrationTest
# from geoserverexplorer.gui.pgoperations import importToPostGIS
# from geoserverexplorer.qgis import layers
#
# class DragDropTests(ExplorerIntegrationTest):
#
#     #===========================================================================
#     # Drag & drop URIs (i.e. from QGIS browser) to a Explorer tree item
#     #===========================================================================
#
#     def testDropVectorLayerUriInCatalogItem(self):
#         uri = os.path.join(os.path.dirname(__file__), "data", PT1 + ".shp")
#         self.catalogItem.acceptDroppedUris(self.tree, self.explorer, [uri])
#         layer = self.cat.get_layer(PT1)
#         self.assertIsNotNone(layer)
#         self.cat.get_store(PT1, WORKSPACE)
#         self.cat.delete(self.cat.get_layer(PT1), recurse = True)
#         self.cat.delete(self.cat.get_style(PT1), purge = True)
#
#     def testDropVectorLayerUriInWorkspaceItem(self):
#         uri = os.path.join(os.path.dirname(__file__), "data", PT1 + ".shp")
#         item = self.getWorkspaceItem(WORKSPACEB)
#         self.assertIsNotNone(item)
#         item.acceptDroppedUris(self.tree, self.explorer, [uri])
#         layer = self.cat.get_layer(PT1)
#         self.assertIsNotNone(layer)
#         self.cat.get_store(PT1, WORKSPACEB)
#         self.cat.delete(self.cat.get_layer(PT1), recurse = True)
#         self.cat.delete(self.cat.get_style(PT1), purge = True)
#
#     def testDropVectorLayerUriInLayersItem(self):
#         uri = os.path.join(os.path.dirname(__file__), "data", PT1 + ".shp")
#         item = self.catalogItem.child(1)
#         item.acceptDroppedUris(self.tree, self.explorer, [uri])
#         layer = self.cat.get_layer(PT1)
#         self.assertIsNotNone(layer)
#         self.cat.get_store(PT1, WORKSPACE)
#         self.cat.delete(self.cat.get_layer(PT1), recurse = True)
#         self.cat.delete(self.cat.get_style(PT1), purge = True)
#
#     #===========================================================================
#     # Drag & drop explorer tree element(s) into another explorer tree element
#     #===========================================================================
#
#
#     def testDropGsStyleInGsLayerItem(self):
#         styleItem = self.getStyleItem(STYLE)
#         self.assertIsNotNone(styleItem)
#         layerItem = self.getLayerItem(PT2)
#         self.assertIsNotNone(layerItem)
#         layerItem.acceptDroppedItems(self.tree, self.explorer, [styleItem])
#         self.assertIsNotNone(self._getItemUnder(layerItem, STYLE))
#
#     def testDropGsLayerInGsGroupItem(self):
#         groupItem = self.getGroupItem(GROUP)
#         childCount = groupItem.childCount()
#         layerItem = self.getLayerItem(PT3)
#         groupItem.acceptDroppedItems(self.tree, self.explorer, [layerItem])
#         self.assertEquals(childCount + 1, groupItem.childCount())
#
#
# def suite():
#     suite = unittest.makeSuite(DragDropTests, 'test')
#     return suite
#===============================================================================
