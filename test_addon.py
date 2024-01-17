bl_info = {
    "name": "Move X Axis",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
import mathutils
from bpy.types import WindowManager


def xy_vect(vect: mathutils.Vector) -> mathutils.Vector:
    return mathutils.Vector((vect.x, vect.y))


def prolong_vector(from_vector: mathutils.Vector, to_vector: mathutils.Vector, size: float) -> mathutils.Vector:
    vect_delta: mathutils.Vector = xy_vect(to_vector) - xy_vect(from_vector)
    scale = (vect_delta.length + size) / vect_delta.length
    return xy_vect(from_vector) + (vect_delta * scale)


def change_mesh(cursor, mesh_obj, scale: float):
    for v in mesh_obj.data.vertices:
        new_v = prolong_vector(cursor, v.co, scale)
        v.co.x = new_v.x
        v.co.y = new_v.y


class CustomDrawOperator(bpy.types.Operator):
    bl_idname = "object.custom_draw"
    bl_label = "Simple Modal Operator"
    use_cursor: bpy.props.BoolProperty(name="Use cursor as object origin", default=False)
    scale_size: bpy.props.FloatProperty(name="Size", default=3.0)

    # @classmethod
    # def poll(cls, context):
    #     obj = context.active_object
    #     return obj and obj.type == 'MESH' and obj.mode == 'EDIT'

    def execute(self, context):
        active_obj = context.active_object
        print("Scale:", self.scale_size)
        origin = mathutils.Vector((0, 0, 0))
        if self.use_cursor:
            print("Use cursor as object origin")
            origin = bpy.context.scene.cursor.location - active_obj.location

        change_mesh(origin, active_obj, self.scale_size)
        print("Test", self)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        obj = context.object
        col = layout.column()
        col.label(text="Custom Interface!")
        row = col.row()
        row.prop(self, "use_cursor")

        row = col.row()
        row.prop(self, "scale_size")
        row.label(text="Active object is: " + obj.name)




class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Simple scale"
    bl_idname = "OBJECT_PT_simple_scale"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Tap to scale", icon='WORLD_DATA')

        row = layout.row()
        row.operator("object.custom_draw")


def register():
    bpy.utils.register_class(HelloWorldPanel)
    bpy.utils.register_class(CustomDrawOperator)
    WindowManager.expand_size = bpy.props.FloatProperty(name="Expand Size", default=2.0)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)
    bpy.utils.unregister_class(CustomDrawOperator)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
