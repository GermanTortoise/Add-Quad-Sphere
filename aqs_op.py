import bpy
import bmesh
from bpy_extras.object_utils import AddObjectHelper
from bpy.props import FloatProperty,FloatVectorProperty, IntProperty
from bpy.types import Operator
from mathutils import Vector

class Add_Quad_Sphere(bpy.types.Operator, AddObjectHelper):
    """Add a quad sphere"""
    bl_idname = "mesh.primitive_quad_sphere_add"
    bl_label = "Quad Sphere"
    bl_options = {'REGISTER', 'UNDO'}

    segments: IntProperty(
        name='Segments',
        default=2,
        subtype='DISTANCE',
        soft_min=1,
        description='Segments per "face"'
    
    )
    
    radius: FloatProperty(
        name="Radius",
        default=1.0,
        description="Radius before scaling",
        subtype='DISTANCE',
        soft_min=0.0
    )
    
    scale: FloatVectorProperty(
        name="Scale",
        default=(1.0, 1.0, 1.0),
        subtype='XYZ',
        description="Scale",
    )


    def execute(self, context):
        
        """
        Creates the quad sphere mesh
        """
        
        width = self.scale.x
        depth = self.scale.y
        height = self.scale.z
        radius = self.radius
        
        
        mesh1 = bpy.data.meshes.new("Quad_Sphere")

        bm = bmesh.new()
        
        bmesh.ops.create_cube(bm, size=radius*2)

        bmesh.ops.bevel(bm, geom=bm.edges, offset=radius*1000, segments=self.segments, profile=0.5, affect='EDGES', clamp_overlap=True)
        bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.00001)
        bmesh.ops.scale(bm, vec=Vector((width, depth, height)), verts=bm.verts)

        bm.to_mesh(mesh1)
        mesh1.update()

        # add the mesh as an object into the scene with this utility module
        from bpy_extras import object_utils
        object_utils.object_data_add(context, mesh1, operator=self)
        
        return {'FINISHED'}