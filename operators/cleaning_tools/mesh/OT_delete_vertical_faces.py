import bpy
import bmesh
from mathutils import Vector
from math import radians, sin


class MESH_OT_delete_vertical_faces(bpy.types.Operator):
    """Delete the vertical faces in the active selection"""
    bl_idname = 'mesh.delete_vertical_faces'
    bl_label = 'Delete Vertical Faces'
    bl_options = {'REGISTER', 'UNDO'}
    
    in_world_space: bpy.props.BoolProperty(name='World space', default=False)
    threshold: bpy.props.FloatProperty(
        name='Threshold',
        min=radians(0.0),
        max=radians(90.0),
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
        vec_up = Vector((0.0, 0.0, 1.0))                
        for obj in context.objects_in_mode:
            # Get the mesh data
            mesh = obj.data
            # Create a bew bmesh      
            bm = bmesh.from_edit_mesh(mesh)
            # Cancel the obj rotation matrix
            if self.in_world_space:
                bmesh.ops.transform(bm, matrix=obj.matrix_world.to_3x3().inverted(), verts=bm.verts)
            # Selecting vertical faces from selected faces
            selected_faces = [f for f in bm.faces if f.select]
            vertical_faces = [f for f in selected_faces if abs(f.normal.dot(vec_up)) <= sin(self.threshold)]
            # Delete vertical faces
            bmesh.ops.delete(bm, geom=vertical_faces, context='FACES')
            # Restore the mesh rotation
            if self.in_world_space:
                bmesh.ops.transform(bm, matrix=obj.matrix_world.to_3x3(), verts=bm.verts)
            # Write the bmesh back to the mesh
            bmesh.update_edit_mesh(mesh)
            bm.free()
            self.report({'INFO'}, f'Deleted {len(vertical_faces)} faces in {obj.name}')
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, 'in_world_space')
        layout.prop(self, 'threshold')