"""Expose panel subclasses to be registered"""

# Private

# Public
from .PT_clean_imported_nr import VIEW3D_PT_clean_imported_nr
from .PT_cleaning_tools import VIEW3D_PT_cleaning_tools
from .PT_nr_cleanup import VIEW3D_PT_nr_cleanup


_classes = (
    # Register order is important for panels :
    # - Parents must be registered before childs
    # - Panels registered first will appear above other panels
    VIEW3D_PT_nr_cleanup,
    VIEW3D_PT_clean_imported_nr,
    VIEW3D_PT_cleaning_tools,
)

def register_classes():
    import bpy
    for cls in _classes:
        bpy.utils.register_class(cls)

def unregister_classes():
    import bpy
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)
