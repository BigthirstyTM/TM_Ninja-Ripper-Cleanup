import bpy
import bmesh
from mathutils import Vector
from math import radians, sin


class OBJECT_OT_delete_vertical_faces(bpy.types.Operator):
    """Delete the vertical faces in local/world space for selected meshes"""
    bl_idname = 'object.delete_vertical_faces'
    bl_label = 'Delete Vertical Faces'
    bl_options = {'REGISTER', 'UNDO'}
    
    in_world_space: bpy.props.BoolProperty(name='World space', default=False)
    threshold: bpy.props.FloatProperty(
        name='Threshold',
        min=radians(0.0),
        max=radians(89.0),
        step=10,
        default=radians(1.0),
        precision=3,
        subtype='ANGLE',
        unit='ROTATION',
        description='Maximum angle to consider as vertical',
    )

    @classmethod
    def poll(cls, context):
        return (
            context.mode == 'OBJECT'
            and context.object is not None
            and context.object.type == 'MESH'
            and len(context.selected_objects) > 0
        )
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)
    
    def execute(self, context):
        vec_up = Vector((0.0, 0.0, 1.0))                
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                # Get the mesh data
                mesh = obj.data
                # Create a bew bmesh
                bm = bmesh.new()
                bm.from_mesh(mesh)
                # Cancel the obj rotation matrix
                if self.in_world_space:
                    bmesh.ops.transform(bm, matrix=obj.matrix_world.to_3x3().inverted(), verts=bm.verts)
                # Selecting vertical faces
                vertical_faces = [f for f in bm.faces if abs(f.normal.dot(vec_up)) <= sin(self.threshold)]
                # Delete vertical faces
                bmesh.ops.delete(bm, geom=vertical_faces, context='FACES')      
                # Restore the mesh rotation
                if self.in_world_space:
                    bmesh.ops.transform(bm, matrix=obj.matrix_world.to_3x3(), verts=bm.verts)
                # Write the bmesh back to the mesh
                bm.to_mesh(mesh)
                mesh.update()
                bm.free()
                self.report({'INFO'}, f'Deleted {len(vertical_faces)} faces in {obj.name}')
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, 'in_world_space')
        layout.prop(self, 'threshold')