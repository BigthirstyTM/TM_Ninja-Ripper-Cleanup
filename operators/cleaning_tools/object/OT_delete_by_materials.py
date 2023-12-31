import bpy
import bmesh


class MaterialSelection(bpy.types.PropertyGroup):
    """Store boolean to make a selection"""  
    #name: bpy.props.StringProperty(name='Name', default='undefined') duplicate name if enabled...
    selected: bpy.props.BoolProperty(name='Selected', default=True)


class MATERIAL_UL_material_selection(bpy.types.UIList):
    """Draw callback for each item of our material selection"""
    #bl_idname = 'MATERIAL_UL_material_selection'

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        mat = item
        icon = bpy.data.materials[mat.name].preview.icon_id
        if self.layout_type in {'DEFAULT', 'COMPACT'}: # GRID layout not supported
            row = layout.row()
            row.prop(mat, 'name', text='', emboss=False, icon_value=icon)
            row.prop(mat, 'selected', text='')


class OBJECT_OT_delete_faces_by_material(bpy.types.Operator):
    """Delete the faces that doesn't match a material selection"""
    bl_idname = 'object.delete_faces_by_material'
    bl_label = 'Delete Faces By Material'
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
        return (
            context.mode == 'OBJECT'
            and context.object is not None
            and context.object.type == 'MESH'
            and len(context.selected_objects) > 0
        )
    
    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                selected_materials = [ms.name for ms in self.material_selection if ms.selected]
                material_at_slot =  [ms.name for ms in obj.material_slots]
                # Get the mesh data
                bm = bmesh.new()
                bm.from_mesh(obj.data)
                # Selecting faces to delete
                delete_faces = [f for f in bm.faces if material_at_slot[f.material_index] not in selected_materials]
                # Delete selected faces
                bmesh.ops.delete(bm, geom=delete_faces, context='FACES')
                # Write the bmesh back to the mesh
                bm.to_mesh(obj.data)
                obj.data.update()
                bm.free()
                self.report({'INFO'}, f'Deleted {len(delete_faces)} faces in {obj.name}')
        return {'FINISHED'}
        
    def invoke(self, context, event):
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                for mat in obj.data.materials:
                    if mat.name not in self.material_selection:
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
            listtype_name='MATERIAL_UL_material_selection',
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