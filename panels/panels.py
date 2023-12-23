"""Module internal definitions"""

import bpy


class NRCleanupPanel():
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'NR Cleanup'


class NRCleanupChildPanel(NRCleanupPanel):
    bl_parent_id = 'VIEW3D_PT_nr_cleanup'