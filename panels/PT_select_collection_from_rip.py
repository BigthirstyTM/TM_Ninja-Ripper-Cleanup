import bpy

from . import NRCleanupPanel


class VIEW3D_PT_nr_cleanup(NRCleanupPanel, bpy.types.Panel):
    bl_idname = "PT_nr_cleanup"
    bl_label = "Ninja Ripped Map Cleanup"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("collection.select_collection_from_nr", text="01. Select Map Collection")
        row = layout.row()
        row.operator("object.make_route_collection", text="02. Create Route Collection")
        row = layout.row()
        row.operator("mesh.delete_vertical_faces", text="03. Delete Vertical Faces")