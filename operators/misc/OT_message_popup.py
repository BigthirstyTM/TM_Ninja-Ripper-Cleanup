import bpy


class WINDOW_OT_message_popup(bpy.types.Operator):
    bl_idname = 'window.message_popup'
    bl_label = 'Message Popup'

    title: bpy.props.StringProperty(name='Title', default='')
    icon: bpy.props.StringProperty(name='Icon', default='QUESTION')
    message: bpy.props.StringProperty(name='Message', default='Undefined')

    def invoke(self, context, event):
        return bpy.types.WindowManager.invoke_popup(self)

    def execute(self, context):
        return {'FINISHED'}        

    def draw(self, context):
        layout = self.layout
        layout.label(text=self.title, icon=self.icon)
        lines = self.message.split('\n')
        for i in range(len(lines)):
            layout.label(text=lines[i])