import bpy
import bmesh
from mathutils import Vector
import math

def create_moveai_skeleton():
    # Remove existing objects if needed
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    # Create the armature
    armature_data = bpy.data.armatures.new("MoveAI_Armature")
    armature_obj = bpy.data.objects.new("MoveAI_Skeleton", armature_data)
    
    # Link the armature object to the scene
    bpy.context.collection.objects.link(armature_obj)
    bpy.context.view_layer.objects.active = armature_obj
    
    # Enter edit mode to add bones
    bpy.ops.object.mode_set(mode='EDIT')
    
    edit_bones = armature_obj.data.edit_bones
    
    # Define the bone structure based on the MoveAI data source
    bone_structure = {
        "R": {"parent": None, "head": (0, 0, 0), "tail": (0, 0, 0.1)},  # Root
        "Spine": {"parent": "R", "head": (0, 0, 0.204962417), "tail": (0, 0, 0.4)},  # Offset: z: 0.204962417
        "Chest": {"parent": "Spine", "head": (0, 0, 0.4), "tail": (0, 0, 0.8)},  # Connected to Spine
        "Neck": {"parent": "Chest", "head": (0, 0, 0.821672642), "tail": (0, 0, 0.921672642)},  # Offset: z: 0.421672642
        # Left side
        "L_Shoulder_prism": {"parent": "Chest", "head": (0.172936097, 0, 0.525103551), "tail": (0.272936097, 0, 0.525103551)},  # x: 0.172936097, z: 0.325103551
        "L_Shoulder": {"parent": "L_Shoulder_prism", "head": (0.172936097, 0, 0.525103551), "tail": (0.172936097, 0, 0.219143134)},  # Rotation offset included
        "L_Elbow": {"parent": "L_Shoulder", "head": (0.172936097, 0, 0.219143134), "tail": (0.172936097, 0, -0.086817283)},  # z: -0.305960417 from shoulder
        "L_Wrist": {"parent": "L_Elbow", "head": (0.172936097, 0, -0.086817283), "tail": (0.172936097, 0, -0.353509623)},  # z: -0.26669234 from elbow
        "L_hand1": {"parent": "L_Wrist", "head": (0.172936097, 0.04, -0.425509623), "tail": (0.172936097, 0.08, -0.497509623)},  # y: 0.04, z: -0.072 from wrist
        "L_hand2": {"parent": "L_Wrist", "head": (0.172936097, -0.05, -0.433509623), "tail": (0.172936097, -0.10, -0.513509623)},  # y: -0.05, z: -0.08 from wrist
        # Right side
        "R_Shoulder_prism": {"parent": "Chest", "head": (-0.172936097, 0, 0.525103551), "tail": (-0.272936097, 0, 0.525103551)},  # x: -0.172936097, z: 0.325103551
        "R_Shoulder": {"parent": "R_Shoulder_prism", "head": (-0.172936097, 0, 0.525103551), "tail": (-0.172936097, 0, 0.219143134)},  # Rotation offset included
        "R_Elbow": {"parent": "R_Shoulder", "head": (-0.172936097, 0, 0.219143134), "tail": (-0.172936097, 0, -0.086817283)},  # z: -0.305960417 from shoulder
        "R_Wrist": {"parent": "R_Elbow", "head": (-0.172936097, 0, -0.086817283), "tail": (-0.172936097, 0, -0.353509623)},  # z: -0.26669234 from elbow
        "R_hand1": {"parent": "R_Wrist", "head": (-0.172936097, 0.04, -0.425509623), "tail": (-0.172936097, 0.08, -0.497509623)},  # y: 0.04, z: -0.072 from wrist
        "R_hand2": {"parent": "R_Wrist", "head": (-0.172936097, -0.05, -0.433509623), "tail": (-0.172936097, -0.10, -0.513509623)},  # y: -0.05, z: -0.08 from wrist
        # Left leg
        "L_Hip": {"parent": "R", "head": (0.101491697, 0, 0), "tail": (0.101491697, 0, -0.423745543)},  # x: 0.101491697
        "L_Knee": {"parent": "L_Hip", "head": (0.101491697, 0, -0.423745543), "tail": (0.101491697, 0, -0.88159442)},  # z: -0.423745543 from hip
        "L_Ankle": {"parent": "L_Knee", "head": (0.101491697, 0, -0.88159442), "tail": (0.101491697, 0, -1.339443297)},  # z: -0.457848877 from knee
        "L_Foot_Pinky": {"parent": "L_Ankle", "head": (0.14767088, -0.125943229, -1.381424372), "tail": (0.193850063, -0.251886458, -1.423405447)},  # x: 0.0461791828, y: -0.125943229, z: -0.041981075 from ankle
        "L_BigToe": {"parent": "L_Ankle", "head": (0.010133329, -0.167924304, -1.381424372), "tail": (0.010133329, -0.209905379, -1.423405447)},  # x: -0.0923583657, y: -0.041981075 from ankle
        # Right leg
        "R_Hip": {"parent": "R", "head": (-0.101491697, 0, 0), "tail": (-0.101491697, 0, -0.423745543)},  # x: -0.101491697
        "R_Knee": {"parent": "R_Hip", "head": (-0.101491697, 0, -0.423745543), "tail": (-0.101491697, 0, -0.88159442)},  # z: -0.423745543 from hip
        "R_Ankle": {"parent": "R_Knee", "head": (-0.101491697, 0, -0.88159442), "tail": (-0.101491697, 0, -1.339443297)},  # z: -0.457848877 from knee
        "R_Foot_Pinky": {"parent": "R_Ankle", "head": (-0.14767088, -0.125943229, -1.381424372), "tail": (-0.14767088, -0.251886458, -1.423405447)},  # x: -0.0461791828, y: -0.125943229, z: -0.041981075 from ankle
        "R_BigToe": {"parent": "R_Ankle", "head": (-0.010133329, -0.167924304, -1.381424372), "tail": (-0.010133329, -0.209905379, -1.423405447)},  # x: 0.0923583657, y: -0.041981075 from ankle
        # Head details
        "L_Eye": {"parent": "Neck", "head": (0.084645547, 0, 0.921672642), "tail": (0.184645547, 0, 0.921672642)},  # x: 0.084645547 from neck
        "L_Ear": {"parent": "Neck", "head": (0.084645547, 0, 1.015172642), "tail": (0.184645547, 0, 1.015172642)},  # x: 0.084645547, z: 0.0935 from neck
        "R_Eye": {"parent": "Neck", "head": (-0.084645547, 0, 0.921672642), "tail": (-0.184645547, 0, 0.921672642)},  # Based on L_Eye mirrored
        "R_Ear": {"parent": "Neck", "head": (-0.169291094, 0, 0.921672642), "tail": (-0.269291094, 0, 0.921672642)},  # x: -0.169291094 from neck
    }

    # Create bones based on the structure
    bone_objects = {}
    for bone_name, bone_data in bone_structure.items():
        bone = edit_bones.new(bone_name)
        bone.head = bone_data["head"]
        bone.tail = bone_data["tail"]
        
        if bone_data["parent"]:
            bone.parent = bone_objects[bone_data["parent"]]
        
        bone_objects[bone_name] = bone

    # Set the roll of each bone for better orientation
    bpy.ops.armature.calculate_roll(type='GLOBAL_POS_Y')

    # Exit edit mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Add a simple mesh to visualize the skeleton
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.02, location=(0, 0, 0))
    mesh_obj = bpy.context.active_object
    mesh_obj.name = "MoveAI_Mesh"
    
    # Add armature modifier to the mesh
    modifier = mesh_obj.modifiers.new(name="Armature", type='ARMATURE')
    modifier.object = armature_obj

    # Create a vertex group for each bone
    for bone_name in bone_structure.keys():
        vertex_group = mesh_obj.vertex_groups.new(name=bone_name)
        # For a simple sphere, assign all vertices to each group with different weights
        # In a real scenario, you'd assign vertices based on proximity to bones
        for i in range(len(mesh_obj.data.vertices)):
            vertex_group.add([i], 1.0 / len(bone_structure), 'REPLACE')

    # Create an armature modifier for skinning
    bpy.context.view_layer.objects.active = mesh_obj

    print("MoveAI skeleton created successfully!")
    return armature_obj, mesh_obj

# Execute the function
create_moveai_skeleton()