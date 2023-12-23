import bpy
import bmesh
from mathutils import Vector
from math import radians, sin


class MESH_OT_delete_not_linked_flat_faces(bpy.types.Operator):
    """Delete the not linked flat to horizontal faces in local/world space for selected meshes"""
    bl_idname = 'mesh.delete_not_linked_flat_faces'
    bl_label = 'Delete Not Linked Flat Faces'
    bl_options = {'REGISTER', 'UNDO'}
    
    max_flat_angle: bpy.props.FloatProperty(
        name='Maximum angle',
        min=radians(0.0),
        max=radians(89.0),
        step=10,
        default=radians(1.0),
        precision=3,
        subtype='ANGLE',
        unit='ROTATION',
    )
    
    @classmethod
    def poll(cls, context):
        return (
            context.mode == 'EDIT_MESH'
        )
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)
    
    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, 'max_flat_angle')
        layout.label(text='This is only a placeholder and currently does nothing')