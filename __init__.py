bl_info = {
    "name": "PROJNAME",
    "description": "PROJdesc",
    "author": "Samuel Bernou",
    "version": (0, 1, 0),
    "blender": (2, 93, 0),
    "location": "View3D",
    "warning": "",
    "doc_url": "https://github.com/Pullusb/PROJ_name",
    "category": "Object" }

from . import properties
from . import preferences
from . import ops_power
from . import panels
# from . import keymaps

import bpy


def register():
    if bpy.app.background:
        return

    properties.register()
    preferences.register()
    ops_power.register()
    panels.register()
    # keymaps.register()

def unregister():
    if bpy.app.background:
        return

    # keymaps.unregister()
    panels.unregister()
    ops_power.unregister()
    preferences.unregister()
    properties.unregister()


if __name__ == "__main__":
    register()
