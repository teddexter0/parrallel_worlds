## FILE: game/act3_script.rpy
## ACT 3: THE CHOICE
## Chapters 3-4: University summons, the evidence revealed, the major decision.

## ==========================================
## ACT 3 OPENING
## ==========================================

label act3_opening:

    $ current_chapter = 3
    $ current_act = 3

    scene black with dissolve
    pause 1.0

    centered "ACT 3: THE CHOICE"
    pause 2.0

    scene bg campus_day
    play music "audio/music/ambient_city.wav" fadein 2.0

    show screen game_hud

    if persistent.narrator_enabled:
        pass

# voice "audio/narration/[persistent.narrator_voice]/act3_open.mp3"

    "Three days have passed."
    "The university posted a notice. A 'formal review of academic conduct.'"
    "No names. Just the department. Just the dates."
    "But everyone on campus knows."


    "And then your student email pings."

    play sound "audio/sfx/phone_buzz.wav"
    pause 0.5

    show screen notification_popup("Dean's Office", "Requested attendance: Friday 10 AM")
    pause 2.5
    hide screen notification_popup

    "They want you there."
    "Not as a suspect."
    "As a witness."

    pause 1.0

    $ active_threads.append("University Summons - Friday 10 AM")

    jump act3_scene_morgan_meetup


## ==========================================
## SCENE 3.1 — MORGAN MEETS YOU
## ==========================================

label act3_scene_morgan_meetup:

    scene bg cafe
    play music "audio/music/ambient_city.wav"
    play sound "audio/sfx/cafe_ambience.wav"

    if persistent.narrator_enabled:
        pass

# voice "audio/narration/[persistent.narrator_voice]/act3_morgan.mp3"

    "Morgan finds you before you find [morgan_pronoun_object]."
    "Back corner booth. Hands around a cup that's been empty for a while."

    show morgan nervous at left

    morgan "You got the summons."

    "It's not a question."

    player "Yeah."

    morgan "Me too."
    morgan "Jordan too."

    pause 0.5

    show morgan serious

    morgan "I need you to understand something."
    morgan "Before you go in there."

    menu:
        "You respond:"

        "I'm listening.":
            jump morgan_reveal_listen

        "Depends what you're about to say.":
            jump morgan_reveal_cautious

        "Whatever you're about to say, it won't change what I saw.":
            jump morgan_reveal_firm


label morgan_reveal_listen:

    $ morgan_relationship += 10
    $ truth += 5

    player "I'm listening."

    show morgan neutral

    morgan "Good."

    jump morgan_reveals_evidence


label morgan_reveal_cautious:

    $ ambition += 5
    $ morgan_relationship += 5

    player "Depends what you're about to say."

    show morgan neutral

    morgan "Fair."
    morgan "It's just... context."

    jump morgan_reveals_evidence


label morgan_reveal_firm:

    $ truth += 10
    $ morgan_relationship -= 10

    player "Whatever you're about to say won't change what I saw."

    show morgan frustrated

    morgan "I'm not asking you to lie."
    morgan "I'm asking you to understand why I did what I did."

    jump morgan_reveals_evidence


label morgan_reveals_evidence:

    show morgan serious

    morgan "I was the one who found the evidence."
    morgan "Harkins' grading files. The payment records. All of it."
    morgan "I found it by accident. I was doing research for [morgan_pronoun_possessive] seminar and..."

    "[morgan_pronoun_subject.capitalize()] trails off."

    morgan "It's a lot. More than I expected."

    "You already know what it is. Riley told you."
    "But you let Morgan say it."

    morgan "Twelve students. Three years."
    morgan "Some of them — some of them weren't paying with money."

    pause 1.5

    show morgan quiet

    morgan "I panicked."
    morgan "I thought — if I had something this big, maybe I could protect myself."
    morgan "Maybe I could make sure nothing like that ever happened to me."


    "Something shifts in your chest."

    $ insights_unlocked.append("Morgan was trying to protect themselves, not just cause harm")
    call screen insight_popup("Morgan was trying to protect themselves, not just cause harm")

    player "You were scared."

    show morgan neutral

    morgan "Still am."


    morgan "Jordan wanted to go straight to the dean."
    morgan "And Jordan was right. I know that now."
    morgan "But I froze."


    morgan "I just need you to tell them the truth about what you saw."
    morgan "Not about what you think of me."
    morgan "Just what you saw."

    menu:
        "What do you tell Morgan?"

        "I'll tell the truth. All of it.":
            jump morgan_respond_truth

        "I'll tell them what I saw. Nothing more.":
            jump morgan_respond_neutral

        "I'll think about what's best for everyone.":
            jump morgan_respond_ambiguous


