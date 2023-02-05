# SPDX-License-Identifier: GPL-2.0-or-later

import bpy
from bpy.props import (FloatProperty,
                        BoolProperty,
                        EnumProperty,
                        StringProperty,
                        IntProperty,
                        PointerProperty)

## update on prop change
def update_prop(self, context):
    print('Update trigger')
    
class PROJ_PGT_settings(bpy.types.PropertyGroup) :
    ## HIDDEN to hide the animatable dot thing
    stringprop : StringProperty(
        name="str prop",
        description="",
        default="")# update=None, get=None, set=None
    
    boolprop : BoolProperty(
        name="bool prop",
        description="",
        default=False, options={'HIDDEN'}) # options={'ANIMATABLE'},subtype='NONE', update=None, get=None, set=None

    IntProperty : IntProperty(
        name="int prop", description="", default=25, min=1, max=2**31-1, soft_min=1, soft_max=2**31-1, step=1, options={'HIDDEN'})#, subtype='PIXEL'

    ## property with update on change
    edit_lines_opacity : FloatProperty(
        name="edit lines Opacity", description="Change edit lines opacity for all grease pencils", 
        default=0.5, min=0.0, max=1.0, step=3, precision=2, update=update_prop)

    ## enum (with Icon)
    keyframe_type : EnumProperty(
        name="Keyframe Filter", description="Only jump to defined keyframe type", 
        default='ALL', options={'HIDDEN', 'SKIP_SAVE'},
        items=(
            ('ALL', 'All', '', 0), # 'KEYFRAME'
            ('KEYFRAME', 'Keyframe', '', 'KEYTYPE_KEYFRAME_VEC', 1),
            ('BREAKDOWN', 'Breakdown', '', 'KEYTYPE_BREAKDOWN_VEC', 2),
            ('MOVING_HOLD', 'Moving Hold', '', 'KEYTYPE_MOVING_HOLD_VEC', 3),
            ('EXTREME', 'Extreme', '', 'KEYTYPE_EXTREME_VEC', 4),
            ('JITTER', 'Jitter', '', 'KEYTYPE_JITTER_VEC', 5),
            ))


class MYID_PGT_full_options_settings(bpy.types.PropertyGroup) :
    import sys
    Bool_variable_name : bpy.props.BoolProperty(
        name="", description="", default=False, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None)

    BoolVector_variable_name : bpy.props.BoolVectorProperty(
        name="", description="", default=(False, False, False), options={'ANIMATABLE'}, subtype='NONE', size=3, update=None, get=None, set=None)

    Collection_variable_name : bpy.props.CollectionProperty(
        type=None, name="", description="", options={'ANIMATABLE'})

    Enum_variable_name : bpy.props.EnumProperty(
        items=(
            ('FIRST', 'first element label', 'First element hover description', 0),#include icon name in fourth position
            ('SECOND', 'Second element label', 'second element hover description', 1),
            ),
        name="", description="", default=None, options={'ANIMATABLE'}, update=None, get=None, set=None)

    Float_variable_name : bpy.props.FloatProperty(
        name="", description="", default=0.0, min=sys.float_info.min, max=sys.float_info.max, soft_min=sys.float_info.min, soft_max=sys.float_info.max, step=3, precision=2, options={'ANIMATABLE'}, subtype='NONE', unit='NONE', update=None, get=None, set=None)

    FloatVector_variable_name : bpy.props.FloatVectorProperty(
        name="", description="", default=(0.0, 0.0, 0.0), min=sys.float_info.min, max=sys.float_info.max, soft_min=sys.float_info.min, soft_max=sys.float_info.max, step=3, precision=2, options={'ANIMATABLE'}, subtype='NONE', unit='NONE', size=3, update=None, get=None, set=None)

    Int_variable_name : bpy.props.IntProperty(
        name="", description="", default=0, min=-2**31, max=2**31-1, soft_min=-2**31, soft_max=2**31-1, step=1, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None)

    IntVector_variable_name : bpy.props.IntVectorProperty(
        name="", description="", default=(0, 0, 0), min=-2**31, max=2**31-1, soft_min=-2**31, soft_max=2**31-1, step=1, options={'ANIMATABLE'}, subtype='NONE', size=3, update=None, get=None, set=None)

    String_variable_name : bpy.props.StringProperty(
        name="", description="", default="", maxlen=0, options={'ANIMATABLE'}, subtype='NONE', update=None, get=None, set=None)

    # place at the end of register()
    # bpy.types.Scene.mytoolprops = bpy.props.PointerProperty(type = GP_PG_ToolsSettings)
    # place at the end of unregister()
    # del bpy.types.Scene.mytoolprops


# classes=(
# PROJ_PGT_settings,
# )

def register(): 
    # for cls in classes:
    #     bpy.utils.register_class(cls)
    bpy.utils.register_class(PROJ_PGT_settings)
    bpy.types.Scene.pgroup_name = bpy.props.PointerProperty(type = PROJ_PGT_settings)
    

def unregister():
    # for cls in reversed(classes):
    #     bpy.utils.unregister_class(cls)
    bpy.utils.unregister_class(PROJ_PGT_settings)
    del bpy.types.Scene.pgroup_name