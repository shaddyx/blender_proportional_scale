bl_info = {
    "name": "Move X Axis",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
from bpy.types import WindowManager


class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Simple scale"
    bl_idname = "OBJECT_PT_simple_scale"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    size: bpy.props.FloatProperty(
        name="Size",
        default=3.0,
    )

    def draw(self, context):
        layout = self.layout

        obj = context.object
        wm = context.window_manager

        row = layout.row()
        row.label(text="Hello world!", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(wm, "expand_size")

        row = layout.row()
        row.operator("mesh.primitive_cube_add")


def register():
    bpy.utils.register_class(HelloWorldPanel)
    WindowManager.expand_size = bpy.props.FloatProperty(name="Expand Size", default=2.0)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
