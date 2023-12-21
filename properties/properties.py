import bpy


class NRCleanup_Props(bpy.types.PropertyGroup):
    nr_collection: bpy.props.PointerProperty(type=bpy.types.Collection)