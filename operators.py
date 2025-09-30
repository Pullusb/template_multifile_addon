# SPDX-License-Identifier: GPL-2.0-or-later

import bpy
from bpy.types import Operator
from .preferences import get_addon_prefs


class PROJ_OT_ops_name(Operator):
    bl_idname = "catname.ops_name"
    bl_label = "Ops Name"
    bl_description = "Description that shows in blender tooltips"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        if not context.object:
            self.report({'ERROR'}, 'No active object')
            return {"CANCELLED"}
        print('Super simple ops !')        
        return {"FINISHED"}


class PROJ_OT_ops_name_modal(Operator):
    bl_idname = "catname.ops_name_modal"
    bl_label = "Opsname Modal"
    bl_description = "Description that shows in blender tooltips"
    bl_options = {"REGISTER", "UNDO"} # INTERNAL

    @classmethod
    def poll(cls, context):
        return context.object and context.object.type == 'MESH'

    shift : bpy.props.BoolProperty(name='Shifter', default=False)

    def invoke(self, context, event):
        # if context.mode not in ('PAINT_GPENCIL', 'EDIT_GPENCIL'):
        #     return {"CANCELLED"}
        self.shift = event.shift

        ## for a modal
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
        # return self.execute(context)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "shift")

    def modal(self, context, event):
        if event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            self.execute(context)
            return {"FINISHED"}

        if event.type == 'RIGHTMOUSE':
            print('Abort')
            return {"CANCELLED"}

        # return {'PASS_THROUGH'}
        return {"RUNNING_MODAL"}

    def execute(self, context):
        print('What a click !')        
        return {"FINISHED"}

classes=(
PROJ_OT_ops_name,
PROJ_OT_ops_name_modal,
)

def register(): 
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)