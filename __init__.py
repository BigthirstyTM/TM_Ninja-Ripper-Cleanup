import bpy

# Note from Skyrow : v0.1.0 changes
# - Packaged addon into multiple files
# - Panels and operators rename

bl_info = {
    "name": "NR_Cleanup",
    "author": "Bigthirsty & Skyrow",
    "version": (0, 1, 0), #<major>.<minor>.<patch>
    "blender": (4, 0, 1),
    "location": "3D Viewport > Sidebar > NR Cleanup",
    "description": "Cleans up NinjaRipped trackmania2020 maps to driving surfaces only",
    "category": "Trackmania",
}


# Import props
from .properties.nr_cleanup_props import NRCleanup_Props
# Import operators
from .operators.OT_select_collection_from_nr import COLLECTION_OT_select_collection_from_nr
from .operators.OT_make_route_collection import OBJECT_OT_make_route_collection
from .operators.OT_delete_vertical_faces import MESH_OT_delete_vertical_faces
# Import panels
from .panels.PT_nr_cleanup import VIEW3D_PT_nr_cleanup
from .panels.PT_select_collection_from_nr import VIEW3D_PT_select_collection_from_nr
from .panels.PT_make_route_collection import VIEW3D_PT_make_route_collection
from .panels.PT_delete_vertical_faces import VIEW3D_PT_delete_vertical_faces


# Define register order
classes = (
    # Props
    NRCleanup_Props,
    # Operators
    COLLECTION_OT_select_collection_from_nr,
    OBJECT_OT_make_route_collection,
    MESH_OT_delete_vertical_faces,
    # Panels (order matters here)
    VIEW3D_PT_nr_cleanup,
    VIEW3D_PT_select_collection_from_nr,
    VIEW3D_PT_make_route_collection,
    VIEW3D_PT_delete_vertical_faces,
)


# Register addon
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.nr_cleanup_props = bpy.props.PointerProperty(type=NRCleanup_Props)

# Unregister addon
def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    

if __name__ == "__main__":
    register()