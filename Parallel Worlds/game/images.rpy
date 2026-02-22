## FILE: game/images.rpy
## Explicit Ren'Py image definitions for all characters.
## - Gender-dynamic characters use ConditionSwitch (evaluates at display time)
## - Missing expressions alias to the nearest existing one
## - Characters without sprite folders yet show Null() so game doesn't crash

## ==========================================
## JORDAN (single folder, gender doesn't change)
## ==========================================

image jordan neutral    = "images/characters/jordan/neutral.png"
image jordan serious    = "images/characters/jordan/serious.png"
image jordan angry      = "images/characters/jordan/angry.png"
image jordan happy      = "images/characters/jordan/happy.png"
image jordan sad        = "images/characters/jordan/sad.png"
image jordan frustrated = "images/characters/jordan/frustrated.png"
image jordan suspicious = "images/characters/jordan/suspicious.png"
image jordan worried    = "images/characters/jordan/worried.png"
image jordan listening  = "images/characters/jordan/listening.png"
## Aliases (expressions used in scripts that map to existing files)
image jordan quiet      = "images/characters/jordan/sad.png"

## ==========================================
## CASEY (gender-dynamic: female or male)
## ==========================================

image casey neutral = ConditionSwitch(
    "casey_gender == 'female'", "images/characters/casey_female/neutral.png",
    "True",                     "images/characters/casey_male/neutral.png")

image casey serious = ConditionSwitch(
    "casey_gender == 'female'", "images/characters/casey_female/serious.png",
    "True",                     "images/characters/casey_male/serious.png")

image casey angry = ConditionSwitch(
    "casey_gender == 'female'", "images/characters/casey_female/angry.png",
    "True",                     "images/characters/casey_male/angry.png")

image casey frustrated = ConditionSwitch(
    "casey_gender == 'female'", "images/characters/casey_female/frustrated.png",
    "True",                     "images/characters/casey_male/frustrated.png")

image casey suspicious = ConditionSwitch(
    "casey_gender == 'female'", "images/characters/casey_female/suspicious.png",
    "True",                     "images/characters/casey_male/suspicious.png")

image casey worried = ConditionSwitch(
    "casey_gender == 'female'", "images/characters/casey_female/worried.png",
    "True",                     "images/characters/casey_male/worried.png")

image casey listening = ConditionSwitch(
    "casey_gender == 'female'", "images/characters/casey_female/listening.png",
    "True",                     "images/characters/casey_male/listening.png")

image casey happy = ConditionSwitch(
    "casey_gender == 'female'", "images/characters/casey_female/happy.png",
    "True",                     "images/characters/casey_male/happy.png")

image casey sad = ConditionSwitch(
    "casey_gender == 'female'", "images/characters/casey_female/sad.png",
    "True",                     "images/characters/casey_male/sad.png")

## Aliases
image casey concerned = ConditionSwitch(
    "casey_gender == 'female'", "images/characters/casey_female/worried.png",
    "True",                     "images/characters/casey_male/worried.png")

image casey quiet = ConditionSwitch(
    "casey_gender == 'female'", "images/characters/casey_female/sad.png",
    "True",                     "images/characters/casey_male/sad.png")

image casey relieved = ConditionSwitch(
    "casey_gender == 'female'", "images/characters/casey_female/happy.png",
    "True",                     "images/characters/casey_male/happy.png")

## ==========================================
## RILEY (gender-dynamic: female or male)
## ==========================================

image riley neutral = ConditionSwitch(
    "riley_gender == 'female'", "images/characters/riley_female/neutral.png",
    "True",                     "images/characters/riley_male/neutral.png")

image riley serious = ConditionSwitch(
    "riley_gender == 'female'", "images/characters/riley_female/serious.png",
    "True",                     "images/characters/riley_male/serious.png")

image riley angry = ConditionSwitch(
    "riley_gender == 'female'", "images/characters/riley_female/angry.png",
    "True",                     "images/characters/riley_male/angry.png")

image riley frustrated = ConditionSwitch(
    "riley_gender == 'female'", "images/characters/riley_female/frustrated.png",
    "True",                     "images/characters/riley_male/frustrated.png")

image riley suspicious = ConditionSwitch(
    "riley_gender == 'female'", "images/characters/riley_female/suspicious.png",
    "True",                     "images/characters/riley_male/suspicious.png")

image riley worried = ConditionSwitch(
    "riley_gender == 'female'", "images/characters/riley_female/worried.png",
    "True",                     "images/characters/riley_male/worried.png")