label morgan_respond_truth:

    $ truth += 10
    $ morgan_relationship += 5

    player "I'll tell the truth. All of it."

    show morgan quiet

    morgan "Okay."
    morgan "Okay. That's all I can ask."

    jump morgan_scene_end


label morgan_respond_neutral:

    $ mask += 5
    $ morgan_relationship += 10

    player "I'll tell them what I saw. Nothing more."

    show morgan relieved

    morgan "That's enough."
    morgan "That's more than enough."

    jump morgan_scene_end


label morgan_respond_ambiguous:

    $ ambition += 10

    player "I need to think about what's best for everyone."

    show morgan serious

    morgan "Don't take too long."
    morgan "Friday is in two days."

    jump morgan_scene_end


label morgan_scene_end:

    hide morgan with dissolve
    stop sound
    scene bg campus_day

    pause 1.0

    "Two days."
    "The summons sits in your email."
    "Your name. A time. A room number."

    pause 1.0

    jump act3_scene_jordan_side


## ==========================================
## SCENE 3.2 — JORDAN'S SIDE
## ==========================================

label act3_scene_jordan_side:

    scene bg campus_day

    if persistent.narrator_enabled:
        pass

# voice "audio/narration/[persistent.narrator_voice]/act3_jordan.mp3"

    "Jordan texts you that evening."

    scene bg phone_screen
    play sound "audio/sfx/phone_unlock.wav"

    nvl clear
    "JORDAN" "{size=14}7:41 PM{/size}"
    "JORDAN" "can we talk"
    "JORDAN" "{size=14}7:42 PM{/size}"
    "JORDAN" "not text. actually talk."
    nvl clear

    scene bg campus_day

    menu:
        "Do you meet Jordan?"

        "Yes — tonight.":
            jump jordan_meet_yes

        "Maybe tomorrow.":
            jump jordan_meet_delay

        "Not right now.":
            jump jordan_meet_no


label jordan_meet_no:

    $ jordan_relationship -= 15

    scene bg phone_screen

    nvl clear
    "YOU" "{size=14}7:50 PM{/size}"
    "YOU" "not right now"
    "JORDAN" "{size=14}7:51 PM{/size}"
    "JORDAN" "ok"
    nvl clear

    scene bg campus_day

    "That 'ok' carries a lot."
    "Jordan doesn't text again."

    jump act3_scene_casey_support


label jordan_meet_delay:

    $ jordan_relationship -= 5

    scene bg phone_screen

    nvl clear
    "YOU" "{size=14}7:50 PM{/size}"
    "YOU" "maybe tomorrow?"
    "JORDAN" "{size=14}7:52 PM{/size}"
    "JORDAN" "fine."
    nvl clear

    scene bg campus_day

    "Fine. From Jordan."
    "Not actually fine."

    jump act3_scene_casey_support


label jordan_meet_yes:

    $ jordan_relationship += 15

    scene bg rooftop_night
    play music "audio/music/ambient_city.wav" fadein 2.0

    show jordan serious at center

    "Jordan is on the quad bench."
    "Not the rooftop. Somewhere public."
    "Like [jordan_pronoun_subject] doesn't fully trust the situation."

    jordan "Thanks for coming."

    player "Of course."


    jordan "I need to know where you stand."

    player "On what?"

    jordan "Don't."

    pause 0.5

    show jordan quiet

    jordan "I did the right thing. I pushed Morgan to report it."
    jordan "Morgan didn't want to."
    jordan "You know what happened next."

    player "I walked away."

    jordan "Yeah."


    jordan "I'm not angry at you."
    jordan "I get it. It's messy. It's complicated."
    jordan "But Harkins is still there."
    jordan "Teaching. Grading. Still there."

    pause 1.5

    show jordan serious

    jordan "I need to know if you're going to tell them what you saw."
    jordan "Because if you don't..."
    jordan "Riley's testimony isn't enough. They already told [riley_pronoun_object] that."


    menu:
        "What do you tell Jordan?"

        "I'm going to tell the truth.":
            jump jordan_respond_yes

        "I'm still deciding.":
            jump jordan_respond_maybe

        "I can't make you a promise right now.":
            jump jordan_respond_honest


label jordan_respond_yes:

    $ truth += 15
    $ jordan_relationship += 20

    player "I'm going to tell the truth."

    show jordan quiet

    "Something in Jordan's shoulders releases."

    jordan "Okay."
    jordan "Thank you."

    jump jordan_scene_end


