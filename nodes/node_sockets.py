import bpy
from bpy.types import NodeSocket
from ..properties.props import TestProps

# Custom socket type
class MyCustomSocket(NodeSocket):
    # Description string
    '''Custom node socket type'''
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'CustomSocketType'
    # Label for nice name display
    bl_label = "Custom Node Socket"

    # Enum items list
    # my_items = (
    #     ('DOWN', "Down", "Where your feet are"),
    #     ('UP', "Up", "Where your head should be"),
    #     ('LEFT', "Left", "Not right"),
    #     ('RIGHT', "Right", "Not left"),
    # )


    # my_enum_prop: bpy.props.EnumProperty(
    #     name="Direction",
    #     description="Just an example",
    #     items=my_items,
    #     default='UP',
    # )
    my_enum_prop: TestProps.my_float_prop


    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "my_enum_prop", text=text)

    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)


classes = (
	MyCustomSocket
	)


def register():
    from bpy.utils import register_class
    # for cls in classes:
    #     register_class(cls)
    register_class(MyCustomSocket)


def unregister():
    from bpy.utils import unregister_class
    # for cls in reversed(classes):
    #     unregister_class(cls)
    unregister_class(MyCustomSocket)