image riley listening = ConditionSwitch(
    "riley_gender == 'female'", "images/characters/riley_female/listening.png",
    "True",                     "images/characters/riley_male/listening.png")

image riley happy = ConditionSwitch(
    "riley_gender == 'female'", "images/characters/riley_female/happy.png",
    "True",                     "images/characters/riley_male/happy.png")

image riley sad = ConditionSwitch(
    "riley_gender == 'female'", "images/characters/riley_female/sad.png",
    "True",                     "images/characters/riley_male/sad.png")

## Aliases
image riley quiet = ConditionSwitch(
    "riley_gender == 'female'", "images/characters/riley_female/sad.png",
    "True",                     "images/characters/riley_male/sad.png")

## ==========================================
## MORGAN (gender-dynamic: needs morgan_male / morgan_female folders)
## Shows Null() until sprite folders are created — game won't crash.
## ==========================================

image morgan neutral   = ConditionSwitch(
    "morgan_gender == 'female'", "images/characters/morgan_female/neutral.png",
    "True",                      "images/characters/morgan_male/neutral.png")

image morgan serious   = ConditionSwitch(
    "morgan_gender == 'female'", "images/characters/morgan_female/serious.png",
    "True",                      "images/characters/morgan_male/serious.png")

image morgan frustrated = ConditionSwitch(
    "morgan_gender == 'female'", "images/characters/morgan_female/frustrated.png",
    "True",                      "images/characters/morgan_male/frustrated.png")

image morgan listening = ConditionSwitch(
    "morgan_gender == 'female'", "images/characters/morgan_female/listening.png",
    "True",                      "images/characters/morgan_male/listening.png")

image morgan happy     = ConditionSwitch(
    "morgan_gender == 'female'", "images/characters/morgan_female/happy.png",
    "True",                      "images/characters/morgan_male/happy.png")

image morgan sad       = ConditionSwitch(
    "morgan_gender == 'female'", "images/characters/morgan_female/sad.png",
    "True",                      "images/characters/morgan_male/sad.png")

## Aliases
image morgan quiet     = ConditionSwitch(
    "morgan_gender == 'female'", "images/characters/morgan_female/sad.png",
    "True",                      "images/characters/morgan_male/sad.png")

image morgan nervous   = ConditionSwitch(
    "morgan_gender == 'female'", "images/characters/morgan_female/worried.png",
    "True",                      "images/characters/morgan_male/worried.png")

image morgan worried   = ConditionSwitch(
    "morgan_gender == 'female'", "images/characters/morgan_female/worried.png",
    "True",                      "images/characters/morgan_male/worried.png")

image morgan relieved  = ConditionSwitch(
    "morgan_gender == 'female'", "images/characters/morgan_female/happy.png",
    "True",                      "images/characters/morgan_male/happy.png")

## ==========================================
## ANCHOR (gender-dynamic: needs anchor_male / anchor_female folders)
## ==========================================

image anchor neutral   = ConditionSwitch(
    "anchor_gender == 'female'", "images/characters/anchor_female/neutral.png",
    "True",                      "images/characters/anchor_male/neutral.png")

image anchor serious   = ConditionSwitch(
    "anchor_gender == 'female'", "images/characters/anchor_female/serious.png",
    "True",                      "images/characters/anchor_male/serious.png")

image anchor listening = ConditionSwitch(
    "anchor_gender == 'female'", "images/characters/anchor_female/listening.png",
    "True",                      "images/characters/anchor_male/listening.png")

## Aliases
image anchor quiet     = ConditionSwitch(
    "anchor_gender == 'female'", "images/characters/anchor_female/sad.png",
    "True",                      "images/characters/anchor_male/sad.png")

## ==========================================
## PARENT (needs parent/ folder — Null until created)
## ==========================================

image parent neutral    = Null()
image parent serious    = Null()
image parent angry      = Null()
image parent suspicious = Null()
image parent frustrated = Null()
image parent listening  = Null()

## ==========================================
## BACKGROUNDS
## (Defined here as well so any missing bg shows black rather than crashing)
## ==========================================

image bg campus_day           = "images/bg/campus_day.png"
image bg library_steps_evening = "images/bg/library_steps_evening.png"
image bg cafe                 = "images/bg/cafe.png"
image bg rooftop_night        = "images/bg/rooftop_night.png"
image bg dean_office          = "images/bg/dean_office.png"
