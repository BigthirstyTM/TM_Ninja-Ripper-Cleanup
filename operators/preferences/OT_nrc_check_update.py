import bpy

from ...utils.update import AddonUpdate


class PREFERENCES_OT_nrc_check_update(bpy.types.Operator):
    bl_idname = 'preferences.nrc_check_update'
    bl_label = 'NR_Cleanup Check Update'

    def execute(self, context):
        AddonUpdate.check_for_new_release()

        if AddonUpdate.can_update:
            self.report({'INFO'}, 'NR_Cleanup update available !')
        else:
            self.report({'INFO'}, 'No update available.')

        return {'FINISHED'}        

