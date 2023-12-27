import bpy

from . import _NRCChildPanel

from ..operators import (
    UI_OT_message_popup,
    OBJECT_OT_delete_vertical_faces,
    OBJECT_OT_delete_faces_by_material,
    MESH_OT_delete_not_linked_flat_faces,
    MESH_OT_delete_vertical_faces,
)


class VIEW3D_PT_cleaning_tools(_NRCChildPanel, bpy.types.Panel):
    bl_label = 'Cleaning Tools'
    bl_options = {'HEADER_LAYOUT_EXPAND'}

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        row = col.row()

        # Object Mode tools
        if context.mode == 'OBJECT':
            row.label(text='Object Mode', icon='OBJECT_DATAMODE')
            op = row.operator(UI_OT_message_popup.bl_idname, text='', icon='QUESTION')
            op.title = 'Help'
            op.message = \
                'These tools are available only in object mode,\n' \
                + 'They can be used on multiple selected objects.\n' \
                + 'Switch to Edit Mode for other tools.'
            col.operator(OBJECT_OT_delete_vertical_faces.bl_idname, text="Delete vertical faces")
            col.operator(OBJECT_OT_delete_faces_by_material.bl_idname, text="Delete faces by material")

        # Edit Mode tools
        elif context.mode == 'EDIT_MESH':
            row.label(text='Edit Mode', icon='EDITMODE_HLT')
            op = row.operator(UI_OT_message_popup.bl_idname, text='', icon='QUESTION')
            op.title = 'Help'
            op.message = \
                'These tools are available only in Edit Mode,\n' \
                + 'They can be used on multiple objects in Edit Mode,\n' \
                + 'And they use the active selection to work with.'
            col.operator(MESH_OT_delete_vertical_faces.bl_idname, text='Delete vertical faces')
            col.operator(MESH_OT_delete_not_linked_flat_faces.bl_idname, text="Delete not linked flat faces")
        
        # Other Modes
        else:
            row.label(text='No tool in the current mode.', icon='QUESTION')