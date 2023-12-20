import bpy


class COLLECTION_OT_select_collection_from_nr(bpy.types.Operator):
    bl_idname = "collection.select_collection_from_nr"
    bl_label = "Select Collection From NR"
    bl_options = {'REGISTER', 'UNDO'}

    collection_name: bpy.props.StringProperty(
        name="Collection Name",
        description="Name of the collection to select",
        default=""
    )

    def execute(self, context):
        collection_name = self.collection_name

        # Check if the collection exists
        if collection_name in bpy.data.collections:
            # Clear existing selection
            bpy.ops.object.select_all(action='DESELECT')

            # Set the collection as the active collection
            context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children[collection_name]

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
            bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True))

            # Clean up Mat doubles
            bpy.ops.object.select_all(action='SELECT')
            bpy.data.orphans_purge(do_recursive=True)

            # Separate by material
            bpy.ops.mesh.separate(type='MATERIAL')

            self.report({'INFO'}, f"Joined objects in collection: {collection_name}. Other collections removed.")
        else:
            self.report({'ERROR'}, f"Collection not found: {collection_name}")
        
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)