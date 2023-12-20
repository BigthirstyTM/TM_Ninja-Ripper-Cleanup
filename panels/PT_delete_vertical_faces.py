import bpy

from . import NRCleanupChildPanel


class VIEW3D_PT_delete_vertical_faces(NRCleanupChildPanel, bpy.types.Panel):
    bl_label = "Delete Vertical Faces"
    
    def draw(self, context):
        layout = self.layout

        col = layout.column()
        col.operator("mesh.delete_vertical_faces", text="03. Delete Vertical Faces")