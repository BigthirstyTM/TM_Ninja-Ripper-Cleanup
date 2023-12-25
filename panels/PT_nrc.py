import bpy

from . import _NRCPanel
from ..utils.update import AddonUpdate
from ..operators import (
    PREFERENCES_OT_nrc_check_update,
    PREFERENCES_OT_nrc_do_update,
)

class VIEW3D_PT_nr_cleanup(_NRCPanel, bpy.types.Panel):
    bl_label = 'Ninja Ripped Map Cleanup'

    def draw(self, context):
        layout = self.layout
        row = layout.row()

        if AddonUpdate.can_update:
            row.operator(PREFERENCES_OT_nrc_do_update.bl_idname)
        else:
            row.operator(PREFERENCES_OT_nrc_check_update.bl_idname)
