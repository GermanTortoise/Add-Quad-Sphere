bl_info = {
        "name" : "Add Quad Sphere",
        "author" : "Yunhan Luo",
        "version" : (1, 0, 0),
        "blender" : (3, 4, 1),
        "location" : "View 3D > Add > Mesh",
        "description" :
            "Adds a quad sphere",
        "warning" : "",
        "wiki_url" : "",
        "tracker_url" : "",
        "category" : "Add Mesh",
        }

import bpy
from . aqs_op import Add_Quad_Sphere

def menu_func(self, context):
    self.layout.operator(Add_Quad_Sphere.bl_idname, text='Quad Sphere', icon='SPHERE')


# Register and add to the "add mesh" menu (required to use F3 search "Add Box" for quick access).
def register():
    bpy.utils.register_class(Add_Quad_Sphere)
    bpy.types.VIEW3D_MT_mesh_add.prepend(menu_func)

def unregister():
    bpy.utils.unregister_class(Add_Quad_Sphere)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)
    
    