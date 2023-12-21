"""Expose subclasses to be registered"""

# Private
from .operators import MaterialSelection as _MaterialSelection
from .operators import MATERIAL_UL_material_selection as _MATERIAL_UL_material_selection
# Public
from .OT_delete_by_materials import MESH_OT_delete_by_materials
from .OT_delete_vertical_faces import MESH_OT_delete_vertical_faces
from .OT_make_route_collection import OBJECT_OT_make_route_collection
from .OT_select_collection_from_nr import COLLECTION_OT_select_collection_from_nr


_classes = (
    _MaterialSelection,
    _MATERIAL_UL_material_selection,
    MESH_OT_delete_by_materials,
    MESH_OT_delete_vertical_faces,
    OBJECT_OT_make_route_collection,
    COLLECTION_OT_select_collection_from_nr,
)

def register_classes():
    import bpy
    for cls in _classes:
        bpy.utils.register_class(cls)

def unregister_classes():
    import bpy
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)