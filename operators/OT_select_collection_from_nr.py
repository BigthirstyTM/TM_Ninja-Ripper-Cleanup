import bpy


class COLLECTION_OT_select_collection_from_nr(bpy.types.Operator):
    bl_idname = "collection.select_collection_from_nr"
    bl_label = "Select Collection From NR"
    bl_options = {'REGISTER', 'UNDO'}

    flip_meshes: bpy.props.BoolProperty(name="Flip meshes", default=True)

    @classmethod
    def poll(cls, context):
        return bpy.context.scene.nrc_props.nr_collection
    
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
        if self.flip_meshes:        
            bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True))

        # Clean up Mat doubles
        bpy.ops.object.select_all(action='SELECT')
        bpy.data.orphans_purge(do_recursive=True)

        # Separate by material
        bpy.ops.mesh.separate(type='MATERIAL')

        self.report({'INFO'}, f"Joined objects in collection: {collection_name}. Other collections removed.")
        #else:
            #self.report({'ERROR'}, f"Collection not found: {collection_name}")
        
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)