label jordan_respond_maybe:

    $ jordan_relationship -= 5

    player "I'm still deciding."

    show jordan frustrated

    jordan "There are people who got hurt by Harkins."
    jordan "Real hurt."
    jordan "This isn't abstract."

    jump jordan_scene_end


label jordan_respond_honest:

    $ truth += 5
    $ jordan_relationship += 5

    player "I can't make you a promise right now."

    show jordan neutral

    jordan "At least that's honest."
    jordan "Just... think about who you want to be when this is over."

    jump jordan_scene_end


label jordan_scene_end:

    hide jordan with dissolve
    stop music fadeout 2.0
    play music "audio/music/ambient_city.wav" fadein 2.0

    pause 1.0

    jump act3_scene_casey_support


## ==========================================
## SCENE 3.3 — CASEY'S SUPPORT
## ==========================================

label act3_scene_casey_support:

    scene bg room_night
    play music "audio/music/ambient_city.wav"

    if persistent.narrator_enabled:
        pass

# voice "audio/narration/[persistent.narrator_voice]/act3_casey.mp3"

    "The night before Friday."
    "You're in your room."
    "Staring at the ceiling more than your notes."

    pause 1.0

    play sound "audio/sfx/phone_buzz.wav"

    show screen notification_popup("Casey", "still up?")
    pause 1.5
    hide screen notification_popup

    menu:
        "Reply to Casey?"

        "Yeah. Can't sleep.":
            jump casey_support_yes

        "Leave it on read.":
            jump casey_support_ignore


label casey_support_ignore:

    $ casey_relationship -= 5
    $ mask += 5

    "You leave it."
    "The phone screen dims."
    "The ceiling has no answers either."

    jump act3_major_choice_approach


label casey_support_yes:

    $ casey_relationship += 10

    scene bg phone_screen

    nvl clear
    "YOU" "yeah. can't sleep."
    "CASEY" "same"
    "CASEY" "you ok?"
    nvl clear

    scene bg room_night

    show casey neutral at right

    "Casey calls instead of texting."
    "You answer."

    casey "Hey."

    player "Hey."

    casey "You don't have to tell me everything."
    casey "But if you want to talk, I'm here."

    pause 1.0

    if recall("casey_secret_shared") == True:
        ## Casey already knows - deeper conversation
        casey "I already know some of it."
        casey "I just want to know you're okay."

        player "I don't know if I am."

        casey "That's honest."
        casey "Whatever happens tomorrow — you're still you after it."
        casey "Don't forget that."

        $ casey_relationship += 10

    else:
        ## Casey doesn't know - general support
        casey "Whatever's going on..."
        casey "I'm not going anywhere."

        player "You don't know what's going on."

        casey "Doesn't matter."
        casey "I know you."

    pause 1.0

    hide casey with dissolve

    "The call ends."
    "You feel slightly less like you're about to drown."

    jump act3_major_choice_approach


## ==========================================
## SCENE 3.4 — THE ANCHOR (PRE-DECISION)
## ==========================================

label act3_major_choice_approach:

    scene bg rooftop_night
    play music "audio/music/ambient_city.wav" fadein 2.0

    if persistent.narrator_enabled:
        pass

# voice "audio/narration/[persistent.narrator_voice]/act3_anchor.mp3"

    "You go to the roof."
    "You don't know why. You just end up there."

    show anchor neutral at right

    "The Anchor is there."
    "Of course [anchor_pronoun_subject] is."

    anchor "Tomorrow."

    player "You know?"

    anchor "Word gets around."
    anchor "How are you sitting with it?"

    player "Not great."

    anchor "What are you afraid of?"


    menu:
        "What are you most afraid of?"

        "What it costs me to tell the truth.":
            jump anchor_fear_cost

        "What it says about me if I don't.":
            jump anchor_fear_self

        "Saying the wrong thing and making it worse.":
            jump anchor_fear_wrong


label anchor_fear_cost:

    $ ambition += 5

    player "What it costs me. If I testify — there are people who'll be angry."

    show anchor listening

    anchor "That's real."
    anchor "Some of those people will stay angry."
    anchor "That's also real."
    anchor "The question is: what does it cost you NOT to?"


    "You don't answer."
    "But you think about it."

    jump anchor_pre_choice_end


label anchor_fear_self:

    $ truth += 10

    player "What it says about me if I stay silent."

    show anchor serious

    anchor "That's the harder fear."
    anchor "Easier to live with external consequences."
    anchor "Harder to live with knowing what you didn't do."

    jump anchor_pre_choice_end


