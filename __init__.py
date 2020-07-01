bl_info = {
    "name": "Test props",
    "author": "RUben Begalov",
    "version": (0, 1, 0), # Make sure this matches the version in version.txt  Update both
    "blender": (2, 80, 0),
    "category": "Test"}

if 'bpy' in locals():
    import importlib
    if "properties" in locals():
        importlib.reload(properties)
    if "nodes" in locals():
        importlib.reload(nodes)

else:
    import bpy
    from . import properties
    from . import nodes


#------------------------------------
# Register the script
#------------------------------------
submodules = (
    properties,
    nodes,
    )

def register():
    for sub in submodules:
        sub.register()


def unregister():
    for sub in reversed(submodules):
        sub.unregister()


if __name__ == "__main__":
    register()