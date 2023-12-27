import bpy

from . import _NRCPanel
from .. import bl_info
from ..utils.logs import html_logs_filepath
from ..utils.update import AddonUpdate
from ..operators import (
    UI_OT_open_url,
    PREFERENCES_OT_nrc_check_update,
    PREFERENCES_OT_nrc_do_update,
)

class VIEW3D_PT_nr_cleanup(_NRCPanel, bpy.types.Panel):
    bl_label = 'Ninja Ripped Map Cleanup'

    def draw(self, context):
        current_version_str = f'v{".".join(str(i) for i in bl_info["version"])}'
        new_version_str = f'v{".".join(str(i) for i in AddonUpdate.latest_addon_version)}'
        
        layout = self.layout      
        row = layout.row(align=True)
        if AddonUpdate.update_successfull:
            row.label(text='Blender must be restarted !', icon ='FILE_SCRIPT')
        else:
            row.label(text=f'{current_version_str}', icon='FILE_SCRIPT')
            if AddonUpdate.can_update:
                row.alert = True
                row.operator(PREFERENCES_OT_nrc_do_update.bl_idname, text=f'{new_version_str}', icon='IMPORT')
                row.alert = False
            else:
                row.operator(PREFERENCES_OT_nrc_check_update.bl_idname, text='', icon='FILE_REFRESH')
        
        row.operator(UI_OT_open_url.bl_idname, text='', icon='URL').url = 'https://github.com/BigthirstyTM/TM_Ninja-Ripper-Cleanup.git'
        row.operator(UI_OT_open_url.bl_idname, text='', icon='FILE_TEXT').url = str(html_logs_filepath)

