bl_info = {
    "name": "NR_Cleanup",
    "author": "Bigthirsty & Skyrow",
    "version": (0, 4, 0), #<major>.<minor>.<patch>
    "blender": (3, 6, 0),
    "location": "3D Viewport > Sidebar > NR Cleanup",
    "description": "Cleans up NinjaRipped trackmania2020 maps to driving surfaces only",
    "category": "Trackmania",
}

ROOT_PATH = __file__
LOG_DEBUG = True


import bpy

from . import properties
from . import operators
from . import panels
from .utils import events
from .utils import logs

log = logs.get_logger(__name__)


# Register addon
def register():
    logs.start_logging()

    # Register classes
    properties.register_classes()
    operators.register_classes()
    panels.register_classes()

    # Extend blender data
    bpy.types.Scene.nrc_props = bpy.props.PointerProperty(type=properties.NRCleanup_Props)

    events.start_listening()


# Unregister addon
def unregister():
    events.stop_listening()

    # Unregister classes
    panels.unregister_classes()
    operators.unregister_classes()
    properties.unregister_classes()

    logs.stop_logging()