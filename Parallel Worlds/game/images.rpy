## FILE: game/images.rpy
## Explicit Ren'Py image definitions for all characters.
## - Gender-dynamic characters use ConditionSwitch (evaluates at display time)
## - Missing expressions alias to the nearest existing one
## - Characters with incomplete expression sets alias to the nearest existing one

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
## MORGAN
## ==========================================

image morgan neutral    = "images/characters/morgan/neutral.png"
image morgan serious    = "images/characters/morgan/serious.png"
image morgan frustrated = "images/characters/morgan/frustrated.png"
image morgan listening  = "images/characters/morgan/listening.png"
image morgan happy      = "images/characters/morgan/happy.png"
image morgan sad        = "images/characters/morgan/sad.png"

## Aliases
image morgan quiet      = "images/characters/morgan/sad.png"
image morgan nervous    = "images/characters/morgan/worried.png"
image morgan worried    = "images/characters/morgan/worried.png"
image morgan relieved   = "images/characters/morgan/happy.png"

## ==========================================
## ANCHOR
## ==========================================

image anchor neutral   = "images/characters/anchor/neutral.png"
image anchor serious   = "images/characters/anchor/serious.png"
image anchor listening = "images/characters/anchor/listening.png"

## Aliases
image anchor quiet     = "images/characters/anchor/sad.png"

## ==========================================
## PARENT
## ==========================================

image parent neutral    = "images/characters/parent/neutral.png"
image parent serious    = "images/characters/parent/serious.png"
image parent angry      = "images/characters/parent/angry.png"
image parent suspicious = "images/characters/parent/suspicious.png"
image parent frustrated = "images/characters/parent/frustrated.png"
image parent listening  = "images/characters/parent/listening.png"

## ==========================================
## BACKGROUNDS
## (Defined here as well so any missing bg shows black rather than crashing)
## ==========================================

image bg campus_day           = "images/bg/campus_day.png"
image bg library_steps_evening = "images/bg/library_steps_evening.png"
image bg cafe                 = "images/bg/cafe.png"
image bg rooftop_night        = "images/bg/rooftop_night.png"
image bg dean_office          = "images/bg/dean_office.png"
image bg room_night           = "gui/main_menu.png"
image bg phone_screen         = "images/bg/phone_screen.png"
image bg kitchen_morning      = "images/bg/kitchen_morning.png"
image bg unknown_location     = "images/bg/unknown_location.png"

image white = Solid("#ffffff")
