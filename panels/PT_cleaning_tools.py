import bpy

from .panels import NRCleanupChildPanel
from ..operators.OT_delete_vertical_faces import MESH_OT_delete_vertical_faces
from ..operators.OT_delete_by_materials import MESH_OT_delete_by_materials


class VIEW3D_PT_cleaning_tools(NRCleanupChildPanel, bpy.types.Panel):
    bl_label = "Cleaning Tools"

    def draw(self, context):
        layout = self.layout

        col = layout.column()
        col.operator(MESH_OT_delete_vertical_faces.bl_idname, text="Delete vertical faces")
        col.operator(MESH_OT_delete_by_materials.bl_idname, text="Delete faces by material")