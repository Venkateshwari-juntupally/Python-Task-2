import bpy
import math

# Clear existing objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Create a new scene
bpy.ops.scene.new()

# Set up camera and lighting
bpy.ops.object.camera_add(location=(0, -5, 2))
bpy.context.scene.camera = bpy.context.object
bpy.ops.object.light_add(type='SUN', location=(0, 0, 5))

# Add a glass mesh object
bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=0.05, location=(0, 0, 0))
glass_obj = bpy.context.object

# Apply a transparent material to the glass
glass_mat = bpy.data.materials.new(name='GlassMaterial')
glass_mat.use_nodes = True
glass_nodes = glass_mat.node_tree.nodes
glass_links = glass_mat.node_tree.links
glass_principled = glass_nodes.get("Principled BSDF")

# Set the material properties
glass_principled.inputs['Base Color'].default_value = (1, 1, 1, 1)  # White color
glass_principled.inputs['Roughness'].default_value = 0.1  # Some roughness
glass_principled.inputs['Transmission'].default_value = 1  # Fully transparent
glass_principled.inputs['IOR'].default_value = 1.45  # Index of refraction for glass

# Assign the material to the glass object
glass_obj.data.materials.append(glass_mat)

# Set the glass object as the active object
bpy.context.view_layer.objects.active = glass_obj
glass_obj.select_set(True)

# Render the scene
bpy.ops.render.render(write_still=True)
