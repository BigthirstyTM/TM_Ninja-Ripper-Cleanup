import bpy

from . import _NRCChildPanel

from ..operators import (
    UI_OT_message_popup,
    OBJECT_OT_clean_nr_collection,
    OBJECT_OT_make_route_collection,
)


class VIEW3D_PT_clean_imported_nr(_NRCChildPanel, bpy.types.Panel):
    bl_label = 'Clean Imported NR'
    bl_options = {'HEADER_LAYOUT_EXPAND'}

    def draw(self, context):
        nrc_props = bpy.context.scene.nrc_props
        layout = self.layout
        # Select map collection
        box = layout.box()
        row = box.row()
        row.label(text='01. Select Map Collection')
        op = row.operator(UI_OT_message_popup.bl_idname, text='', icon='QUESTION')
        op.title = 'Help'
        op.message = \
            'hey is this working ?\n' \
            + 'OK FINE'   
        box.prop(nrc_props, 'nr_collection', text='')
        box.operator(OBJECT_OT_clean_nr_collection.bl_idname, text='Clean Map Collection')
        # Create route collection
        box = layout.box()
        row = box.row()
        row.label(text='02. Create Route Collection')
        op = row.operator(UI_OT_message_popup.bl_idname, text='', icon='QUESTION')
        op.title = 'Help'
        op.message = \
            'hey is this working ?\n' \
            + 'OK FINE'   
        box.operator(OBJECT_OT_make_route_collection.bl_idname, text='Create Route Collection')