label anchor_fear_wrong:

    $ mask += 5

    player "Saying the wrong thing. Making it worse somehow."

    show anchor neutral

    anchor "The wrong thing is a very precise fear."
    anchor "Usually means you already know what the right thing is."


    "You don't say anything."
    "The Anchor lets the silence be."

    jump anchor_pre_choice_end


label anchor_pre_choice_end:

    show anchor neutral

    anchor "Whatever you decide tomorrow."
    anchor "Make sure it's yours."
    anchor "Not theirs. Not Jordan's. Not Morgan's."
    anchor "Yours."

    hide anchor with dissolve

    pause 1.0

    scene black with dissolve
    stop music fadeout 2.0
    pause 1.0

    centered "FRIDAY"
    pause 2.0

    jump act3_major_choice


## ==========================================
## THE MAJOR CHOICE — DEAN'S OFFICE
## ==========================================

label act3_major_choice:

    $ current_chapter = 4
    $ remember("act1_major_choice", "dean_office")

    scene bg dean_office
    play music "audio/music/tension_rising.wav" fadein 2.0

    if persistent.narrator_enabled:
        pass

# voice "audio/narration/[persistent.narrator_voice]/act3_choice.mp3"

    "Dean Okafor's office."
    "Sunlight through old blinds."
    "Two university investigators on one side of the table."
    "An empty chair for you on the other."


    "They introduce themselves."
    "You don't retain the names."


    "One of them places a recorder on the table."

    "Investigator" "We understand you were present in the university library on the evening of October 14th."


    "Investigator" "We're asking you to share what you witnessed that night."


    "Investigator" "You are not under suspicion. You are being asked as a potential witness to events relevant to our review."


    "The recorder blinks."
    "The room waits."


    ## This is the critical branch
    menu:
        "What do you do?"

        "Tell them everything — exactly what you witnessed.":
            jump major_choice_A_testify

        "Tell them you don't have anything relevant to share.":
            jump major_choice_B_silent

        "Ask about immunity or protection before speaking.":
            jump major_choice_C_deal

        "Ask if you can step out briefly — to talk to Morgan first.":
            jump major_choice_D_morgan_gambit


## ==========================================
## PATH A — TESTIFY
## ==========================================

label major_choice_A_testify:

    $ truth += 30
    $ mask -= 20
    $ ambition -= 5
    $ remember("act2_betrayal", "chose_truth")
    $ choices_made.append("Testified fully at dean's hearing")

    play music "audio/music/ambient_city.wav" fadein 1.0

    "You take a breath."
    "And you start talking."


    player "I was in the library on October 14th. Around 11 PM."
    player "I saw Jordan and Morgan in the east reading room."
    player "They were arguing. Morgan had something on their laptop — files, I think. Records."
    player "Jordan wanted to report it. Morgan didn't — not yet."
    player "I heard enough to understand it was about Professor Harkins."
    player "About grades. About payments."
    player "And then I left."


    "Investigator" "And why did you leave?"


    player "Because I was scared."
    player "And I didn't want to be involved."
    player "I was wrong not to come forward sooner."


    "The investigator writes something."
    "The recorder blinks."
    "That's it."

    $ insights_unlocked.append("Telling the truth out loud is different from knowing it privately")
    call screen insight_popup("Telling the truth out loud is different from knowing it privately")

    stop music fadeout 2.0
    jump act3_aftermath_shared


## ==========================================
## PATH B — STAY SILENT
## ==========================================

label major_choice_B_silent:

    $ mask += 30
    $ truth -= 25
    $ remember("act2_betrayal", "chose_silence")
    $ choices_made.append("Refused to testify at dean's hearing")

    "You look at the recorder."
    "The table."
    "Your hands."


    player "I don't think I have anything relevant to share."


    "The investigator's pen pauses."

    "Investigator" "You were in the library that evening?"

    player "I'm in the library most evenings."

    "Investigator" "Did you observe any interaction between students Jordan and Morgan?"


    player "I may have seen them. I didn't pay attention."


    "The investigator glances at their colleague."

    "Investigator" "Alright."
    "Investigator" "If you remember anything else, please reach out."


    "They hand you a card."
    "The session is over in four minutes."


    "You walk out into the hallway."
    "Riley is waiting on a bench."
    "One look at your face and [riley_pronoun_subject] knows."

    show riley serious at center

    riley "You didn't tell them."

    "You don't answer."

    riley "I'm going in alone then."

    "Riley stands. Walks past you. Doesn't look back."

    hide riley

    $ riley_relationship -= 30
    $ jordan_relationship -= 20

    $ insights_unlocked.append("Some silences cost other people more than yourself")
    call screen insight_popup("Some silences cost other people more than yourself")

    jump act3_aftermath_shared


