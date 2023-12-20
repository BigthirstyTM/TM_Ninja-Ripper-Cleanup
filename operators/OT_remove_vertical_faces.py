import bpy

from ..utils.math import (
    cross,
    length
)


class MESH_OT_delete_vertical_faces(bpy.types.Operator):
    bl_idname = 'mesh.delete_vertical_faces'
    bl_label = 'Delete Vertical Faces'
    bl_options = {'REGISTER', 'UNDO'}
    
    apply_rotation: bpy.props.BoolProperty(name='Apply rotation', default=False)
    
    @classmethod
    def poll(cls, context):
        return context.object.type == 'MESH'
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)
    
    def execute(self, context):                
        up_vector = [0., 0., 1.]
        
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
        bpy.ops.object.mode_set(mode='OBJECT')
        
        # Apply rotation if requested
        if self.apply_rotation:
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=False) 
               
        # Mesh faces
        faces = [f for f in context.object.data.polygons]
        
        # Selecting vertical faces
        for f in faces:
            normal_x_up = cross(f.normal, up_vector)
            # If the norm of cross profuct is 1., then the face is vertical    
            if (length(normal_x_up) == 1.):
                f.select = True
            else:
                f.select = False
                
        # Deleting selected faces
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.delete(type='FACE')
        bpy.ops.object.mode_set(mode='OBJECT')
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        layout.label(text='It will delete vertical face in the local space.', icon='INFO')
        layout.label(text='If your object has a transformation of its rotation,')
        layout.label(text='You may want to apply it first')
        layout.prop(self, 'apply_rotation')