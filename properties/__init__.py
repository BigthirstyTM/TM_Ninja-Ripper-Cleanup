"""Expose property subclasses to be registered"""

# Private

# Public
from .properties import NRCleanup_Props


_classes = (
    NRCleanup_Props,
)

def register_classes():
    import bpy
    for cls in _classes:
        bpy.utils.register_class(cls)

def unregister_classes():
    import bpy
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)
