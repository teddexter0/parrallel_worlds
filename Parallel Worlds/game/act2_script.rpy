## FILE: game/act2_script.rpy
## ACT 2: THE UNRAVELING
## Chapters 2-3: The truth surfaces, characters take sides, Riley is revealed.

## ==========================================
## ACT 2 OPENING
## ==========================================

label act2_opening:

    $ current_chapter = 2
    $ current_act = 2

    scene black with dissolve
    pause 1.0

    centered "ACT 2: THE UNRAVELING"
    pause 2.0

    scene bg campus_day
    play music "audio/music/ambient_city.mp3" fadein 2.0

    show screen game_hud

    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act2_open.mp3"

    "The next morning hits like a wall of light."
    "Campus looks the same."
    "But everything feels different."

    pause 1.0

    "You slept two hours. Maybe three."
    "Your head keeps replaying the same question:"
    "Who knows?"

    pause 1.5

    jump act2_scene_campus_walk


## ==========================================
## SCENE 2.1 — CAMPUS WALK
## ==========================================

label act2_scene_campus_walk:

    scene bg campus_day
    play music "audio/music/ambient_city.mp3"

    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act2_campus.mp3"

    "The quad is busy."
    "Groups of students. Laughter. Coffee cups."
    "You feel completely outside of all of it."

    pause 1.0

    show jordan neutral at left

    "Then you see Jordan."
    "[jordan_pronoun_subject.capitalize()] spots you at the same moment."

    pause 0.5

    "Neither of you moves first."

    menu:
        "What do you do?"

        "Walk toward Jordan":
            jump act2_approach_jordan

        "Look away and keep walking":
            jump act2_avoid_jordan


label act2_approach_jordan:

    $ jordan_relationship += 5
    $ truth += 5
    $ remember("act2_jordan_campus", "approached")

    "You cross the quad."
    "Jordan's expression doesn't change until you're two feet away."

    jordan "Hey."
    "That's it. Just 'hey'."

    player "Hey."

    pause 1.0

    jordan "You look terrible."
    player "Didn't sleep."
    jordan "Yeah."

    pause 1.0

    jordan "Me neither."

    "A beat. Something hangs between you."

    jordan "You got the messages too?"
    player "What messages?"
    jordan "Don't."

    show jordan serious

    jordan "Just... don't. Not with me."

    pause 1.0

    "You realize Jordan knows more than [jordan_pronoun_subject] is saying."

    $ insights_unlocked.append("Jordan is involved in whatever happened")
    show screen insight_popup("Jordan is involved in whatever happened")
    pause
    hide screen insight_popup

    jump act2_jordan_campus_end


label act2_avoid_jordan:

    $ jordan_relationship -= 10
    $ mask += 5
    $ remember("act2_jordan_campus", "avoided")

    "You turn your eyes to your phone."
    "Pretend to read something."
    "Walk past."

    pause 1.0

    "Jordan doesn't call after you."
    "That's almost worse."

    pause 1.0

    "You feel [jordan_pronoun_possessive] eyes on your back all the way to the library steps."

    jump act2_jordan_campus_end


label act2_jordan_campus_end:

    hide jordan with dissolve
    pause 0.5

    "Six hours until the library steps meeting."
    "You need to get through the day first."

    jump act2_scene_casey_confrontation


## ==========================================
## SCENE 2.2 — CASEY FINDS YOU
## ==========================================

label act2_scene_casey_confrontation:

    scene bg cafe
    play music "audio/music/ambient_city.mp3"
    play sound "audio/sfx/cafe_ambience.mp3"

    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act2_casey.mp3"

    "You find a corner of the campus café."
    "Coffee. Headphones. Your own head."
    "You need twenty minutes to think."

    pause 1.0

    "You don't get them."

    show casey neutral at right

    play sound "audio/sfx/chair_scrape.mp3"

    casey "I've been texting you."

    menu:
        "You respond:"

        "I know. Sorry. It's been a lot.":
            jump casey_conf_honest

        "I haven't checked my phone.":
            jump casey_conf_deflect

        "I was going to reply. What's up?":
            jump casey_conf_casual


