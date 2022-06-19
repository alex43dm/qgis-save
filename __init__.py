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
from platform import system
from os import path, makedirs
from datetime import datetime

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
        image_dir = path.dirname(self.iface.activeLayer().dataProvider().dataSourceUri())

        if not path.exists(image_dir):
            if system() == 'Linux':
                image_dir = '/mnt/media/QGIS'
            elif system() == 'Windows':
                image_dir = 'C:\\Users\\USER'

        if system() == 'Linux':
            image_dir = image_dir + '/report/'
        elif system() == 'Windows':
            image_dir = image_dir + '\\report\\'

        if not path.exists(image_dir):
            makedirs(image_dir)

        image_file = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.png'
        self.iface.mapCanvas().saveAsImage(image_dir + image_file)
#        QMessageBox.information(None, 'Save plugin', 'Saveed as:'+image_file)
