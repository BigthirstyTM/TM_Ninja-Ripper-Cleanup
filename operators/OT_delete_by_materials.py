import bpy

from .operators import (
    MaterialSelection,
    MATERIAL_UL_material_selection,
)

from ..utils import logs
log = logs.get_logger(__name__)


class MESH_OT_delete_by_materials(bpy.types.Operator):
    """Delete the faces that doesn't match a material selection."""
    bl_idname = 'object.delete_by_materials'
    bl_label = 'Delete by materials'
    bl_options = {'REGISTER', 'UNDO'}

    active_mat_item_index: bpy.props.IntProperty(default=0)
    material_selection: bpy.props.CollectionProperty(type=MaterialSelection, options={'SKIP_SAVE'})
    preview_render_type_enum: bpy.props.EnumProperty(
        name='Preview Render Type',
        items=[('FLAT', 'FLAT', '', 'MATPLANE', 0),
               ('SPHERE','SPHERE', '', 'MATSPHERE', 1),
               ('CUBE','CUBE', '', 'MATCUBE', 2)]
    )

    @classmethod
    def poll(cls, context):
        return (context.object.type == 'MESH')
    
    def execute(self, context):
        selected_materials = [ms.name for ms in self.material_selection if ms.selected]
        material_at_slot =  [ms.name for ms in bpy.context.object.material_slots]
        # don't make any copy to preserve memory
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='OBJECT')
        for f in context.object.data.polygons:
            if material_at_slot[f.material_index] not in selected_materials:
                f.select = True
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.delete(type='FACE')
        bpy.ops.object.mode_set(mode='OBJECT')
        return {'FINISHED'}
        
    def invoke(self, context, event):
        for mat in context.object.data.materials:
            m = self.material_selection.add()
            m.name = mat.name
        return context.window_manager.invoke_props_dialog(self, width=300)
    
    def check(self, context):
        active_mat_item = self.material_selection[self.active_mat_item_index]
        active_mat_name = active_mat_item.name
        active_mat_id = bpy.data.materials[active_mat_name]       
        active_mat_id.preview_render_type = self.preview_render_type_enum      
        return True
            
    def draw(self, context):    
        active_mat_item = self.material_selection[self.active_mat_item_index]
        active_mat_name = active_mat_item.name
        active_mat_selected = active_mat_item.selected
        active_mat_id = bpy.data.materials[active_mat_name]    
        preview = active_mat_id.preview
        
        # Layout start
        layout = self.layout
        col = layout.column()    
        # Selected material
        row = col.box().row()
        row.label(text=f'{active_mat_name}', icon='MATERIAL')
         # Common button to toggle material selected
        if active_mat_selected:           
            row.prop(active_mat_item, 'selected', text='Keep', toggle=1, icon='FUND')
        else:
            row.prop(active_mat_item, 'selected', text='Delete', toggle=1, icon='TRASH')
        # Material selection list                           
        col.template_list(
            listtype_name=MATERIAL_UL_material_selection.bl_idname,
            list_id='',
            dataptr=self,
            propname='material_selection',
            active_dataptr=self,
            active_propname='active_mat_item_index',
            rows=8,
            maxrows=8,
            type='DEFAULT')   
        # Preview icon, not material because there's no 'clean' way tu refresh layout.template_preview()
        box = col.box()
        box.row().prop_tabs_enum(self, 'preview_render_type_enum', icon_only=True)
        box.template_icon(preview.icon_id, scale=14)