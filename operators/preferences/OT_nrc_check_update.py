import bpy
import threading

from ...utils.update import AddonUpdate


class PREFERENCES_OT_nrc_check_update(bpy.types.Operator):
    bl_idname = 'preferences.nrc_check_update'
    bl_label = 'NR_Cleanup Check Update'

    def execute(self, context):
        AddonUpdate.check_for_new_release()

        if AddonUpdate.can_update:
            self.report({'INFO'}, f'NR_Cleanup  update available !')
        elif AddonUpdate.new_addon_available and not AddonUpdate.current_blender_supported:
            self.report({'ERROR'},f'A new version is available but blender version is too old ! Minimal is {AddonUpdate.latest_minimal_blender_version}).')
        else:
            self.report({'INFO'}, 'No update available.')

        return {'FINISHED'}        

