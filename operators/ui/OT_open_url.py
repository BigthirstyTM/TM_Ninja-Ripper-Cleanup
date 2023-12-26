import bpy
import webbrowser


class UI_OT_open_url(bpy.types.Operator):
    bl_idname = "ui.open_url"
    bl_description = "Open URL in web browser"
    bl_label = "Open URL"

    url: bpy.props.StringProperty("")
        
    def execute(self, context):
        webbrowser.open(self.url)
        return {"FINISHED"}