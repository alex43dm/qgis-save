# QGIS Save Plugin

To save working layers as image

## Why?

For fast woring

## How to use it?

1. Create a new python plugin directory
  * e.g. Linux ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/qgis-save
  * e.g. Windows C:\Users\USER\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\qgis-save
2. Copy metadata.txt and __init__.py to that directory
3. Start QGIS and enable the plugin (menu Plugins > Manager and Install Plugins...)

Now you should see a "Save!" button in your "Plugins" toolbar (make sure it is enabled in menu Settings > Toolbars > Plugins).

The next step is path for save data:
adding your own path to __init__.py:36
        if platform.system() == 'Linux':
            image_dir = '/mnt/media/QGIS/report/'
        elif platform.system() == 'Windows':
            image_dir = 'C:\\Users\\USER\\report\\'

and to change the bind key and __init__.py:28:
        self.action.setShortcut('F10')

Have fun!
