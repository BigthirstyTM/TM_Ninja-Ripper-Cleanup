"""Module internal definitions"""

import bpy


class MaterialSelection(bpy.types.PropertyGroup):
    """Store boolean to make a selection."""
    #name: bpy.props.StringProperty(name='Name', default='undefined') duplicate name if enabled...
    selected: bpy.props.BoolProperty(name='Selected', default=True)


class MATERIAL_UL_material_selection(bpy.types.UIList):
    """Draw callback for each item of our material selection."""
    bl_idname = 'MATERIAL_UL_material_selection'

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        mat = item
        icon = bpy.types.UILayout.icon(bpy.data.materials[mat.name])
        if self.layout_type in {'DEFAULT', 'COMPACT'}: # GRID layout not supported
            row = layout.row()
            row.prop(mat, "name", text="", emboss=False, icon_value=icon)
            row.prop(mat, "selected", text="")