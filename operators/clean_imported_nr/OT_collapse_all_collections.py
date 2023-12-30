import bpy


class COLLECTION_OT_collapse_all_collections(bpy.types.Operator):
    """Collapse all collections in the outliner"""
    bl_idname = 'collection.collapse_all_collections'
    bl_label = 'Collapse All Collections'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        
        areaOverride = context.area
        for area in bpy.context.screen.areas:
            if area.type == 'OUTLINER':
                areaOverride=area

        with bpy.context.temp_override(area=areaOverride):
            bpy.ops.outliner.show_one_level(open=False)
        
        areaOverride.tag_redraw()

        return {'FINISHED'}
