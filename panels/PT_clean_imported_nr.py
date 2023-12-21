import bpy

from .panels import NRCleanupChildPanel
from ..operators.OT_select_collection_from_nr import COLLECTION_OT_select_collection_from_nr
from ..operators.OT_make_route_collection import OBJECT_OT_make_route_collection

class VIEW3D_PT_clean_imported_nr(NRCleanupChildPanel, bpy.types.Panel):
    bl_label = "Clean Imported NR"

    def draw(self, context):
        layout = self.layout

        nrc_props = bpy.context.scene.nrc_props

        col = layout.column()
        col.prop(nrc_props, "nr_collection", text="Map collection")
        col.operator(COLLECTION_OT_select_collection_from_nr.bl_idname, text="01. Select Map Collection")

        col = layout.column()
        col.operator(OBJECT_OT_make_route_collection.bl_idname, text="02. Create Route Collection")