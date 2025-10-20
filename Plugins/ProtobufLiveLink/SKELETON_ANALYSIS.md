# MoveAI ProtobufLiveLink Plugin Analysis

## Project Overview

The MoveAI ProtobufLiveLink plugin is designed to receive motion capture data from a Python gRPC server using protocol buffers (protobuf) and stream it to Unreal Engine via Live Link. The system handles motion capture data containing skeleton information with bones, joints, and transforms.

## Source Skeleton Structure Analysis

Based on the protobuf definition and actual data received, the MoveAI source skeleton has the following structure:

### Bone Names and Hierarchy

**Root Bone:**
- "R" (Root, no parent - parentLinkId: -1)

**Spine Chain:**
- "R" → "Spine" → "Chest" → "Neck"

**Left Arm Chain:**
- "R" → "L_Shoulder_prism" → "L_Shoulder" → "L_Elbow" → "L_Wrist" → ["L_hand1", "L_hand2"]

**Right Arm Chain:**
- "R" → "R_Shoulder_prism" → "R_Shoulder" → "R_Elbow" → "R_Wrist" → ["R_hand1", "R_hand2"]

**Left Leg Chain:**
- "R" → "L_Hip" → "L_Knee" → "L_Ankle" → ["L_Foot_Pinky", "L_BigToe"]

**Right Leg Chain:**
- "R" → "R_Hip" → "R_Knee" → "R_Ankle" → ["R_Foot_Pinky", "R_BigToe"]

**Head Details:**
- "Neck" → ["L_Eye", "L_Ear", "R_Eye", "R_Ear"]

### Special Bone Notes

1. **"prism" Joints**: The skeleton includes "L_Shoulder_prism" and "R_Shoulder_prism" which appear to be auxiliary joints for enhanced animation control. These have specific orientation quaternions that suggest they're used for special joint constraints.

2. **Detailed Hand/Foot Bones**: The skeleton includes detailed finger bones ("L_hand1", "L_hand2", "R_hand1", "R_hand2") and toe bones ("L_BigToe", "L_Foot_Pinky", "R_BigToe", "R_Foot_Pinky").

3. **Head Accessories**: The skeleton includes "L_Eye", "L_Ear", "R_Eye", "R_Ear" bones for facial motion capture.

### Bone Position Offsets

The position offsets from the protobuf data (in meters):
- Spine z: 0.204962417
- Chest connected to Spine
- Neck z: 0.421672642 from Chest
- Left Shoulder Prism: x: 0.172936097, z: 0.325103551
- Right Shoulder Prism: x: -0.172936097, z: 0.325103551
- Left Hip: x: 0.101491697
- Right Hip: x: -0.101491697
- Left Knee: z: -0.423745543 from Hip
- Right Knee: z: -0.423745543 from Hip
- Left Ankle: z: -0.457848877 from Knee
- Right Ankle: z: -0.457848877 from Knee
- Elbow z: -0.305960417 from Shoulder
- Wrist z: -0.26669234 from Elbow

### Rotation Offsets

The "prism" joints have special rotation quaternions:
- L_Shoulder rotation: [-8.6595606e-17, -0.707106769, -8.6595606e-17, 0.707106769]
- R_Shoulder rotation: [2.65122575e-33, 0.707106769, 2.65122575e-33, 0.707106769]

## Data Flow Process

1. **Data Source**: Python gRPC server sends motion capture data using the MocapExchange protocol
2. **Protocol**: MocapExchange.proto defines Structure (skeleton) and Pose (motion) messages
3. **Processing**: LiveLinkSubjectStream.cpp receives structure info and creates FLiveLinkSkeletonStaticData
4. **Remapping**: MoveaiLiveLinkRemapAssetBase handles bone name mapping from source to target skeleton
5. **Application**: Bone transforms are applied to the Unreal skeleton via Live Link

## Bone Name Mapping Implementation

The plugin implements a remapping system where source bone names are mapped to target skeleton bone names using the ULiveLinkRemapAsset base class. Child Blueprint classes implement the GetRemappedBoneName function to map between source names (from MoveAI) and target skeleton names.

## Scripts Provided

1. **blender_create_moveai_skeleton.py**: Creates a Blender armature with the exact MoveAI bone structure and hierarchy
2. **unreal_create_moveai_skeleton.py**: Conceptual Unreal Python script showing the bone structure (for manual implementation in Unreal)

## Compatibility with MoveAI Data

- The skeleton structure matches exactly what MoveAI provides
- No remapping required if using the original MoveAI bone names
- Supports all detailed joints including hands, feet, and head accessories
- Maintains proper parent-child relationships for correct animation propagation