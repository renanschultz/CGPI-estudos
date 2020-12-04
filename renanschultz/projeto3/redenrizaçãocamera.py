import bpy

cena=bpy.context.scene
cena.frame_end=50
bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,0))
esfera=bpy.context.object

locations=[(0,0,-2), (0,0,1), (0,0,0), (0,0,1), (0,0,2)]
quadro = 0

for l in locations:
    cena.frame_set(quadro)
    esfera.location = l
    esfera.keyframe_insert(data_path="location")
    quadro +=40
