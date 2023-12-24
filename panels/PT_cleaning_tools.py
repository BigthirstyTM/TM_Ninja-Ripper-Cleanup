import bpy

from .panels import NRCleanupChildPanel

from ..operators import (
    WINDOW_OT_message_popup,
    MESH_OT_delete_vertical_faces,
    MESH_OT_delete_faces_by_material,
    MESH_OT_delete_not_linked_flat_faces,
)


class VIEW3D_PT_cleaning_tools(NRCleanupChildPanel, bpy.types.Panel):
    bl_label = 'Cleaning Tools'
    bl_options = {'HEADER_LAYOUT_EXPAND'}

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        row = col.row()
        if context.mode == 'OBJECT':
            row.label(text='Object mode', icon='OBJECT_DATAMODE')
            op = row.operator(WINDOW_OT_message_popup.bl_idname, text='', icon='QUESTION')
            op.message = \
                'hey is this working ?\n' \
                + 'OK FINE'
            col.operator(MESH_OT_delete_vertical_faces.bl_idname, text="Delete vertical faces")
            col.operator(MESH_OT_delete_faces_by_material.bl_idname, text="Delete faces by material")
        elif context.mode == 'EDIT_MESH':
            row.label(text='Edit mode', icon='EDITMODE_HLT')
            op = row.operator(WINDOW_OT_message_popup.bl_idname, text='', icon='QUESTION')
            op.message = \
                'hey is this working ?\n' \
                + 'OK FINE'
            col.operator(MESH_OT_delete_not_linked_flat_faces.bl_idname, text="Delete not linked flat faces")
        else:
            row.label(text='Go in object or edit mode', icon='QUESTION')