## ==========================================
## PATH C — THE DEAL
## ==========================================

label major_choice_C_deal:

    $ ambition += 30
    $ mask += 10
    $ truth -= 10
    $ remember("act2_betrayal", "chose_deal")
    $ choices_made.append("Negotiated before testifying at dean's hearing")

    player "Before I say anything — I'd like to know what protections are in place for witnesses."


    "Investigator" "This is a university conduct review, not a legal proceeding."

    player "I understand. But if what I share has implications — academic or otherwise — I want to make sure my standing isn't affected."


    "The two investigators look at each other."

    "Investigator" "Any information you provide would be treated as protected witness testimony."
    "Investigator" "Your academic record would not be part of this review."

    player "And what about my name in any public findings?"

    "Investigator" "Witnesses are not named in the official report."


    "You've gotten what you came for."


    "You tell them what you saw."
    "Everything."
    "Clearly. Accurately."
    "But only after you protected yourself first."

    pause 1.0

    $ truth += 10

    $ insights_unlocked.append("Pragmatism and morality don't always cancel each other out")
    call screen insight_popup("Pragmatism and morality don't always cancel each other out")

    jump act3_aftermath_shared


## ==========================================
## PATH D — MORGAN GAMBIT
## ==========================================

label major_choice_D_morgan_gambit:

    $ truth += 5
    $ morgan_relationship += 5

    player "Could I have five minutes? There's someone I need to speak to first."


    "Investigator" "The session is scheduled for—"

    player "Five minutes. I'll be right back."


    "The investigator looks at the clock. Then nods."

    scene bg campus_day
    play music "audio/music/ambient_city.wav" fadein 1.0

    show morgan nervous at center

    "Morgan is in the hallway. Pacing."

    morgan "How'd it go?"

    player "I asked for five minutes."
    player "Morgan. Come in with me."

    show morgan serious

    morgan "What?"

    player "You found it. It should come from you."

    pause 1.5

    if morgan_relationship >= 60:
        ## High relationship — Morgan agrees
        jump morgan_gambit_success
    else:
        ## Low relationship — Morgan refuses
        jump morgan_gambit_fail


label morgan_gambit_success:

    show morgan quiet

    morgan "I..."
    morgan "Yeah."
    morgan "Okay."
    morgan "Yeah."

    $ morgan_relationship += 25
    $ truth += 20
    $ remember("act2_betrayal", "convinced_morgan")
    $ choices_made.append("Convinced Morgan to testify at dean's hearing")

    "Morgan walks in with you."

    hide morgan

    "You both give your statements."
    "Together."

    $ insights_unlocked.append("Sometimes the right move is helping someone else do the right thing")
    call screen insight_popup("Sometimes the right move is helping someone else do the right thing")

    jump act3_aftermath_shared


label morgan_gambit_fail:

    show morgan serious

    morgan "I can't."
    morgan "I'm sorry. I can't."

    hide morgan

    "Morgan walks away."

    "You stand in the hallway."
    "Five minutes almost up."
    "You go back in alone."


    "You tell them what you saw."
    "Morgan's decision is [morgan_pronoun_possessive] own."

    $ truth += 15
    $ remember("act2_betrayal", "tried_morgan_failed")
    $ choices_made.append("Tried to bring Morgan — testified alone")

    jump act3_aftermath_shared


## ==========================================
## SHARED AFTERMATH (ALL PATHS CONVERGE)
## ==========================================

label act3_aftermath_shared:

    scene bg campus_day
    play music "audio/music/ambient_city.wav" fadein 2.0

    if persistent.narrator_enabled:
        pass

# voice "audio/narration/[persistent.narrator_voice]/act3_aftermath.mp3"

    "You step out of the administration building."
    "Campus is loud."
    "Students between classes. Bikes. Pigeons."
    "None of them know what just happened in that room."


    "Your phone starts filling up."

    play sound "audio/sfx/phone_buzz.wav"
    pause 0.3
    play sound "audio/sfx/phone_buzz.wav"
    pause 0.3
    play sound "audio/sfx/phone_buzz.wav"

    "Word travels fast."


    "Whatever you said in there — or didn't say — it's done."

    pause 1.5

    scene black with dissolve
    stop music fadeout 2.0
    pause 1.0


    centered "CHAPTER 3 COMPLETE"
    pause 2.0


    $ current_chapter = 4
    $ renpy.save("act3_checkpoint")

    jump act4_opening


