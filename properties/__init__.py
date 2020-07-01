import bpy
from . import props


submodules = (
    props,
    )


def register():
    for sub in submodules:
        sub.register()


def unregister():
    for sub in reversed(submodules):
        sub.unregister()
