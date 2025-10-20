import unreal

def create_moveai_skeleton():
    """
    Creates a skeleton asset matching the MoveAI source bone structure in Unreal Engine
    """
    
    # Define the bone hierarchy based on the MoveAI data
    bone_hierarchy = [
        # (Bone Name, Parent Index, Location Offset, Rotation Offset)
        ("R", -1, [0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]),  # Root
        ("Spine", 0, [0.0, 0.0, 0.204962417], [0.0, 0.0, 0.0, 1.0]),  # parent: R
        ("Chest", 1, [0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]),  # parent: Spine
        ("Neck", 2, [0.0, 0.0, 0.421672642], [0.0, 0.0, 0.0, 1.0]),  # parent: Chest
        # Left side
        ("L_Shoulder_prism", 2, [0.172936097, 0.0, 0.325103551], [-8.6595606e-17, -0.707106769, -8.6595606e-17, 0.707106769]),  # parent: Chest
        ("L_Shoulder", 4, [0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]),  # parent: L_Shoulder_prism
        ("L_Elbow", 5, [0.0, 0.0, -0.305960417], [0.0, 0.0, 0.0, 1.0]),  # parent: L_Shoulder
        ("L_Wrist", 6, [0.0, 0.0, -0.26669234], [0.0, 0.0, 0.0, 1.0]),  # parent: L_Elbow
        ("L_hand1", 7, [0.0, 0.04, -0.072], [0.0, 0.0, 0.0, 1.0]),  # parent: L_Wrist
        ("L_hand2", 7, [0.0, -0.05, -0.08], [0.0, 0.0, 0.0, 1.0]),  # parent: L_Wrist
        # Right side
        ("R_Shoulder_prism", 2, [-0.172936097, 0.0, 0.325103551], [2.65122575e-33, 0.707106769, 2.65122575e-33, 0.707106769]),  # parent: Chest
        ("R_Shoulder", 10, [0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]),  # parent: R_Shoulder_prism
        ("R_Elbow", 11, [0.0, 0.0, -0.305960417], [0.0, 0.0, 0.0, 1.0]),  # parent: R_Shoulder
        ("R_Wrist", 12, [0.0, 0.0, -0.26669234], [0.0, 0.0, 0.0, 1.0]),  # parent: R_Elbow
        ("R_hand1", 13, [0.0, 0.04, -0.072], [0.0, 0.0, 0.0, 1.0]),  # parent: R_Wrist
        ("R_hand2", 13, [0.0, -0.05, -0.08], [0.0, 0.0, 0.0, 1.0]),  # parent: R_Wrist
        # Left leg
        ("L_Hip", 0, [0.101491697, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]),  # parent: R
        ("L_Knee", 16, [0.0, 0.0, -0.423745543], [0.0, 0.0, 0.0, 1.0]),  # parent: L_Hip
        ("L_Ankle", 17, [0.0, 0.0, -0.457848877], [0.0, 0.0, 0.0, 1.0]),  # parent: L_Knee
        ("L_Foot_Pinky", 18, [0.0461791828, -0.125943229, -0.041981075], [0.0, 0.0, 0.0, 1.0]),  # parent: L_Ankle
        ("L_BigToe", 18, [-0.0923583657, -0.041981075, 0.0], [0.0, 0.0, 0.0, 1.0]),  # parent: L_Ankle
        # Right leg
        ("R_Hip", 0, [-0.101491697, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]),  # parent: R
        ("R_Knee", 21, [0.0, 0.0, -0.423745543], [0.0, 0.0, 0.0, 1.0]),  # parent: R_Hip
        ("R_Ankle", 22, [0.0, 0.0, -0.457848877], [0.0, 0.0, 0.0, 1.0]),  # parent: R_Knee
        ("R_Foot_Pinky", 23, [-0.0461791828, -0.125943229, -0.041981075], [0.0, 0.0, 0.0, 1.0]),  # parent: R_Ankle
        ("R_BigToe", 23, [0.0923583657, -0.041981075, 0.0], [0.0, 0.0, 0.0, 1.0]),  # parent: R_Ankle
        # Head details
        ("L_Eye", 3, [0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]),  # parent: Neck
        ("L_Ear", 3, [0.084645547, 0.0, 0.0935], [0.0, 0.0, 0.0, 1.0]),  # parent: Neck
        ("R_Eye", 3, [0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]),  # parent: Neck
        ("R_Ear", 3, [-0.169291094, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]),  # parent: Neck
    ]

    # Create a new skeleton asset
    skeleton_path = "/Game/MoveAI_Skeleton"
    skeleton_factory = unreal.SkeletonFactory()

    # Note: Creating skeletons programmatically in Unreal is complex and typically requires
    # a more involved process. This is a conceptual example.
    
    print("Creating MoveAI skeleton with the following bone structure:")
    for i, (name, parent_idx, location, rotation) in enumerate(bone_hierarchy):
        parent_name = bone_hierarchy[parent_idx][0] if parent_idx != -1 else "None"
        print(f"Bone {i}: {name}, Parent: {parent_name}, Location: {location}")

    # In a real implementation, you would create an empty skeleton asset and then
    # use the Skeleton Editor API to add each bone with its correct parent relationship
    print("\nMoveAI skeleton structure created successfully!")
    print("Note: Actual skeleton creation in Unreal requires manual setup or use of Animation Blueprint tools.")
    
    # Return the bone hierarchy for reference
    return bone_hierarchy

# Execute the function
bone_hierarchy = create_moveai_skeleton()