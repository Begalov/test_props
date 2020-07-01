import bpy

class TestProps( bpy.types.PropertyGroup):
    my_string_prop: bpy.props.StringProperty()
    
    my_float_prop: bpy.props.FloatProperty(default=3.1415926)

    my_items = (
        ('DOWN', "Down", "Where your feet are"),
        ('UP', "Up", "Where your head should be"),
        ('LEFT', "Left", "Not right"),
        ('RIGHT', "Right", "Not left"),
    )

    my_enum_prop: bpy.props.EnumProperty(
        name="Direction",
        description="Just an example",
        items=my_items,
        default='UP',
    )

def register():
    from bpy.utils import register_class

    register_class(TestProps)


def unregister():
    from bpy.utils import unregister_class

    unregister_class(TestProps)