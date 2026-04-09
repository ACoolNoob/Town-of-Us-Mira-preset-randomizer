import os
import math, random

directory = r"Your file path here"
createdFilePath = os.path.join(directory, "Random.cfg")

# roles

# neutral
uniqueNeutralRoles = ["Arsonist", "Plaguebearer", "Chef", "Inquisitor", "Glitch", "Vampire"]
nonUniqueNeutralRoles = ["Amnesiac", "Doomsayer", "Jester", "Juggernaut", "Fairy", "Mercenary", "Spectre", "SoulCollector", "Survivor", "Werewolf", "Executioner",]
# maybe move exe to non unique cuz im dum
# maybe move fairy to unique cuz im dum

# crewmate
uniqueCrewmateRoles = ["Jailor", "Politician", "Prosecutor", "Swapper", "TimeLord", "Monarch"]
nonUniqueCrewmateRoles = ["Altruist", "Aurial", "Cleric", "Deputy", "Engineer", "Forensic", "Haunter", "Hunter", "Imitator", "Investigator", "Lookout", "Medic", "Medium", "Mirrorcaster", "Mystic", "Oracle", "Plumber", "Seer", "Sentry", "Sherrif", "Snitch", "Sonar", "Spy", "Transporter", "Trapper", "Veteran", "Vigilante", "Warden"]

# imp
uniqueImpRoles = ["Ambassador",  "Puppeteer", "Spellslinger", "Traitor"]
nonUniqueImpRoles = ["Ambusher", "Eclipsal", "Escapist", "Grenadier", "Morphling", "Swooper", "Venerer", "Bomber", "Parasite", "Scavenger", "Warlock", "Blackmailer", "Hypnotist", "Janitor", "Miner", "Undertaker", "Herbalist"]



# non unique roles
def NonUniqueRandomRoleSpawn(allignment, role):
    file.write(f"""# Setting type: Int32
# Default value: 0
Num TownOfUs.Roles.{allignment}.{role}Role = {random.randint(0,15)} \n
# Setting type: Int32
# Default value: 0
Chance TownOfUs.Roles.{allignment}.{role}Role = {random.randint(1,100)} \n \n""")

# unique roles
def UniqueRandomRoleSpawn(allignment, role):
    file.write(f"""# Setting type: Int32
# Default value: 0
Num TownOfUs.Roles.{allignment}.{role}Role = {random.randint(0,1)} \n
# Setting type: Int32
# Default value: 0
Chance TownOfUs.Roles.{allignment}.{role}Role = {random.randint(1,100)} \n \n""")

# make file
if not os.path.exists(directory):
    os.makedirs(directory)

# clear and mark the start cuz i need a way to clear it all
with open(createdFilePath, "w") as file:
    file.write("[Roles] \n \n")


