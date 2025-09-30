# SPDX-License-Identifier: GPL-2.0-or-later

bl_info = {
    "name": "PROJNAME",
    "description": "PROJdesc",
    "author": "Samuel Bernou",
    "version": (0, 1, 0),
    "blender": (4, 5, 0),
    "location": "View3D",
    "warning": "",
    "doc_url": "https://github.com/Pullusb/REPONAME",
    "tracker_url": "https://github.com/Pullusb/REPONAME/issues",
    "category": "Object"
}

import bpy
from . import properties
from . import preferences
from . import operators
from . import ui
from . import keymaps

mods = (
    properties,
    preferences,
    operators,
    ui,
    keymaps,
)

def register():
    ## if addon is only keymap based for example
    # if bpy.app.background:
    #     return
    
    for mod in mods:
        mod.register()

def unregister():
    # if bpy.app.background:
    #     return
    
    for mod in reversed(mods):
        mod.unregister()

if __name__ == "__main__":
    register()
