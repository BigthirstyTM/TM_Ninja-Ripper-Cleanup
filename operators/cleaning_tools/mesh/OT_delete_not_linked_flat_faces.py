import bpy
import bmesh
from math import radians


class MESH_OT_delete_not_linked_flat_faces(bpy.types.Operator):
    """Delete the not linked flat faces from the active selection"""
    bl_idname = 'mesh.delete_not_linked_flat_faces'
    bl_label = 'Delete Not Linked Flat Faces'
    bl_options = {'REGISTER', 'UNDO'}
    
    sharpness: bpy.props.FloatProperty(
        name='Sharpness',
        min=radians(0.0),
        max=radians(179.0),
        step=10,
        default=radians(1.0),
        precision=3,
        subtype='ANGLE',
        unit='ROTATION',
        description='Maximum angle to consider as flat',
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
        objects = context.objects_in_mode

        # Extend selection to linked flat faces
        bpy.ops.mesh.faces_select_linked_flat(sharpness=self.sharpness)
        for obj in objects:
            obj.update_from_editmode()
        linked_flat_per_obj = [[f.index for f in obj.data.polygons if f.select] for obj in objects]

        # Extend selection to linked faces
        bpy.ops.mesh.select_linked()
        for obj in objects:
            obj.update_from_editmode()
        

        for i, obj in enumerate(objects):
            # Get linked flat faces
            linked_flat_faces = linked_flat_per_obj[i]

            # Create bmesh
            mesh = obj.data
            bm = bmesh.from_edit_mesh(mesh)
            bm.faces.ensure_lookup_table()

            # Deselect linked flat faces
            for f in linked_flat_faces:
                bm.faces[f].select = False

            # List not linked flat faces
            not_linked_flat_faces = [f for f in bm.faces if f.select]
   
            # Delete not linked flat faces
            bmesh.ops.delete(bm, geom=not_linked_flat_faces, context='FACES')

            # Write the bmesh back to the mesh
            bmesh.update_edit_mesh(mesh)
            bm.free()

            self.report({'INFO'}, f'Deleted {len(not_linked_flat_faces)} faces in {obj.name}')

        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        layout.label(text='Does not delete unconnected geometry.', icon='QUESTION')
        layout.prop(self, 'sharpness')