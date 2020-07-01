import bpy
from . import node_sockets, nodes, node_trees


submodules = (
    node_sockets,
    nodes,
    node_trees,
    )


def register():
    for sub in submodules:
        sub.register()

def unregister():
    for sub in reversed(submodules):
        sub.unregister()
