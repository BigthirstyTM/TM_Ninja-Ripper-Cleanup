import bpy


class NRCleanup_Props(bpy.types.PropertyGroup):
    collection_from_nr: bpy.props.PointerProperty(type=bpy.types.Collection)