label casey_conf_honest:

    $ casey_relationship += 10
    $ truth += 5
    $ mask -= 5

    player "I know. Sorry. It's been a lot."

    show casey concerned

    casey "Yeah. I can see that."
    pause 0.5
    casey "What's going on?"

    jump casey_conf_pressure


label casey_conf_deflect:

    $ mask += 10
    $ casey_relationship -= 5

    player "I haven't checked my phone."

    show casey suspicious

    casey "Really."
    pause 0.5
    casey "I sent you four messages."

    player "I've been busy."

    casey "Everyone's been busy. That's not what I'm talking about."

    jump casey_conf_pressure


label casey_conf_casual:

    $ mask += 5
    $ casey_relationship += 5

    player "I was going to reply. What's up?"

    show casey serious

    casey "Don't do that."
    pause 0.5
    casey "Don't act like everything's normal."

    jump casey_conf_pressure


label casey_conf_pressure:

    show casey serious

    casey "People are talking."
    pause 0.5
    casey "They're saying you were there."

    "Your coffee cup stops halfway to your lips."

    player "There where?"

    casey "The library. Two months ago."
    pause 0.5
    casey "The night Morgan and Jordan—"

    "[casey_pronoun_subject.capitalize()] stops."

    casey "You were there. Weren't you."

    pause 1.5

    "It's not a question."

    menu:
        "What do you tell Casey?"

        "Yes. I was there.":
            jump casey_conf_admit

        "I don't know what you've heard.":
            jump casey_conf_vague

        "Who told you that?":
            jump casey_conf_redirect


label casey_conf_admit:

    $ casey_relationship += 15
    $ truth += 10
    $ mask -= 10
    $ remember("casey_secret_shared", True)

    player "Yeah."
    pause 0.5
    player "I was there."

    show casey quiet

    casey "Okay."
    pause 1.0
    casey "Okay. That's... okay."

    "You wait for [casey_pronoun_object] to ask more."
    "[casey_pronoun_subject.capitalize()] doesn't."

    casey "Are you in trouble?"

    player "I don't know yet."

    casey "Then I'm staying close."

    $ insights_unlocked.append("Casey would rather know hard truths than comfortable lies")
    show screen insight_popup("Casey would rather know hard truths than comfortable lies")
    pause
    hide screen insight_popup

    jump casey_conf_end


label casey_conf_vague:

    $ mask += 10
    $ casey_relationship -= 5

    player "I don't know what you've heard."

    show casey frustrated

    casey "I've heard your name. That's what I've heard."
    pause 0.5
    casey "From more than one person."

    player "People talk."

    casey "Yeah. They do."

    pause 1.0

    casey "I just hope you're not hiding something from me."

    jump casey_conf_end


label casey_conf_redirect:

    $ ambition += 5
    $ mask += 5

    player "Who told you that?"

    show casey neutral

    casey "Does it matter?"
    pause 0.5
    casey "The point is people know. Or think they know."

    player "What exactly are they saying?"

    casey "That you saw something. And stayed quiet."

    pause 1.0

    "The accuracy of that lands heavier than [casey_pronoun_subject] probably intended."

    jump casey_conf_end


label casey_conf_end:

    show casey neutral

    casey "Just... be careful, okay?"
    pause 0.5
    casey "Whatever this is."

    "[casey_pronoun_subject.capitalize()] stands. Squeezes your shoulder."
    "Then [casey_pronoun_subject] leaves."

    hide casey with dissolve

    pause 1.0

    "Three hours until the library steps."

    jump act2_scene_morgan_text


## ==========================================
## SCENE 2.3 — MORGAN'S WARNING (via text)
## ==========================================

