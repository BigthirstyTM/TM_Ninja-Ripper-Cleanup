import bpy
import bmesh
from mathutils import Vector
from math import radians, sin


class MESH_OT_delete_not_linked_flat_faces(bpy.types.Operator):
    """Delete the not linked flat faces from the active selection"""
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
            and context.edit_object is not None
            and context.edit_object.type == 'MESH'
        )
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)
    
    def execute(self, context):
        for obj in context.objects_in_mode:
            # Get the mesh data
            mesh = obj.data
            # Create a bew bmesh      
            bm = bmesh.from_edit_mesh(mesh)

            
            selected_faces = [f for f in bm.faces if f.select]

            # Delete not linked flat faces
            bmesh.ops.delete(bm, geom=selected_faces, context='FACES')

            # Write the bmesh back to the mesh
            bmesh.update_edit_mesh(mesh)
            bm.free()
            self.report({'INFO'}, f'Deleted {len(selected_faces)} faces in {obj.name}')
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, 'max_flat_angle')