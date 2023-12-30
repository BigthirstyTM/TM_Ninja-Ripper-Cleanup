import bpy

from . import _NRCChildPanel

from ..operators import (
    UI_OT_message_popup,
    COLLECTION_OT_clean_nr_collection,
    COLLECTION_OT_collapse_all_collections,
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
            '1. Select the collection containing textured meshes\n' \
            + '2. Press the "Clean Map Collection" button\n' \
            + 'It will join all objects inside of the selected collection\n' \
            + 'and then separate it by material.\n' \
            + 'EVERYTHING ELSE IN THE SCENE WILL BE DELETED !'
        row = box.row(align=True)
        row.prop(nrc_props, 'nr_collection', text='')
        row.operator(COLLECTION_OT_collapse_all_collections.bl_idname, text='', icon='FULLSCREEN_EXIT')
        box.operator(COLLECTION_OT_clean_nr_collection.bl_idname, text='Clean Map Collection')
        # Create route collection
        box = layout.box()
        row = box.row()
        row.label(text='02. Create Route Collection')
        op = row.operator(UI_OT_message_popup.bl_idname, text='', icon='QUESTION')
        op.title = 'Help'
        op.message = \
            '1. Select objects that are part of the route\n' \
            + '2. Press the "Create Route Collection" button\n' \
            + 'It will create a new collection and link the selected objects.'
        box.operator(OBJECT_OT_make_route_collection.bl_idname, text='Create Route Collection')