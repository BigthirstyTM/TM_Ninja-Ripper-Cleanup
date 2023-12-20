import bpy

from . import NRCleanupChildPanel


class VIEW3D_PT_select_collection_from_nr(NRCleanupChildPanel, bpy.types.Panel):
    bl_label = "Select Collection From NR"
    
    def draw(self, context):
        layout = self.layout

        col = layout.column()
        col.prop(bpy.context.scene.nr_cleanup_props, "collection_from_nr", text="Map collection")
        col.operator("collection.select_collection_from_nr", text="01. Select Map Collection")