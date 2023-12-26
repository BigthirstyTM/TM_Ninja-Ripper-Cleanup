import bpy

from ...utils.update import AddonUpdate


class PREFERENCES_OT_nrc_do_update(bpy.types.Operator):
    bl_idname = 'preferences.nrc_do_update'
    bl_label = 'NR_Cleanup Do Update'


    def invoke(self, context, event):
        return bpy.types.WindowManager.invoke_props_dialog(self)

    def execute(self, context):
        AddonUpdate.do_update()
        return {'FINISHED'}        

    def draw(self, context):
        layout = self.layout
