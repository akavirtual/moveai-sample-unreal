// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class MoveAISample : ModuleRules
{
	public MoveAISample(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;

		PublicDependencyModuleNames.AddRange(new string[] {
			"Core",
			"CoreUObject",
			"Engine",
			"InputCore",
			"EnhancedInput",
			"AIModule",
			"StateTreeModule",
			"GameplayStateTreeModule",
			"UMG",
			"Slate"
		});

		PrivateDependencyModuleNames.AddRange(new string[] { });

		PublicIncludePaths.AddRange(new string[] {
			"MoveAISample",
			"MoveAISample/Variant_Platforming",
			"MoveAISample/Variant_Platforming/Animation",
			"MoveAISample/Variant_Combat",
			"MoveAISample/Variant_Combat/AI",
			"MoveAISample/Variant_Combat/Animation",
			"MoveAISample/Variant_Combat/Gameplay",
			"MoveAISample/Variant_Combat/Interfaces",
			"MoveAISample/Variant_Combat/UI",
			"MoveAISample/Variant_SideScrolling",
			"MoveAISample/Variant_SideScrolling/AI",
			"MoveAISample/Variant_SideScrolling/Gameplay",
			"MoveAISample/Variant_SideScrolling/Interfaces",
			"MoveAISample/Variant_SideScrolling/UI"
		});

		// Uncomment if you are using Slate UI
		// PrivateDependencyModuleNames.AddRange(new string[] { "Slate", "SlateCore" });

		// Uncomment if you are using online features
		// PrivateDependencyModuleNames.Add("OnlineSubsystem");

		// To include OnlineSubsystemSteam, add it to the plugins section in your uproject file with the Enabled attribute set to true
	}
}
