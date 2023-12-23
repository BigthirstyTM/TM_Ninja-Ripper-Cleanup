"""Expose operrator subclasses to be registered"""

# Private
from .operators import MaterialSelection as _MaterialSelection
from .operators import MATERIAL_UL_material_selection as _MATERIAL_UL_material_selection
# Public
from .clean_imported_nr.OT_select_collection_from_nr import COLLECTION_OT_select_collection_from_nr
from .clean_imported_nr.OT_make_route_collection import OBJECT_OT_make_route_collection
from .cleaning_tools.OT_delete_by_materials import MESH_OT_delete_by_materials
from .cleaning_tools.OT_delete_not_linked_flat_faces import MESH_OT_delete_not_linked_flat_faces
from .cleaning_tools.OT_delete_vertical_faces import MESH_OT_delete_vertical_faces
from .misc.OT_message_popup import WINDOW_OT_message_popup 


_classes = (
    # Props and UIList must be registered before operators
    _MaterialSelection,
    _MATERIAL_UL_material_selection,
    COLLECTION_OT_select_collection_from_nr,
    OBJECT_OT_make_route_collection,
    MESH_OT_delete_by_materials,
    MESH_OT_delete_not_linked_flat_faces,
    MESH_OT_delete_vertical_faces,
    WINDOW_OT_message_popup,
)

def register_classes():
    import bpy
    for cls in _classes:
        bpy.utils.register_class(cls)

def unregister_classes():
    import bpy
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)