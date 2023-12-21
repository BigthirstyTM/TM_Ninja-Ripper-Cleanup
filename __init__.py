import os
import bpy

bl_info = {
    "name": "NR_Cleanup",
    "author": "Bigthirsty & Skyrow",
    "version": (0, 1, 0), #<major>.<minor>.<patch>
    "blender": (4, 0, 1),
    "location": "3D Viewport > Sidebar > NR Cleanup",
    "description": "Cleans up NinjaRipped trackmania2020 maps to driving surfaces only",
    "category": "Trackmania",
}

LOG_DEBUG = True

ADDON_DIRNAME = os.path.dirname(__file__)

# Third party modules
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
    bpy.types.Scene.nr_cleanup_props = bpy.props.PointerProperty(type=properties.NRCleanup_Props)

    events.start_listening()


# Unregister addon
def unregister():
    events.stop_listening()

    # Unregister classes
    panels.unregister_classes()
    operators.unregister_classes()
    properties.unregister_classes()

    logs.stop_logging()