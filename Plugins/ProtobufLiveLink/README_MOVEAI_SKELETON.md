# MoveAI Skeleton Generation and Live Link Integration

## Overview
This repository provides tools and analysis for working with MoveAI motion capture data in Unreal Engine through the ProtobufLiveLink plugin. It includes Python scripts to generate skeletons that match the MoveAI source data structure.

## Files Included

1. `blender_create_moveai_skeleton.py` - Blender Python script to create a skeleton matching MoveAI source
2. `unreal_create_moveai_skeleton.py` - Conceptual Unreal Python script showing bone structure
3. `SKELETON_ANALYSIS.md` - Detailed analysis of the MoveAI source skeleton structure

## MoveAI Source Skeleton Structure

The MoveAI motion capture data source provides the following skeleton structure:

### Root and Spine
- **R** (Root, no parent)
- **Spine** (Child of R, z: 0.204962417)
- **Chest** (Child of Spine)
- **Neck** (Child of Chest, z: 0.421672642 from Chest)

### Left Arm
- **L_Shoulder_prism** (Child of Chest, x: 0.172936097, z: 0.325103551)
- **L_Shoulder** (Child of L_Shoulder_prism)
- **L_Elbow** (Child of L_Shoulder, z: -0.305960417)
- **L_Wrist** (Child of L_Elbow, z: -0.26669234)
- **L_hand1** (Child of L_Wrist, y: 0.04, z: -0.072)
- **L_hand2** (Child of L_Wrist, y: -0.05, z: -0.08)

### Right Arm
- **R_Shoulder_prism** (Child of Chest, x: -0.172936097, z: 0.325103551)
- **R_Shoulder** (Child of R_Shoulder_prism)
- **R_Elbow** (Child of R_Shoulder, z: -0.305960417)
- **R_Wrist** (Child of R_Elbow, z: -0.26669234)
- **R_hand1** (Child of R_Wrist, y: 0.04, z: -0.072)
- **R_hand2** (Child of R_Wrist, y: -0.05, z: -0.08)

### Left Leg
- **L_Hip** (Child of R, x: 0.101491697)
- **L_Knee** (Child of L_Hip, z: -0.423745543)
- **L_Ankle** (Child of L_Knee, z: -0.457848877)
- **L_Foot_Pinky** (Child of L_Ankle, x: 0.0461791828, y: -0.125943229, z: -0.041981075)
- **L_BigToe** (Child of L_Ankle, x: -0.0923583657, y: -0.041981075)

### Right Leg
- **R_Hip** (Child of R, x: -0.101491697)
- **R_Knee** (Child of R_Hip, z: -0.423745543)
- **R_Ankle** (Child of R_Knee, z: -0.457848877)
- **R_Foot_Pinky** (Child of R_Ankle, x: -0.0461791828, y: -0.125943229, z: -0.041981075)
- **R_BigToe** (Child of R_Ankle, x: 0.0923583657, y: -0.041981075)

### Head Details
- **L_Eye** (Child of Neck)
- **L_Ear** (Child of Neck, x: 0.084645547, z: 0.0935)
- **R_Eye** (Child of Neck)
- **R_Ear** (Child of Neck, x: -0.169291094)

### Special Notes
- The "prism" joints (L_Shoulder_prism, R_Shoulder_prism) have special rotation quaternions for enhanced animation
- Bone positions are in meters as per the protobuf specification
- The skeleton includes detailed finger and toe bones for more precise animation

## Using the Blender Script

1. Open Blender
2. Go to the Scripting workspace
3. Open `blender_create_moveai_skeleton.py`
4. Run the script to create the MoveAI-compatible skeleton

The script will:
- Create a new armature named "MoveAI_Skeleton"
- Generate all bones with proper hierarchy and positioning
- Create parent-child relationships matching the MoveAI source
- Add a simple mesh with vertex groups for visualization

## Using with Unreal Engine

The skeleton structure provided matches the MoveAI source data, which means you can configure your Live Link setup to work directly with MoveAI data without requiring bone name remapping.

## Integration with ProtobufLiveLink Plugin

The plugin handles the gRPC communication and transforms the MoveAI protobuf data into Unreal's Live Link format. The skeleton structure analysis helps ensure proper bone name mapping between the source and target skeletons.

## Data Flow

1. MoveAI gRPC server sends Structure and Pose data via protobuf
2. Plugin receives data and creates LiveLink skeleton structure
3. Bone transforms are applied to target skeleton through remapping
4. Animation is displayed in Unreal Engine

## Author
Analysis and scripts created based on the MoveAI ProtobufLiveLink plugin structure.