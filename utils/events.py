"""Event Routines:

- on_active_obj
- on_load_post
- on_save_post
"""

import bpy
from bpy.app.handlers import persistent

from . import logs

# logging
log = logs.get_logger(__name__)

# Object that will store the handle to the msgbus subscription
_active_obj_handle_owner = object()


#---------------------------------------------------------------------------
#   Callback functions
#---------------------------------------------------------------------------

# Do stuff when active object changes
def _on_active_obj(*args) -> None:
    """Run when active object changes:
    
    - When a different object is clicked in viewport
    - Everytime an object is clicked in outliner"""
    pass


# Do stuff after blender startup
@persistent
def _on_load_post(filepath) -> None:
    """Run post blender startup & file load"""
    if filepath == '':
        # Runs post startup
        bpy.ops.preferences.nrc_check_update()
        
    else:
        # Runs post file load
        pass


# Do stuff after blender file save
@persistent
def _on_save_post(filepath)-> None:
    """Run post blender file save"""
    pass


#---------------------------------------------------------------------------
#   Msgbus subscribing functions
#---------------------------------------------------------------------------
    
# Add subscriber to 'active object' msgbus 
@persistent
def _subscribe_active_obj(dummy) -> None:
    """Subscribe to active object update"""
    bpy.msgbus.clear_by_owner(_active_obj_handle_owner)
    bpy.msgbus.subscribe_rna(
            key=(bpy.types.LayerObjects, "active"),
            owner=_active_obj_handle_owner,
            args=(),
            notify=_on_active_obj,
            options={"PERSISTENT"}
        )
# Remove subscriber from msgbus
@persistent
def _unsubscribe_active_obj(dummy) -> None:
    bpy.msgbus.clear_by_owner(_active_obj_handle_owner)


#---------------------------------------------------------------------------
#   Manage callbacks
#---------------------------------------------------------------------------

# Load event handlers
def start_listening() -> None:
    """Load message subscriber, startup & save routines"""
    _subscribe_active_obj(_active_obj_handle_owner)

    if _subscribe_active_obj not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(_subscribe_active_obj)
        
    if _on_load_post not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(_on_load_post)

    if _on_save_post not in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.append(_on_save_post)


# Delete event handlers
def stop_listening() -> None:
    """remove message subscriber, startup & save routines"""
    _unsubscribe_active_obj(_active_obj_handle_owner)

    if _subscribe_active_obj in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(_subscribe_active_obj)
        
    if _on_load_post in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(_on_load_post)

    if _on_save_post in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.remove(_on_save_post)