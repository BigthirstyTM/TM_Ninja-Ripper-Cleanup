import bpy

from . import NRCleanupChildPanel


class VIEW3D_PT_make_route_collection(NRCleanupChildPanel, bpy.types.Panel):
    bl_label = "Make Route Collection"
    
    def draw(self, context):
        layout = self.layout

        col = layout.column()
        col.operator("object.make_route_collection", text="02. Create Route Collection")