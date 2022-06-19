#-----------------------------------------------------------
# Copyright (C) 2022 Oleksandr Dmytrenko
#-----------------------------------------------------------
# Licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#---------------------------------------------------------------------

from PyQt5.QtWidgets import QAction, QMessageBox
from datetime import datetime
import platform
import qgis

def classFactory(iface):
    return SavePlugin(iface)


class SavePlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.action = QAction('Save!', self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.action.setShortcut('F10')
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action

    def run(self):
        if platform.system() == 'Linux':
            image_dir = '/mnt/media/QGIS/report/'
        elif platform.system() == 'Windows':
            image_dir = 'C:\\Users\\USER\\report\\'
        image_file = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.png'
        qgis.utils.iface.mapCanvas().saveAsImage(image_dir + image_file)
        QMessageBox.information(None, 'Save plugin', 'Saveed as:'+image_file)