label act2_scene_morgan_text:

    scene bg campus_day

    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act2_morgan.mp3"

    play sound "audio/sfx/phone_buzz.mp3"
    pause 0.3
    play sound "audio/sfx/phone_buzz.mp3"

    show screen notification_popup("Morgan", "We need to talk. But not here.")
    pause 2.0
    hide screen notification_popup

    scene bg phone_screen
    play sound "audio/sfx/phone_unlock.mp3"
    pause 0.3

    nvl clear
    "MORGAN" "{size=14}2:14 PM{/size}"
    "MORGAN" "we need to talk"
    "MORGAN" "{size=14}2:15 PM{/size}"
    "MORGAN" "but not on campus"
    "MORGAN" "{size=14}2:16 PM{/size}"
    "MORGAN" "and not tonight"
    "MORGAN" "{size=14}2:17 PM{/size}"
    "MORGAN" "whatever you're planning - don't."
    nvl clear

    scene bg campus_day

    "Don't."
    pause 1.0
    "Morgan knows about the meeting."
    pause 0.5
    "Or suspects."
    pause 1.0

    menu:
        "How do you reply to Morgan?"

        "Why not? What do you know?":
            jump morgan_text_probe

        "I'll reach out tomorrow.":
            jump morgan_text_delay

        "Don't reply.":
            jump morgan_text_ignore


label morgan_text_probe:

    $ truth += 5
    $ morgan_relationship += 5

    scene bg phone_screen

    nvl clear
    "YOU" "{size=14}2:19 PM{/size}"
    "YOU" "why not? what do you know?"
    pause 1.5
    "MORGAN" "{size=14}2:22 PM{/size}"
    "MORGAN" "enough."
    "MORGAN" "{size=14}2:23 PM{/size}"
    "MORGAN" "just trust me on this."
    nvl clear

    scene bg campus_day

    "Trust Morgan."
    "After two months of silence."

    jump morgan_text_end


label morgan_text_delay:

    $ mask += 5

    scene bg phone_screen

    nvl clear
    "YOU" "{size=14}2:19 PM{/size}"
    "YOU" "i'll reach out tomorrow"
    pause 1.5
    "MORGAN" "{size=14}2:21 PM{/size}"
    "MORGAN" "please do."
    nvl clear

    scene bg campus_day

    jump morgan_text_end


label morgan_text_ignore:

    $ ambition += 5
    $ morgan_relationship -= 10

    scene bg campus_day

    "You put your phone away without replying."
    "Morgan doesn't text again."

    jump morgan_text_end


label morgan_text_end:

    $ active_threads.append("Morgan's Warning")

    "One hour until the library steps."

    jump act2_scene_riley_reveal


## ==========================================
## SCENE 2.4 — THE LIBRARY STEPS: RILEY REVEALED
## ==========================================

label act2_scene_riley_reveal:

    scene bg library_steps_evening
    play music "audio/music/tension_rising.mp3" fadein 2.0

    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act2_riley.mp3"

    "6 PM."
    "The library steps are mostly empty."
    "Students heading to dinner. Lights coming on across campus."

    pause 1.0

    "Someone is already there."

    show riley neutral at center

    "Younger than you expected."
    "Watching you like [riley_pronoun_subject] calculated exactly how long it would take you to walk over."

    riley "You came."

    player "You said you're not my enemy."

    riley "I'm not."

    pause 1.0

    riley "My name is Riley."

    player "Were you one of the messages?"

    riley "I was the message."

    "The unknown number."

    pause 1.0

    riley "I was in the library that night too."
    pause 0.5
    riley "I saw you watching them."
    pause 0.5
    riley "Then I saw you leave."

    "Your jaw tightens."

    player "So you've been watching me."

    riley "I've been waiting for you to do the right thing."
    pause 0.5
    riley "You haven't."

    menu:
        "How do you respond to Riley?"

        "What right thing? You don't know the full story.":
            jump riley_pushback

        "What do you want from me?":
            jump riley_direct

        "Why didn't you just report it yourself?":
            jump riley_deflect


label riley_pushback:

    $ truth += 5
    $ riley_relationship += 5

    player "You don't know the full story."

    show riley serious

    riley "Then tell me."

    pause 1.0

    riley "I've got time."

    jump riley_reveal_full


