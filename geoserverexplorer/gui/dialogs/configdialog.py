# -*- coding: utf-8 -*-
#
# (c) 2016 Boundless, http://boundlessgeo.com
# This code is licensed under the GPL 2.0 license.
#
from builtins import str
from builtins import range

import os

from qgis.PyQt.QtCore import Qt, QSettings
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import (QDialog,
                                 QVBoxLayout,
                                 QTreeWidget,
                                 QDialogButtonBox,
                                 QTreeWidgetItem,
                                 QTreeWidgetItemIterator
                                )
from qgis.gui import QgsFilterLineEdit


class ConfigDialog(QDialog):

    def __init__(self, explorer):
        self.explorer = explorer
        QDialog.__init__(self)
        self.setupUi()
        if hasattr(self.searchBox, 'setPlaceholderText'):
            self.searchBox.setPlaceholderText(self.tr("Search..."))
        self.searchBox.textChanged.connect(self.filterTree)
        self.fillTree()
        self.tree.expandAll()

    def setupUi(self):
        self.setMinimumWidth(500)
        self.setMinimumHeight(400)
        self.resize(640, 450)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(0)
        self.searchBox = QgsFilterLineEdit(self)
        self.verticalLayout.addWidget(self.searchBox)
        self.tree = QTreeWidget(self)
        self.tree.setAlternatingRowColors(True)
        self.verticalLayout.addWidget(self.tree)
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.verticalLayout.addWidget(self.buttonBox)

        self.setWindowTitle("Configuration options")
        self.searchBox.setToolTip("Enter setting name to filter list")
        self.tree.headerItem().setText(0, "Setting")
        self.tree.headerItem().setText(1, "Value")


        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)


    def filterTree(self):
        text = str(self.searchBox.text())
        for i in range(self.tree.topLevelItemCount()):
            item = self.tree.topLevelItem(i)
            visible = False
            for j in range(item.childCount()):
                subitem = item.child(j)
                itemText = subitem.text(0)
            if (text.strip() == ""):
                subitem.setHidden(False)
                visible = True
            else:
                hidden = text not in itemText
                item.setHidden(hidden)
                visible = visible or not hidden
            item.setHidden(not visible)
            item.setExpanded(visible and text.strip() != "")

    def fillTree(self):
        self.items = {}
        self.tree.clear()

        generalParams = [("ShowDescription", "Show description panel", True),
                         ("ConfirmDelete", "Ask confirmation before deleting",True),
                         ("ShowToolbar", "Show toolbar", False)]
        icon = QIcon(os.path.dirname(__file__) + "/../../images/geoserver.png")
        generalItem = self._getItem("General", icon, generalParams)
        self.tree.addTopLevelItem(generalItem)

        gsParams = [("SaveCatalogs", "Keep a list of previous catalog connections", True),
                    ("UseRestApi", "Always use REST API for uploads", True),
                    ("DeleteStyle", "Delete style when deleting layer", True),
                    ("Recurse", "Delete resource when deleting layer", True),
                    ("OverwriteGroupLayers", "Overwrite layers when uploading group", True),
                    ("AuthCatalogXMLCacheTime", "AuthCatalog XML cache time in seconds", 180),
                    ]
        try:
            import processing.tools.dataobjects
            gsParams.extend([("PreuploadRasterHook", "Raster pre-upload hook file", ""),
                            ("PreuploadVectorHook", "Vector pre-upload hook file", "")])
        except:
            pass

        gsItem = self._getItem("GeoServer", icon, gsParams)
        self.tree.addTopLevelItem(gsItem)

        self.tree.setColumnWidth(0, 400)

    def _getItem(self, name, icon, params):
        item = QTreeWidgetItem()
        item.setText(0, name)
        item.setIcon(0, icon)
        for param in params:
            paramName, paramDescription, defaultValue = param
            paramName = "/GeoServer/Settings/" + name + "/" + paramName
            subItem = TreeSettingItem(paramName, paramDescription, defaultValue)
            item.addChild(subItem)
        return item


    def accept(self):
        iterator = QTreeWidgetItemIterator(self.tree)
        value = iterator.value()
        while value:
            if hasattr(value, 'saveValue'):
                value.saveValue()
            iterator += 1
            value = iterator.value()
        self.explorer.refreshContent()
        QDialog.accept(self)

class TreeSettingItem(QTreeWidgetItem):

    def __init__(self, name, description, defaultValue):
        QTreeWidgetItem.__init__(self)
        self.name = name
        self.setText(0, description)
        if isinstance(defaultValue,bool):
            self.value = QSettings().value(name, defaultValue=defaultValue, type=bool)
            if self.value:
                self.setCheckState(1, Qt.Checked)
            else:
                self.setCheckState(1, Qt.Unchecked)
        else:
            self.value = QSettings().value(name, defaultValue=defaultValue)
            self.setFlags(self.flags() | Qt.ItemIsEditable)
            self.setText(1, str(self.value))

    def saveValue(self):
        if isinstance(self.value,bool):
            self.value = self.checkState(1) == Qt.Checked
        else:
            self.value = self.text(1)
        QSettings().setValue(self.name, self.value)
