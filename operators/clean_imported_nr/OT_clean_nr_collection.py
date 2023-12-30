import bpy


class COLLECTION_OT_clean_nr_collection(bpy.types.Operator):
    """Join all objects in the selected collection and remove other collections"""
    bl_idname = 'collection.clean_nr_collection'
    bl_label = 'Clean NR Collection'
    bl_options = {'REGISTER', 'UNDO'}

    flip_vertically: bpy.props.BoolProperty(name='Flip vertically', default=True)
    flip_faces: bpy.props.BoolProperty(name='Flip faces', default=True)

    @classmethod
    def poll(cls, context):
        return (
            context.scene.nrc_props.nr_collection
            and context.mode == 'OBJECT'
        )
    
    def execute(self, context):
        # Get props
        nr_collection:bpy.types.Collection = bpy.context.scene.nrc_props.nr_collection

        # Get collection name
        collection_name = nr_collection.name 

        # Clear existing selection  
        bpy.ops.object.select_all(action='DESELECT')
               
        # Make one object from the collection active
        active_object = bpy.data.collections[collection_name].all_objects[0]
        context.view_layer.objects.active = active_object

        # Select all objects in the collection
        for obj in bpy.data.collections[collection_name].all_objects:
            obj.select_set(True)

        # Join selected objects
        bpy.ops.object.join()

        # Remove all other collections
        for collection in bpy.data.collections:
            if collection.name != collection_name:
                bpy.data.collections.remove(collection)

        # Mirror map on Z Global
        if self.flip_vertically:        
            bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True))

        if self.flip_faces:
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.flip_normals()
            bpy.ops.object.editmode_toggle()

        # Separate by material
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.mesh.separate(type='MATERIAL')

        self.report({'INFO'}, f'Joined objects in collection: "{collection_name}". Other collections removed.')
        
        bpy.data.orphans_purge(do_recursive=True)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)