# write down settings
with open(createdFilePath, "a") as file:


    # role spawn chances for non unique neuts
    for role in nonUniqueNeutralRoles:
        NonUniqueRandomRoleSpawn("Neutral", role)

    # role spawns for unique neuts
    for role in uniqueNeutralRoles:
        UniqueRandomRoleSpawn("Neutral", role)

    # unique crew
    for role in uniqueCrewmateRoles:
        UniqueRandomRoleSpawn("Crewmate", role)

    # non unique crew
    for role in nonUniqueCrewmateRoles:
        NonUniqueRandomRoleSpawn("Crewmate", role)

    # unique imp
    for role in uniqueImpRoles:
        UniqueRandomRoleSpawn("Impostor", role)

    # non unique
    for role in nonUniqueImpRoles:
        NonUniqueRandomRoleSpawn("Impostor", role)

    # make sure for assasin stuff
    file.write("[TownOfUs.Options.AssassinOptions] \n \n ")

    # im not gonna bother writing stuff for all the settings so its all gonna be 1 string
    file.write(f"""# Setting type: Single
# Default value: 1
NumberOfImpostorAssassins = {random.randint(0,4)}

# Setting type: Single
# Default value: 100
ImpAssassinChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 1
NumberOfNeutralAssassins = {random.randint(0,5)}

# Setting type: Single
# Default value: 100
NeutAssassinChance = {random.randint(0,100)}

# Setting type: Boolean
# Default value: true
AmneTurnImpAssassin = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
AmneTurnNeutAssassin = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
TraitorCanAssassin = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 5
AssassinKills = {random.randint(1,15)}

# Setting type: Boolean
# Default value: true
AssassinMultiKill = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
GuessVanillaRoles = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
AssassinCrewmateGuess = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
AssassinGuessInvest = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
AssassinGuessNeutralBenign = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
AssassinGuessNeutralEvil = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
AssassinGuessNeutralKilling = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
AssassinGuessNeutralOutlier = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
AssassinGuessImpostors = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
AssassinGuessCrewModifiers = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
AssassinGuessUtilityModifiers = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
AssassinGuessAlliances = {random.choice(["true", "false"])}""")

    # time for uh [TownOfUs.Options.GameMechanicOptions]

    file.write(f"""
[TownOfUs.Options.GameMechanicOptions]

# Setting type: Boolean
# Default value: false
GhostwalkerFixSabos = {random.choice(["true", "false"])}

# Setting type: Int32
# Default value: 2
ShowPetsMode = {random.randint(0,2)}

# Setting type: Boolean
# Default value: true
HidePetsOnBodyRemove = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 5
TempSaveCdReset = {random.uniform(0.0,15.0)}
""")


    # time for [TownOfUs.Options.GameTimerOptions]
    file.write(f"""[TownOfUs.Options.GameTimerOptions]

# Setting type: Boolean
# Default value: false
GameTimerEnabled = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 5
PauseInMeetings = {random.randint(1,10)}

# Setting type: Int32
# Default value: 1
TimerEndOption = {random.randint(0,1)}

# Setting type: Single
# Default value: 15
GameTimeLimit = {random.uniform(1.0, 30.0)}

""")

    # okay next section
    file.write(f"""[TownOfUs.Options.GeneralOptions]

# Setting type: Int32
# Default value: 1
ModifierReveal = {random.randint(0,2)}

# Setting type: Boolean
# Default value: true
TeamModifierReveal = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
FFAImpostorMode = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
ImpsKnowRoles = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
ImpostorChat = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
VampireChat = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 10
GameStartCd = {random.uniform(10,30)}

# Setting type: Int32
# Default value: 1
StartCooldownMode = {random.randint(0,2)}

# Setting type: Single
# Default value: 5
StartCooldownMin = {random.uniform(0,60)}

# Setting type: Single
# Default value: 60
StartCooldownMax = {random.uniform(0,60)}

# Setting type: Single
# Default value: 5
AddedMeetingDeathTimer = {random.uniform(0,15)}

# Setting type: Boolean
# Default value: true
FirstDeathShield = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
RoundOneVictims = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
CrewKillersContinue = {random.choice(["true", "false"])}

TempSaveCdReset = 5
""")


    # next
    file.write(f"""[TownOfUs.Options.Maps.AdvancedSabotageOptions]

# Setting type: Boolean
# Default value: true
KillDuringCamoComms = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
CamoKillScreens = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
HidePlayerSizeInCamo = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
HidePlayerSpeedInCamo = {random.choice(["true", "false"])}

CamouflageComms = {random.choice(["true", "false"])}
""")


    # im not even gonna write it down anymore
    file.write(f"""[TownOfUs.Options.Maps.AdvancedUtilityOptions]

# Setting type: Single
# Default value: 1
TasksToUseAdmin = {random.randint(0,15)}

# Setting type: Single
# Default value: 2
TasksToUseCams = {random.randint(0,15)}

# Setting type: Single
# Default value: 0
TasksToUseDoorlog = {random.randint(0,15)}

# Setting type: Single
# Default value: 3
TasksToUseVitals = {random.randint(0,15)}

# Setting type: Boolean
# Default value: true
TasksOnPortables = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Maps.BetterAirshipOptions]

# Setting type: Boolean
# Default value: true
CamoComms = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 1
SpeedMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 1
CrewVisionMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 1
ImpVisionMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 0
CooldownOffset = {random.uniform(-15,15)}

# Setting type: Single
# Default value: 0
OffsetShortTasks = {random.randint(-5,5)}

# Setting type: Single
# Default value: 0
OffsetLongTasks = {random.randint(-3,3)}

# Setting type: Int32
# Default value: 2
AirshipDoorType = {random.randint(0,6)}

# Setting type: Int32
# Default value: 0
SpawnMode = {random.randint(0,3)}

# Setting type: Int32
# Default value: 0
SingleLocation = {random.randint(0,5)}

# Setting type: Boolean
# Default value: true
NoLadderCooldown = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
ChangeSaboTimers = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 90
SaboCountdownReactor = {random.uniform(25, 90)}
""")

    file.write(f"""[TownOfUs.Options.Maps.BetterFungleOptions]

# Setting type: Boolean
# Default value: false
CamoComms = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 1
SpeedMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 1
CrewVisionMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 1
ImpVisionMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 0
CooldownOffset = {random.uniform(-15,15)}

# Setting type: Single
# Default value: 0
OffsetShortTasks = {random.randint(-5,5)}

# Setting type: Single
# Default value: 0
OffsetLongTasks = {random.randint(-3,3)}

# Setting type: Int32
# Default value: 3
FungleDoorType = {random.randint(0,6)}

# Setting type: Boolean
# Default value: true
NoLadderCooldown = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
ChangeSaboTimers = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 60
SaboCountdownReactor = {random.uniform(15, 90)}

# Setting type: Single
# Default value: 10
SaboCountdownMixUp = {random.uniform(5, 60)}
""")

    file.write(f"""[TownOfUs.Options.Maps.BetterLevelImpostorOptions]

# Setting type: Boolean
# Default value: true
CamoComms = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 1
SpeedMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 1
CrewVisionMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 1
ImpVisionMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 0
CooldownOffset = {random.uniform(-15,15)}

# Setting type: Single
# Default value: 0
OffsetShortTasks = {random.randint(-5,5)}

# Setting type: Single
# Default value: 0
OffsetLongTasks = {random.randint(-3,3)}

# Setting type: Boolean
# Default value: true
NoLadderCooldown = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
ChangeOxygenSaboTimer = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
ChangeReactorSaboTimer = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
ChangeMixUpSaboTimer = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 30
SaboCountdownOxygen = {random.uniform(15, 90)}

# Setting type: Single
# Default value: 30
SaboCountdownReactor = {random.uniform(15, 90)}

# Setting type: Single
# Default value: 10
SaboCountdownMixUp = {random.uniform(5, 60)}
""")


    file.write(f"""[TownOfUs.Options.Maps.BetterMiraHqOptions]

# Setting type: Boolean
# Default value: true
CamoComms = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 1
SpeedMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 1
CrewVisionMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 1
ImpVisionMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 0
CooldownOffset = {random.uniform(-15,15)}

# Setting type: Single
# Default value: 0
OffsetShortTasks = {random.randint(-5,5)}

# Setting type: Single
# Default value: 0
OffsetLongTasks = {random.randint(-3,3)}

# Setting type: Int32
# Default value: 0
BetterVentNetwork = {random.randint(0,2)}

# Setting type: Int32
# Default value: 0
MapTheme = {random.randint(0,2)}

# Setting type: Boolean
# Default value: true
ChangeSaboTimers = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 45
SaboCountdownOxygen = {random.uniform(15, 90)}

# Setting type: Single
# Default value: 45
SaboCountdownReactor = {random.uniform(15, 90)}
""")


    file.write(f"""[TownOfUs.Options.Maps.BetterPolusOptions]

# Setting type: Boolean
# Default value: true
CamoComms = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 1
SpeedMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 1
CrewVisionMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 1
ImpVisionMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 0
CooldownOffset = {random.uniform(-15,15)}

# Setting type: Single
# Default value: 0
OffsetShortTasks = {random.randint(-5,5)}

# Setting type: Single
# Default value: 0
OffsetLongTasks = {random.randint(-3,3)}

# Setting type: Int32
# Default value: 1
PolusDoorType = {random.randint(0,6)}

# Setting type: Boolean
# Default value: false
BPVentNetwork = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
BPVitalsInLab = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
BPTempInDeathValley = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
BPSwapWifiAndChart = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
MoveToiletVent = {random.choice(["true", "false"])}

# Setting type: Int32
# Default value: 0
MapTheme = {random.randint(0,2)}

# Setting type: Boolean
# Default value: true
ChangeSaboTimers = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 60
SaboCountdownReactor = {random.uniform(15, 90)}
""")


    file.write(f"""[TownOfUs.Options.Maps.BetterSkeldOptions]

# Setting type: Boolean
# Default value: true
CamoComms = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 1
SpeedMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 1
CrewVisionMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 1
ImpVisionMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 0
CooldownOffset = {random.uniform(-15,15)}

# Setting type: Single
# Default value: 0
OffsetShortTasks = {random.randint(-5,5)}

# Setting type: Single
# Default value: 0
OffsetLongTasks = {random.randint(-3,3)}

# Setting type: Int32
# Default value: 0
SkeldDoorType = {random.randint(0,6)}

# Setting type: Int32
# Default value: 0
BetterVentNetwork = {random.randint(0,1)}

# Setting type: Int32
# Default value: 0
MapTheme = {random.randint(0,2)}

# Setting type: Boolean
# Default value: true
ChangeSaboTimers = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 30
SaboCountdownOxygen = {random.uniform(15, 90)}

# Setting type: Single
# Default value: 30
SaboCountdownReactor = {random.uniform(15, 90)}
""")


    file.write(f"""[TownOfUs.Options.Maps.BetterSubmergedOptions]

# Setting type: Boolean
# Default value: false
CamoComms = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 1
SpeedMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 1
CrewVisionMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 1
ImpVisionMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 0
CooldownOffset = {random.uniform(-15,15)}

# Setting type: Single
# Default value: 0
OffsetShortTasks = {random.randint(-5,5)}

# Setting type: Single
# Default value: 0
OffsetLongTasks = {random.randint(-3,3)}

# Setting type: Int32
# Default value: 4
SubmergedDoorType = {random.randint(0,6)}

# Setting type: Boolean
# Default value: true
ChangeSaboTimers = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 45
SaboCountdownReactor = {random.uniform(15, 90)}

# Setting type: Single
# Default value: 30
SaboCountdownOxygen = {random.uniform(15, 90)}
""")


    file.write(f"""[TownOfUs.Options.Maps.GlobalBetterMapOptions]

# Setting type: Int32
# Default value: 0
GlobalMapCamoCommsConfig = {random.randint(0,2)}

# Setting type: Int32
# Default value: 2
GlobalMapSpeedConfig = {random.randint(0,2)}

# Setting type: Int32
# Default value: 2
GlobalMapCrewVisionConfig = {random.randint(0,2)}

# Setting type: Int32
# Default value: 2
GlobalMapImpVisionConfig = {random.randint(0,2)}

# Setting type: Int32
# Default value: 2
GlobalMapCooldownConfig = {random.randint(0,2)}

# Setting type: Int32
# Default value: 2
GlobalMapShortTaskConfig = {random.randint(0,2)}

# Setting type: Int32
# Default value: 2
GlobalMapLongTaskConfig = {random.randint(0,2)}

# Setting type: Single
# Default value: 1
SpeedMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 1
CrewVisionMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 1
ImpVisionMultiplier = {random.uniform(0.25,1.5)}

# Setting type: Single
# Default value: 0
CooldownOffset = {random.uniform(-15,15)}

# Setting type: Single
# Default value: 0
OffsetShortTasks = {random.randint(-5,5)}

# Setting type: Single
# Default value: 0
OffsetLongTasks = {random.randint(-3,3)}
""")

    file.write(f"""[TownOfUs.Options.Maps.RandomDoorMapOptions]

# Setting type: Single
# Default value: 5
DisabledDoorChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 20
SkeldDoorChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 40
PolusDoorChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 15
AirshipDoorChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 20
FungleDoorChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 25
SubmergedDoorChance = {random.randint(0,100)}
""")


    file.write(f"""[TownOfUs.Options.Maps.TownOfUsMapOptions]

# Setting type: Boolean
# Default value: false
RandomMaps = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 0
SkeldChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
BackwardsSkeldChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
MiraChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
PolusChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
AirshipChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
FungleChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
SubmergedChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
LevelImpostorChance = {random.randint(0,100)}
""")



    file.write(f"""[TownOfUs.Options.Modifiers.Alliance.CrewpostorOptions]

# Setting type: Boolean
# Default value: true
CrewpostorReplacesImpostor = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
CanAlwaysSabotage = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
CrewpostorVision = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
ShowsAsImpostor = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Alliance.EgotistOptions]

# Setting type: Boolean
# Default value: false
EgotistMustSurvive = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
EgotistSpeedsUp = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 1
RoundsToApplyEffects = {random.randint(1,5)}

# Setting type: Single
# Default value: 0.1
SpeedMultiplier = {random.uniform(0,1.5)}

# Setting type: Single
# Default value: 1.5
CooldowmOffset = {random.uniform(0,5)}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Alliance.LoversOptions]

# Setting type: Boolean
# Default value: true
BothLoversDie = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 20
LovingImpPercent = {random.randint(0,100)}

# Setting type: Boolean
# Default value: true
NeutralLovers = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
LoverKillTeammates = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
LoversKillEachOther = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.AllianceModifierOptions]

# Setting type: Single
# Default value: 0
CrewpostorChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
EgotistChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
LoversChance = {random.randint(0,100)}
""")

    file.write(f"""[TownOfUs.Options.Modifiers.Crewmate.BaitOptions]

# Setting type: Single
# Default value: 0
MinDelay = {random.uniform(0,5)}

# Setting type: Single
# Default value: 1
MaxDelay = {random.uniform(0,5)}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Crewmate.DiseasedOptions]

# Setting type: Single
# Default value: 3
CooldownMultiplier = {random.uniform(1.5,5)}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Crewmate.FrostyOptions]

# Setting type: Single
# Default value: 10
ChillDuration = {random.uniform(0,15)}

# Setting type: Single
# Default value: 0.75
ChillStartSpeed = {random.uniform(0.25,0.95)}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Crewmate.NoisemakerOptions]

# Setting type: Boolean
# Default value: true
ImpostorsAlerted = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
NeutsAlerted = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
CommsAffected = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
BodyCheck = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 5
AlertDuration = {random.uniform(1,20)}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Crewmate.OperativeOptions]

# Setting type: Boolean
# Default value: true
MoveOnMira = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 20
StartingCharge = {random.uniform(0,30)}

# Setting type: Single
# Default value: 10
RoundCharge = {random.uniform(0,30)}

# Setting type: Single
# Default value: 7.5
TaskCharge = {random.uniform(0,30)}

# Setting type: Single
# Default value: 15
DisplayCooldown = {random.uniform(0,30)}

# Setting type: Single
# Default value: 15
DisplayDuration = {random.uniform(0,30)}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Crewmate.RottingOptions]

# Setting type: Single
# Default value: 5
RotDelay = {random.uniform(0,25)}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Crewmate.ScientistOptions]

# Setting type: Boolean
# Default value: true
MoveWithMenu = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 20
StartingCharge = {random.uniform(0,30)}

# Setting type: Single
# Default value: 15
RoundCharge = {random.uniform(0,30)}

# Setting type: Single
# Default value: 10
TaskCharge = {random.uniform(0,30)}

# Setting type: Single
# Default value: 15
DisplayCooldown = {random.uniform(0,30)}

# Setting type: Single
# Default value: 15
DisplayDuration = {random.uniform(0,30)}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.CrewmateModifierOptions]

# Setting type: Single
# Default value: 0
AftermathAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
AftermathChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
BaitAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
BaitChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
CelebrityAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
CelebrityChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
DiseasedAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
DiseasedChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
FrostyAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
FrostyChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
InvestigatorAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
InvestigatorChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
MultitaskerAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
MultitaskerChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
NoisemakerAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
NoisemakerChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
OperativeAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
OperativeChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
RottingAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
RottingChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
ScientistAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
ScientistChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
ScoutAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
ScoutChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
SpyAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
SpyChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
TaskmasterAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
TaskmasterChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
TorchAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
TorchChance = {random.randint(0,100)}
""")



    file.write(f"""[TownOfUs.Options.Modifiers.Impostor.CircumventOptions]

# Setting type: Single
# Default value: 3
VentsMin = {random.randint(0,10)}

# Setting type: Single
# Default value: 10
VentsMax = {random.randint(0,10)}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Impostor.DeadlyQuotaOptions]

# Setting type: Single
# Default value: 2
KillQuotaMin = {random.randint(0,5)}

# Setting type: Single
# Default value: 4
KillQuotaMax = {random.randint(0,5)}

# Setting type: Boolean
# Default value: true
MeetingKillsCountTowardsQuota = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
QuotaShield = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
RemoveQuotaUponDeath = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Impostor.SaboteurOptions]

# Setting type: Single
# Default value: 10
ReducedSaboCooldown = {random.uniform(0,15)}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Impostor.TelepathOptions]

# Setting type: Boolean
# Default value: true
KnowKillLocation = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
KnowDeath = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
KnowDeathLocation = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 2.5
TelepathArrowDuration = {random.uniform(0,5)}

# Setting type: Boolean
# Default value: true
KnowCorrectGuess = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
KnowFailedGuess = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Impostor.UnderdogOptions]

# Setting type: Single
# Default value: 5
KillCooldownIncrease = {random.uniform(2.5,10)}

# Setting type: Boolean
# Default value: false
ExtraImpsKillCooldown = {random.choice(["true", "false"])}
""")

    
    file.write(f"""[TownOfUs.Options.Modifiers.ImpostorModifierOptions]

# Setting type: Single
# Default value: 0
CircumventAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
CircumventChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
DeadlyQuotaAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
DeadlyQuotaChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
DisperserAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
DisperserChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
DoubleShotAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
DoubleShotChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
SaboteurAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
SaboteurChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
TelepathAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
TelepathChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
UnderdogAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
UnderdogChance = {random.randint(0,100)}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.NeutralModifierOptions]

# Setting type: Single
# Default value: 0
DoubleShotAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
DoubleShotChance = {random.randint(0,100)}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Universal.ButtonBarryOptions]

# Setting type: Single
# Default value: 30
Cooldown = {random.uniform(2.5,60)}

# Setting type: Single
# Default value: 1
MaxNumButtons = {random.randint(0,3)}

# Setting type: Boolean
# Default value: true
IgnoreSabo = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
FirstRoundUse = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Universal.FlashOptions]

# Setting type: Single
# Default value: 1.75
FlashSpeed = {random.uniform(1.05,2.5)}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Universal.GiantOptions]

# Setting type: Single
# Default value: 0.75
GiantSpeed = {random.uniform(0.25,1)} 
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Universal.MiniOptions]

# Setting type: Single
# Default value: 1.35
MiniSpeed = {random.uniform(1.05,2.5)} 
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Universal.SatelliteOptions]

# Setting type: Single
# Default value: 15
Cooldown = {random.uniform(15,60)} 

# Setting type: Single
# Default value: 5
MaxNumCast = {random.randint(1,15)}

# Setting type: Boolean
# Default value: true
OneUsePerRound = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
FirstRoundUse = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.Universal.ShyOptions]

# Setting type: Single
# Default value: 5
InvisDelay = {random.uniform(0,15)} 

# Setting type: Single
# Default value: 5
TransformInvisDuration = {random.uniform(0,15)}

# Setting type: Single
# Default value: 20
FinalTransparency = {random.uniform(0,80)}
""")


    file.write(f"""[TownOfUs.Options.Modifiers.UniversalModifierOptions]

# Setting type: Single
# Default value: 0
ButtonBarryAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
ButtonBarryChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
FlashAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
FlashChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
GiantAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
GiantChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
ImmovableAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
ImmovableChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
MiniAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
MiniChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
RadarAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
RadarChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
SatelliteAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
SatelliteChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
ShyAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
ShyChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
SixthSenseAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
SixthSenseChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
SleuthAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
SleuthChance = {random.randint(0,100)}

# Setting type: Single
# Default value: 0
TiebreakerAmount = {random.randint(0,15)}

# Setting type: Single
# Default value: 50
TiebreakerChance = {random.randint(0,100)}
""")


    file.write(f"""[TownOfUs.Options.PostmortemOptions]

# Setting type: Boolean
# Default value: true
TheDeadKnow = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
DeadSeeVotes = {random.choice(["true", "false"])}

# Setting type: Int32
# Default value: 1
DeadSeePrivateChat = {random.randint(0,3)}

# Setting type: Int32
# Default value: 1
DeadCanHaunt = {random.randint(0,2)}

# Setting type: Boolean
# Default value: true
HideChatButton = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.RoleOptions]

# Setting type: Int32
# Default value: 1
RoleAssignmentType = 1

# Setting type: Boolean
# Default value: true
LastImpostorBias = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 15
ImpostorBiasPercent = {random.uniform(0,100)}

# Setting type: Int32
# Default value: 0
Slot1 = {random.randint(0,24)}

# Setting type: Int32
# Default value: 0
Slot2 = {random.randint(0,24)}

# Setting type: Int32
# Default value: 0
Slot3 = {random.randint(0,24)}

# Setting type: Int32
# Default value: 17
Slot4 = {random.randint(0,24)}

# Setting type: Int32
# Default value: 0
Slot5 = {random.randint(0,24)}

# Setting type: Int32
# Default value: 0
Slot6 = {random.randint(0,24)}

# Setting type: Int32
# Default value: 0
Slot7 = {random.randint(0,24)}

# Setting type: Int32
# Default value: 0
Slot8 = {random.randint(0,24)}

# Setting type: Int32
# Default value: 17
Slot9 = {random.randint(0,24)}

# Setting type: Int32
# Default value: 0
Slot10 = {random.randint(0,24)}

# Setting type: Int32
# Default value: 0
Slot11 = {random.randint(0,24)}

# Setting type: Int32
# Default value: 0
Slot12 = {random.randint(0,24)}

# Setting type: Int32
# Default value: 0
Slot13 = {random.randint(0,24)}

# Setting type: Int32
# Default value: 17
Slot14 = {random.randint(0,24)}

# Setting type: Int32
# Default value: 0
Slot15 = {random.randint(0,24)}

# Setting type: Single
# Default value: 0
MinNeutralBenign = 0

# Setting type: Single
# Default value: 0
MaxNeutralBenign = 10

# Setting type: Single
# Default value: 0
MinNeutralEvil = 0

# Setting type: Single
# Default value: 0
MaxNeutralEvil = 10

# Setting type: Single
# Default value: 0
MinNeutralKiller = 0

# Setting type: Single
# Default value: 0
MaxNeutralKiller = 10

# Setting type: Single
# Default value: 0
MinNeutralOutlier = 0

# Setting type: Single
# Default value: 0
MaxNeutralOutlier = 10
""")

    file.write(f"""[TownOfUs.Options.Roles.Crewmate.AltruistOptions]

# Setting type: Int32
# Default value: 1
ReviveMode = {random.randint(0,2)}

# Setting type: Single
# Default value: 0.25
ReviveRange = {random.uniform(0.05,1)}

# Setting type: Single
# Default value: 5
ReviveDuration = {random.uniform(1,15)}

# Setting type: Single
# Default value: 2
MaxRevives = {random.randint(1,5)}

# Setting type: Boolean
# Default value: false
KillOnStartRevive = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
FreezeDuringRevive = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
HideAtBeginningOfRevive = {random.choice(["true", "false"])}

# Setting type: Int32
# Default value: 0
KillersAlertedAtStart = {random.randint(0,3)}

# Setting type: Int32
# Default value: 3
KillersAlertedAtEnd = {random.randint(0,3)}
""")

    file.write(f"""[TownOfUs.Options.Roles.Crewmate.AurialOptions]

# Setting type: Single
# Default value: 0.5
AuraInnerRadius = {random.uniform(0,1)}

# Setting type: Single
# Default value: 1.5
AuraOuterRadius = {random.uniform(1,5)}

# Setting type: Single
# Default value: 10
SenseDuration = {random.uniform(1,15)}
""")

    file.write(f"""[TownOfUs.Options.Roles.Crewmate.ClericOptions]

# Setting type: Single
# Default value: 25
BarrierCooldown = {random.uniform(5,120)}

# Setting type: Single
# Default value: 25
BarrierDuration = {random.uniform(5,120)}

# Setting type: Single
# Default value: 25
CleanseCooldown = {random.uniform(5,120)}

# Setting type: Boolean
# Default value: false
ShowBarrier = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
AttackNotif = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.EngineerOptions]

# Setting type: Single
# Default value: -1
MaxVents = {random.randint(-1,30)}

# Setting type: Single
# Default value: 1
VentPerTasks = {random.randint(0,15)}

# Setting type: Single
# Default value: 15
VentCooldown = {random.uniform(0,25)}

# Setting type: Single
# Default value: 10
VentDuration = {random.uniform(0,25)}

# Setting type: Single
# Default value: 2
MaxFixes = {random.randint(-1,15)}

# Setting type: Single
# Default value: 3
FixPerTasks = {random.randint(0,15)}

# Setting type: Single
# Default value: 0.5
FixDelay = {random.uniform(0,5)}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.ForensicOptions]

# Setting type: Single
# Default value: 25
ExamineCooldown = {random.uniform(5,120)}

# Setting type: Boolean
# Default value: true
ForensicReportOn = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 7.5
ForensicRoleDuration = {random.uniform(0,60)}

# Setting type: Single
# Default value: 30
ForensicFactionDuration = {random.uniform(0,60)}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.HaunterOptions]

# Setting type: Single
# Default value: 3
NumTasksLeftBeforeClickable = {random.randint(0,5)}

# Setting type: Single
# Default value: 1
NumTasksLeftBeforeAlerted = {random.randint(0,15)}

# Setting type: Boolean
# Default value: false
RevealNeutralRoles = {random.choice(["true", "false"])}

# Setting type: Int32
# Default value: 1
HaunterCanBeClickedBy = {random.randint(0,2)}
""")

    file.write(f"""[TownOfUs.Options.Roles.Crewmate.HunterOptions]

# Setting type: Single
# Default value: 25
HunterKillCooldown = {random.uniform(5,120)}

# Setting type: Single
# Default value: 20
HunterStalkCooldown = {random.uniform(1,30)}

# Setting type: Single
# Default value: 25
HunterStalkDuration = {random.uniform(5,60)}

# Setting type: Single
# Default value: 5
StalkUses = {random.randint(-1,30)}

# Setting type: Single
# Default value: 1
StalkPerTasks = {random.randint(0,15)}

# Setting type: Int32
# Default value: 0
StalkTriggeredBy = {random.randint(0,1)}

# Setting type: Boolean
# Default value: true
SeesTypeOfInteraction = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
RetributionOnVote = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
HunterBodyReport = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.ImitatorOptions]

# Setting type: Boolean
# Default value: true
ImitateNeutrals = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
ImitateImpostors = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
ImitateBasicCrewmate = {random.choice(["true", "false"])}

# Setting type: Int32
# Default value: 2
ImitatorGuess = {random.randint(0,2)}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.InvestigatorOptions]

# Setting type: Single
# Default value: 4
FootprintSize = {random.uniform(1,10)}

# Setting type: Single
# Default value: 1
FootprintInterval = {random.uniform(0.5,6)}

# Setting type: Single
# Default value: 10
FootprintDuration = {random.uniform(1,15)}

# Setting type: Boolean
# Default value: false
ShowAnonymousFootprints = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
ShowFootprintVent = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.JailorOptions]

# Setting type: Single
# Default value: 20
JailCooldown = {random.uniform(1,30)}

# Setting type: Single
# Default value: 3
MaxExecutes = {random.randint(1,5)}

# Setting type: Boolean
# Default value: false
JailInARow = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
JaileePublicChat = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.LookoutOptions]

# Setting type: Single
# Default value: 20
WatchCooldown = {random.uniform(1,30)}

# Setting type: Single
# Default value: 5
MaxWatches = {random.randint(1,15)}

# Setting type: Boolean
# Default value: true
LoResetOnNewRound = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
TaskUses = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.MedicOptions]

# Setting type: Int32
# Default value: 2
ShowShielded = {random.randint(0,4)}

# Setting type: Int32
# Default value: 0
WhoGetsNotification = {random.randint(0,4)}

# Setting type: Boolean
# Default value: true
ChangeTarget = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 3
MedicShieldUses = {random.randint(0,15)}

# Setting type: Boolean
# Default value: false
ShieldBreaks = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
ShowReports = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 0
MedicReportNameDuration = {random.uniform(0,60)}

# Setting type: Single
# Default value: 15
MedicReportColorDuration = {random.uniform(0,60)}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.MediumOptions]

# Setting type: Single
# Default value: 10
MediateCooldown = {random.uniform(10,60)}

# Setting type: Single
# Default value: 10
MediateDuration = {random.uniform(5,20)}

# Setting type: Single
# Default value: 10
MediatingSpeed = {random.uniform(1.5,10)}

# Setting type: Single
# Default value: 10
LivingSeeSpiritTimer = {random.uniform(0.5,20)}

PlayerVisibility = {random.randint(0,3)}

ArrowVisibility = {random.randint(0,3)}

WhoIsRevealed = {random.randint(0,3)}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.MirrorcasterOptions]

# Setting type: Int32
# Default value: 1
WhoGetsNotification = {random.randint(0,1)}

# Setting type: Single
# Default value: 0
MirrorCooldown = {random.uniform(0,60)}

# Setting type: Single
# Default value: 30
MirrorDuration = {random.uniform(5,120)}

# Setting type: Single
# Default value: 15
UnleashCooldown = {random.uniform(0,60)}

# Setting type: Int32
# Default value: 1
AttackInformationGiven = {random.randint(0,3)}

# Setting type: Boolean
# Default value: false
MultiUnleash = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 5
MaxMirrors = {random.randint(1,15)}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.MonarchOptions]

# Setting type: Single
# Default value: 20
KnightCooldown = {random.uniform(0,60)}

# Setting type: Single
# Default value: 3
MaxKnights = {random.randint(0,15)}

# Setting type: Single
# Default value: 1
VotesPerKnight = {random.randint(1,5)}

# Setting type: Single
# Default value: 3
KnightDelay = {random.uniform(1,10)}

# Setting type: Boolean
# Default value: true
ShowKnightedVotes = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
FirstRoundUse = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
InformWhenKnightDies = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
CrewKnightsGrantKillImmunity = {random.choice(["true", "false"])}

# Setting type: Int32
# Default value: 0
ProtectionFlashColor = {random.randint(0,5)}
""")
    
    
    file.write(f"""[TownOfUs.Options.Roles.Crewmate.MysticOptions]

# Setting type: Single
# Default value: 0.1
MysticArrowDuration = {random.uniform(0,1)}

# Setting type: Boolean
# Default value: true
MysticHnsPopUp = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.OracleOptions]

# Setting type: Single
# Default value: 20
ConfessCooldown = {random.uniform(1,30)}

# Setting type: Single
# Default value: 25
BlessCooldown = {random.uniform(5,120)}

# Setting type: Single
# Default value: 80
RevealAccuracyPercentage = {random.uniform(0,100)}

# Setting type: Boolean
# Default value: false
ShowNeutralBenignAsEvil = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
ShowNeutralEvilAsEvil = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
ShowNeutralKillingAsEvil = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
ShowNeutralOutlierAsEvil = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.PlumberOptions]

# Setting type: Single
# Default value: 25
FlushCooldown = {random.uniform(5,120)}

# Setting type: Single
# Default value: 25
BlockCooldown = {random.uniform(5,120)}

# Setting type: Single
# Default value: 3
MaxBarricades = {random.randint(1,15)}

# Setting type: Single
# Default value: 2
BarricadeRoundDuration = {random.randint(0,15)}

# Setting type: Boolean
# Default value: true
TaskUses = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.PoliticianOptions]

# Setting type: Single
# Default value: 25
CampaignCooldown = {random.uniform(5,120)}

# Setting type: Boolean
# Default value: true
PreventCampaign = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.ProsecutorOptions]

# Setting type: Boolean
# Default value: true
ExileOnCrewmate = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 2
MaxProsecutions = {random.randint(1,5)}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.SeerOptions]

# Setting type: Boolean
# Default value: true
SalemSeer = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 20
SeerCooldown = {random.uniform(5,120)}

# Setting type: Single
# Default value: 5
MaxCompares = {random.randint(0,15)}

# Setting type: Boolean
# Default value: false
BenignShowFriendlyToAll = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
EvilShowFriendlyToAll = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
OutlierShowFriendlyToAll = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
ShowCrewmateKillingAsRed = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
ShowNeutralBenignAsRed = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
ShowNeutralEvilAsRed = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
ShowNeutralKillingAsRed = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
ShowNeutralOutlierAsRed = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
SwapTraitorColors = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.SentryOptions]

# Setting type: Single
# Default value: 30
PlacementCooldown = {random.uniform(5,120)}

# Setting type: Int32
# Default value: 0
DeployedCamerasVisibility = {random.randint(0,1)}

# Setting type: Single
# Default value: 3
CamerasVisibleAfter = {random.uniform(0,10)}

# Setting type: Boolean
# Default value: false
CanMoveWhilePlacingCameras = {random.choice(["true", "false"])}

# Setting type: Int32
# Default value: 2
PortableCamerasMode = {random.randint(0,2)}

# Setting type: Single
# Default value: 2
InitialCameras = {random.randint(0,16)}

# Setting type: Single
# Default value: 2
CameraRoundsLast = {random.randint(0,15)}

# Setting type: Single
# Default value: 2
TasksPerCamera = {random.randint(0,15)}

# Setting type: Single
# Default value: 4
MaxCamerasPlaced = {random.randint(0,20)}

# Setting type: Single
# Default value: 90
PortableCamsBattery = {random.randint(0,120)}

# Setting type: Single
# Default value: 0
BlindspotsCount = {random.randint(0,10)}

# i have literally no idea what this all means lmao um something for later

# Setting type: Int32
# Default value: 0
Blindspot1Room = 0

# Setting type: Int32
# Default value: 27
Blindspot2Room = 27

# Setting type: Int32
# Default value: 2
Blindspot3Room = 2

# Setting type: Int32
# Default value: 1
Blindspot4Room = 1

# Setting type: Int32
# Default value: 6
Blindspot5Room = 6

# Setting type: Int32
# Default value: 7
Blindspot6Room = 7

# Setting type: Int32
# Default value: 11
Blindspot7Room = 11

# Setting type: Int32
# Default value: 10
Blindspot8Room = 10

# Setting type: Int32
# Default value: 12
Blindspot9Room = 12

# Setting type: Int32
# Default value: 14
Blindspot10Room = 14
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.SheriffOptions]

# Setting type: Single
# Default value: 25
KillCooldown = {random.uniform(5,120)}

# Setting type: Boolean
# Default value: false
SheriffBodyReport = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
FirstRoundUse = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
ShootNeutralBenign = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
ShootNeutralEvil = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
ShootNeutralKiller = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
ShootNeutralOutlier = {random.choice(["true", "false"])}

# Setting type: Int32
# Default value: 0
MisfireType = {random.randint(0,3)}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.SnitchOptions]

# Setting type: Boolean
# Default value: false
SnitchNeutralRoles = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
SnitchSeesTraitor = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
SnitchSeesImpostorsMeetings = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 1
TaskRemainingWhenRevealed = {random.randint(1,3)}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.SonarOptions]

# Setting type: Single
# Default value: 20
TrackCooldown = {random.uniform(1,30)}

# Setting type: Single
# Default value: 5
MaxTracks = {random.randint(1,15)}

# Setting type: Single
# Default value: 5
UpdateInterval = {random.uniform(0,15)}

# Setting type: Boolean
# Default value: true
SoundOnDeactivate = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
ResetOnNewRound = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
TaskUses = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.SpyOptions]

# Setting type: Int32
# Default value: 0
WhoSeesDead = {random.randint(0,3)}

# Setting type: Int32
# Default value: 2
HasPortableAdmin = {random.randint(0,3)}

# Setting type: Boolean
# Default value: true
MoveWithMenu = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 20
StartingCharge = {random.uniform(0,30)}

# Setting type: Single
# Default value: 15
RoundCharge = {random.uniform(0,30)}

# Setting type: Single
# Default value: 10
TaskCharge = {random.uniform(0,30)}

# Setting type: Single
# Default value: 15
DisplayCooldown = {random.uniform(0,30)}

# Setting type: Single
# Default value: 15
DisplayDuration = {random.uniform(0,30)}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.SwapperOptions]

# Setting type: Boolean
# Default value: true
CanButton = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.TimeLordOptions]

# Setting type: Single
# Default value: 30
RewindCooldown = {random.uniform(5,120)}

# Setting type: Single
# Default value: 7.5
RewindHistorySeconds = {random.uniform(1,15)}

# Setting type: Single
# Default value: 3
MaxUses = {random.randint(-1,15)}

# Setting type: Single
# Default value: 3
UsesPerTasks = {random.randint(0,15)}

# Setting type: Boolean
# Default value: false
CanUseVitals = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
ReviveOnRewind = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
UndoTasksOnRewind = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
UncleanBodiesOnRewind = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
NotifyOnRevive = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.TransporterOptions]

# Setting type: Single
# Default value: 25
TransporterCooldown = {random.uniform(5,120)}

# Setting type: Single
# Default value: 5
MaxNumTransports = {random.randint(1,15)}

# Setting type: Boolean
# Default value: true
MoveWithMenu = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
CanUseVitals = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
TaskUses = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.TrapperOptions]

# Setting type: Single
# Default value: 20
TrapCooldown = {random.uniform(1,30)}

# Setting type: Single
# Default value: 5
MinAmountOfTimeInTrap = {random.uniform(0,15)}

# Setting type: Single
# Default value: 5
MaxTraps = {random.randint(1,15)}

# Setting type: Single
# Default value: 0.25
TrapSize = {random.uniform(0.05,1)}

# Setting type: Boolean
# Default value: true
TrapsRemoveOnNewRound = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: false
TaskUses = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 3
MinAmountOfPlayersInTrap = {random.randint(1,15)}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.VeteranOptions]

# Setting type: Single
# Default value: 25
AlertCooldown = {random.uniform(5,120)}

# Setting type: Single
# Default value: 10
AlertDuration = {random.uniform(5,15)}

# Setting type: Single
# Default value: 5
MaxNumAlerts = {random.randint(1,15)}

# Setting type: Boolean
# Default value: false
KilledOnAlert = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
KnowWhenAttackedInMeeting = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
TaskUses = {random.choice(["true", "false"])}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.VigilanteOptions]

# Setting type: Single
# Default value: 5
VigilanteKills = {random.randint(1,15)}

# Setting type: Boolean
# Default value: true
VigilanteMultiKill = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
VigilanteGuessNeutralBenign = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
VigilanteGuessNeutralEvil = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
VigilanteGuessNeutralKilling = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
VigilanteGuessNeutralOutlier = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
VigilanteGuessKillerMods = {random.choice(["true", "false"])}

# Setting type: Boolean
# Default value: true
VigilanteGuessAlliances = {random.choice(["true", "false"])}

# Setting type: Single
# Default value: 3
MultiShots = {random.randint(0,3)}
""")


    file.write(f"""[TownOfUs.Options.Roles.Crewmate.WardenOptions]

# Setting type: Int32
# Default value: 2
ShowFortified = {random.randint(0,3)}
""")


print("Finished randomizing")

