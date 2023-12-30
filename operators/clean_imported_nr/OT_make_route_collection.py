import bpy


class OBJECT_OT_make_route_collection(bpy.types.Operator):
    """Create a new collection with only selected objects (linked-copy)"""
    bl_idname = 'object.make_route_collection'
    bl_label = 'Make Route Collection'
    bl_options = {'REGISTER', 'UNDO'}

    exclude_original_collections: bpy.props.BoolProperty(name='Exclude original collections', default=True)
    hide_original_collections: bpy.props.BoolProperty(name='Hide original collections', default=True)
    unlink_original_objexts: bpy.props.BoolProperty(name='Unlink original objects', default=True)

    @classmethod
    def poll(cls, context):
        return (
            context.selected_objects
            and context.mode == 'OBJECT'
        )
    
    def execute(self, context):
        selected_objects = bpy.context.selected_objects

        # Create a new collection for the selected objects
        cleaned_route_collection = bpy.data.collections.get('Cleaned Route')
        if not cleaned_route_collection:
            cleaned_route_collection = bpy.data.collections.new('Cleaned Route')
            bpy.context.scene.collection.children.link(cleaned_route_collection)

        # Get the original collections of selected objects
        original_collections = set()
        for obj in selected_objects:
            for collection in obj.users_collection:
                original_collections.add(collection)

        # Link the selected objects to the new collection 
        for obj in selected_objects:
            if self.unlink_original_objexts:
                for col in obj.users_collection:
                    col.objects.unlink(obj)
            cleaned_route_collection.objects.link(obj)

        # Exclude all collections and enable only new collection
        for layer_collection in context.view_layer.layer_collection.children:
            if self.exclude_original_collections:
                layer_collection.exclude = True
            if self.hide_original_collections:
                layer_collection.hide_viewport = True
        context.view_layer.layer_collection.children[cleaned_route_collection.name].exclude = False    
        context.view_layer.layer_collection.children[cleaned_route_collection.name].hide_viewport = False    

        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
