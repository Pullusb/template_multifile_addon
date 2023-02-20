# SPDX-License-Identifier: GPL-2.0-or-later

bl_info = {
    "name": "PROJNAME",
    "description": "PROJdesc",
    "author": "Samuel Bernou",
    "version": (0, 1, 0),
    "blender": (3, 5, 0),
    "location": "View3D",
    "warning": "",
    "doc_url": "https://github.com/Pullusb/REPONAME",
    "tracker_url": "https://github.com/Pullusb/REPONAME/issues",
    "category": "Object"
}

import bpy
from . import properties
from . import preferences
from . import ops_power
from . import panels
from . import keymaps

mods = (
    properties,
    preferences,
    ops_power,
    panels,
    keymaps,
)

def register():
    if bpy.app.background:
        return
    
    for mod in mods:
        mod.register()

def unregister():
    if bpy.app.background:
        return
    
    for mod in reversed(mods):
        mod.unregister()

if __name__ == "__main__":
    register()
