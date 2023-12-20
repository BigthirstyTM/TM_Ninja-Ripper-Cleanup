import bpy


class OBJECT_OT_make_route_collection(bpy.types.Operator):
    bl_idname = "object.make_route_collection"
    bl_label = "Make Route Collection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        cleaned_route_collection = bpy.data.collections.get("Cleaned Route")
        if not cleaned_route_collection:
            cleaned_route_collection = bpy.data.collections.new("Cleaned Route")
            bpy.context.scene.collection.children.link(cleaned_route_collection)

        selected_objects = bpy.context.selected_objects
        for obj in selected_objects:
            cleaned_route_collection.objects.link(obj)

        bpy.ops.object.select_all(action='DESELECT')

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