label riley_direct:

    $ ambition += 5
    $ riley_relationship += 5

    player "What do you want from me?"

    show riley neutral

    riley "Same thing you want."
    pause 0.5
    riley "For this to be over."

    pause 1.0

    riley "But it won't be. Not unless someone talks."

    jump riley_reveal_full


label riley_deflect:

    $ truth += 5

    player "Why didn't you just report it yourself?"

    show riley quiet

    riley "I tried."
    pause 1.0
    riley "They said I needed a corroborating witness."
    pause 0.5
    riley "They said one student's word against a professor with fifteen years tenure wasn't enough."

    pause 1.0

    riley "So here I am. Asking you."

    jump riley_reveal_full


label riley_reveal_full:

    show riley serious

    riley "Professor Harkins."
    pause 0.5
    riley "Two months ago, Jordan found proof."
    pause 0.5
    riley "Grade changes. Twelve students. Three years."

    "The words land one at a time."

    riley "Some paid. Cash. Through a tutoring front."
    pause 0.5
    riley "Some... didn't pay with money."

    pause 1.5

    "The silence after that sentence is very loud."

    $ insights_unlocked.append("The corruption is worse than you assumed")
    show screen insight_popup("The corruption is worse than you assumed")
    pause
    hide screen insight_popup

    riley "Jordan showed Morgan the evidence."
    pause 0.5
    riley "Morgan wanted to use it as leverage."
    pause 0.5
    riley "Jordan wanted to report it."
    pause 0.5
    riley "You walked in on that argument."
    pause 0.5
    riley "And then you walked out."

    pause 1.5

    "You did."
    "You remember it now."
    "Library. 11 PM. Two months ago."
    "You told yourself it wasn't your business."

    $ remember("memory_trigger", "confirmed")
    $ remember("secret_type", "witness_harkins")

    pause 1.0

    riley "I'm not asking you to be a hero."
    pause 0.5
    riley "I'm asking you to tell the truth."

    menu:
        "What do you say to Riley?"

        "I'll think about it.":
            jump riley_response_maybe

        "I'm in. What do I need to do?":
            jump riley_response_yes

        "I can't be involved in this.":
            jump riley_response_no


label riley_response_maybe:

    $ remember("riley_commitment", "undecided")
    $ riley_relationship += 10

    player "I need to think."

    show riley neutral

    riley "Fair."
    pause 0.5
    riley "But I go to the dean at the end of the week."
    pause 0.5
    riley "With or without you."

    jump riley_scene_end


label riley_response_yes:

    $ truth += 15
    $ remember("riley_commitment", "agreed")
    $ riley_relationship += 20
    $ active_threads.append("Agreeing to Testify")

    player "I'm in. What do I need to do?"

    show riley quiet

    riley "Just tell them what you saw."
    pause 0.5
    riley "Exactly what you saw."
    pause 1.0
    riley "Don't add. Don't subtract."

    jump riley_scene_end


label riley_response_no:

    $ mask += 15
    $ remember("riley_commitment", "refused")
    $ riley_relationship -= 15

    player "I can't be involved in this."

    show riley serious

    riley "You're already involved."
    pause 1.0
    riley "You were involved the night you walked away."

    "That hits."

    $ insights_unlocked.append("Silence is its own kind of choice")
    show screen insight_popup("Silence is its own kind of choice")
    pause
    hide screen insight_popup

    jump riley_scene_end


label riley_scene_end:

    hide riley with dissolve

    stop music fadeout 2.0
    play music "audio/music/ambient_city.mp3" fadein 2.0

    pause 1.0

    "Riley walks away."
    "Campus goes quiet around you."
    "The library doors are still lit."

    pause 1.0

    "You think about the night two months ago."
    "What you saw."
    "What you should have done."

    pause 1.5

    jump act2_scene_anchor


## ==========================================
## SCENE 2.5 — THE ANCHOR
## ==========================================

