import bpy

from .panels import NRCleanupPanel


class VIEW3D_PT_nr_cleanup(NRCleanupPanel, bpy.types.Panel):
    bl_label = 'Ninja Ripped Map Cleanup'

    def draw(self, context):
        layout = self.layout