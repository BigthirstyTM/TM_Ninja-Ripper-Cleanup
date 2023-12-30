"""Expose operator subclasses and (un)register function."""

# clean_imported_nr
from .clean_imported_nr.OT_clean_nr_collection import (
    COLLECTION_OT_clean_nr_collection,
)
from .clean_imported_nr.OT_collapse_all_collections import (
    COLLECTION_OT_collapse_all_collections,
)
from .clean_imported_nr.OT_make_route_collection import (
    OBJECT_OT_make_route_collection,
)

# cleaning_tools
from .cleaning_tools.object.OT_delete_by_materials import (
    MaterialSelection as _MaterialSelection,
    MATERIAL_UL_material_selection as _MATERIAL_UL_material_selection,
    OBJECT_OT_delete_faces_by_material,
)
from .cleaning_tools.object.OT_delete_vertical_faces import (
    OBJECT_OT_delete_vertical_faces,
)
from .cleaning_tools.mesh.OT_delete_not_linked_flat_faces import (
    MESH_OT_delete_not_linked_flat_faces,
)
from .cleaning_tools.mesh.OT_delete_vertical_faces import (
    MESH_OT_delete_vertical_faces,
)

# preferences
from .preferences.OT_nrc_check_update import (
    PREFERENCES_OT_nrc_check_update,
)
from .preferences.OT_nrc_do_update import (
    PREFERENCES_OT_nrc_do_update,
)

# ui
from .ui.OT_message_popup import (
    UI_OT_message_popup,
)
from .ui.OT_open_url import (
    UI_OT_open_url,
)


_classes = (
    # Props and UIList must be registered before operators
    _MaterialSelection,
    _MATERIAL_UL_material_selection,
    COLLECTION_OT_clean_nr_collection,
    COLLECTION_OT_collapse_all_collections,
    OBJECT_OT_make_route_collection,
    OBJECT_OT_delete_faces_by_material,
    OBJECT_OT_delete_vertical_faces,
    MESH_OT_delete_not_linked_flat_faces,
    MESH_OT_delete_vertical_faces,
    PREFERENCES_OT_nrc_check_update,
    PREFERENCES_OT_nrc_do_update,
    UI_OT_message_popup,
    UI_OT_open_url,
)

def register_classes():
    import bpy
    for cls in _classes:
        bpy.utils.register_class(cls)

def unregister_classes():
    import bpy
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)