label act2_scene_anchor:

    $ anchor_relationship = 30

    scene bg rooftop_night
    play music "audio/music/ambient_city.mp3"

    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act2_anchor.mp3"

    "You end up on the roof of the humanities building."
    "You don't know why. You just kept walking up stairs."

    pause 1.0

    "Someone is already there."

    show anchor neutral at right

    "Older. Grad student maybe. Sitting with coffee and a book like the world isn't on fire."

    pause 0.5

    anchor "You look like someone who just got handed something they didn't ask for."

    player "Is it that obvious?"

    show anchor quiet

    anchor "No. It's just a very specific look."
    pause 0.5
    anchor "Sit. If you want."

    menu:
        "Do you sit?"

        "Yes.":
            jump anchor_sit_yes
        "No — you leave.":
            jump anchor_sit_no


label anchor_sit_no:

    $ mask += 5

    "You nod. Don't sit. Start back toward the stairs."

    anchor "It doesn't get easier by yourself, you know."

    "You stop."

    player "You don't know me."

    anchor "True."
    pause 0.5
    anchor "Come back if you change your mind."

    jump anchor_end


label anchor_sit_yes:

    $ anchor_relationship += 20

    "You sit."

    anchor "I'm the Anchor. Long story."

    player "What kind of name is that?"

    anchor "The kind you get when people keep coming to you to not drift away."
    pause 1.0
    anchor "What's yours?"

    player "[persistent.player_name]."

    anchor "So. [persistent.player_name]. What's the shape of it?"

    player "What?"

    anchor "Whatever you're carrying."
    pause 0.5
    anchor "It has a shape. Describe the shape."

    pause 1.0

    menu:
        "You describe it:"

        "Like something I should've done and didn't.":
            jump anchor_guilt_path

        "Like everyone wants something from me and I don't know who's right.":
            jump anchor_pressure_path

        "Like I know the right thing but it could ruin me.":
            jump anchor_cost_path


label anchor_guilt_path:

    $ truth += 5
    $ anchor_relationship += 10

    player "Like something I should've done and didn't."

    show anchor listening

    anchor "Guilt. Good shape to know."
    pause 1.0
    anchor "Guilt means you still have a standard."
    pause 0.5
    anchor "The question is what you do with it."

    jump anchor_end


label anchor_pressure_path:

    $ ambition += 5
    $ anchor_relationship += 10

    player "Like everyone wants something from me and I don't know who's right."

    show anchor listening

    anchor "That's not their job to resolve."
    pause 0.5
    anchor "What do you want?"
    pause 1.0
    anchor "Not what's safe. What do you actually want?"

    "You don't answer right away."
    "That tells you something."

    jump anchor_end


label anchor_cost_path:

    $ truth += 10
    $ anchor_relationship += 15

    player "Like I know the right thing but it could ruin me."

    show anchor serious

    anchor "Then you know more than most people."
    pause 1.0
    anchor "Most people convince themselves they don't know."
    pause 0.5
    anchor "Makes it easier."

    player "That's not helpful."

    anchor "No. It's just true."
    pause 0.5
    anchor "Helpful comes later."

    jump anchor_end


label anchor_end:

    show anchor neutral

    anchor "Come find me again."
    pause 0.5
    anchor "I'm usually up here."

    hide anchor with dissolve

    pause 1.0

    "City lights below."
    "Somewhere out there, Professor Harkins is having a normal evening."
    "Somewhere out there, Riley is preparing [riley_pronoun_possessive] case."
    "Somewhere, Jordan is angry."
    "Morgan is scared."
    "Casey is worried about you."

    pause 1.5

    "And you're up here."
    "Deciding who you are."

    pause 1.0

    jump act2_chapter_end


## ==========================================
## END OF ACT 2 / CHAPTER 2
## ==========================================

label act2_chapter_end:

    scene black with dissolve
    stop music fadeout 2.0
    pause 1.0

    show screen records_sidebar

    centered "CHAPTER 2 COMPLETE"
    pause 1.0
    centered "The investigation is now formal."
    pause 1.0
    centered "The university has announced a review of Professor Harkins."

    pause 2.0

    hide screen records_sidebar

    $ current_chapter = 3
    $ renpy.save("act2_checkpoint")

    jump act3_opening
