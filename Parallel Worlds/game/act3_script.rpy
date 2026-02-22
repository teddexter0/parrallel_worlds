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
    play music "audio/music/ambient_city.mp3" fadein 2.0

    show screen game_hud

    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act3_open.mp3"

    "Three days have passed."
    "The university posted a notice. A 'formal review of academic conduct.'"
    "No names. Just the department. Just the dates."
    "But everyone on campus knows."

    pause 1.5

    "And then your student email pings."

    play sound "audio/sfx/phone_buzz.mp3"
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
    play music "audio/music/ambient_city.mp3"
    play sound "audio/sfx/cafe_ambience.mp3"

    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act3_morgan.mp3"

    "Morgan finds you before you find [morgan_pronoun_object]."
    "Back corner booth. Hands around a cup that's been empty for a while."

    show morgan nervous at left

    morgan "You got the summons."

    "It's not a question."

    player "Yeah."

    morgan "Me too."
    pause 1.0
    morgan "Jordan too."

    pause 0.5

    show morgan serious

    morgan "I need you to understand something."
    pause 0.5
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
    pause 0.5
    morgan "It's just... context."

    jump morgan_reveals_evidence


label morgan_reveal_firm:

    $ truth += 10
    $ morgan_relationship -= 10

    player "Whatever you're about to say won't change what I saw."

    show morgan frustrated

    morgan "I'm not asking you to lie."
    pause 0.5
    morgan "I'm asking you to understand why I did what I did."

    jump morgan_reveals_evidence


label morgan_reveals_evidence:

    show morgan serious

    morgan "I was the one who found the evidence."
    pause 0.5
    morgan "Harkins' grading files. The payment records. All of it."
    pause 0.5
    morgan "I found it by accident. I was doing research for [morgan_pronoun_possessive] seminar and..."

    "[morgan_pronoun_subject.capitalize()] trails off."

    morgan "It's a lot. More than I expected."

    "You already know what it is. Riley told you."
    "But you let Morgan say it."

    morgan "Twelve students. Three years."
    pause 0.5
    morgan "Some of them — some of them weren't paying with money."

    pause 1.5

    show morgan quiet

    morgan "I panicked."
    pause 0.5
    morgan "I thought — if I had something this big, maybe I could protect myself."
    pause 0.5
    morgan "Maybe I could make sure nothing like that ever happened to me."

    pause 1.5

    "Something shifts in your chest."

    $ insights_unlocked.append("Morgan was trying to protect themselves, not just cause harm")
    show screen insight_popup("Morgan was trying to protect themselves, not just cause harm")
    pause
    hide screen insight_popup

    player "You were scared."

    show morgan neutral

    morgan "Still am."

    pause 1.0

    morgan "Jordan wanted to go straight to the dean."
    pause 0.5
    morgan "And Jordan was right. I know that now."
    pause 0.5
    morgan "But I froze."

    pause 1.0

    morgan "I just need you to tell them the truth about what you saw."
    pause 0.5
    morgan "Not about what you think of me."
    pause 0.5
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
    pause 1.0
    morgan "Okay. That's all I can ask."

    jump morgan_scene_end


label morgan_respond_neutral:

    $ mask += 5
    $ morgan_relationship += 10

    player "I'll tell them what I saw. Nothing more."

    show morgan relieved

    morgan "That's enough."
    pause 0.5
    morgan "That's more than enough."

    jump morgan_scene_end


label morgan_respond_ambiguous:

    $ ambition += 10

    player "I need to think about what's best for everyone."

    show morgan serious

    morgan "Don't take too long."
    pause 0.5
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
        voice "audio/narration/[persistent.narrator_voice]/act3_jordan.mp3"

    "Jordan texts you that evening."

    scene bg phone_screen
    play sound "audio/sfx/phone_unlock.mp3"

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
    pause 1.5
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
    pause 1.5
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
    play music "audio/music/ambient_city.mp3" fadein 2.0

    show jordan serious at center

    "Jordan is on the quad bench."
    "Not the rooftop. Somewhere public."
    "Like [jordan_pronoun_subject] doesn't fully trust the situation."

    jordan "Thanks for coming."

    player "Of course."

    pause 0.5

    jordan "I need to know where you stand."

    player "On what?"

    jordan "Don't."

    pause 0.5

    show jordan quiet

    jordan "I did the right thing. I pushed Morgan to report it."
    pause 0.5
    jordan "Morgan didn't want to."
    pause 0.5
    jordan "You know what happened next."

    player "I walked away."

    jordan "Yeah."

    pause 1.0

    jordan "I'm not angry at you."
    pause 0.5
    jordan "I get it. It's messy. It's complicated."
    pause 1.0
    jordan "But Harkins is still there."
    pause 0.5
    jordan "Teaching. Grading. Still there."

    pause 1.5

    show jordan serious

    jordan "I need to know if you're going to tell them what you saw."
    pause 0.5
    jordan "Because if you don't..."
    pause 0.5
    jordan "Riley's testimony isn't enough. They already told [riley_pronoun_object] that."

    pause 1.0

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
    pause 0.5
    jordan "Thank you."

    jump jordan_scene_end


label jordan_respond_maybe:

    $ jordan_relationship -= 5

    player "I'm still deciding."

    show jordan frustrated

    jordan "There are people who got hurt by Harkins."
    pause 0.5
    jordan "Real hurt."
    pause 0.5
    jordan "This isn't abstract."

    jump jordan_scene_end


label jordan_respond_honest:

    $ truth += 5
    $ jordan_relationship += 5

    player "I can't make you a promise right now."

    show jordan neutral

    jordan "At least that's honest."
    pause 1.0
    jordan "Just... think about who you want to be when this is over."

    jump jordan_scene_end


label jordan_scene_end:

    hide jordan with dissolve
    stop music fadeout 2.0
    play music "audio/music/ambient_city.mp3" fadein 2.0

    pause 1.0

    jump act3_scene_casey_support


## ==========================================
## SCENE 3.3 — CASEY'S SUPPORT
## ==========================================

label act3_scene_casey_support:

    scene bg room_night
    play music "audio/music/ambient_city.mp3"

    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act3_casey.mp3"

    "The night before Friday."
    "You're in your room."
    "Staring at the ceiling more than your notes."

    pause 1.0

    play sound "audio/sfx/phone_buzz.mp3"

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
    pause 1.0
    "CASEY" "same"
    pause 0.5
    "CASEY" "you ok?"
    nvl clear

    scene bg room_night

    show casey neutral at right

    "Casey calls instead of texting."
    "You answer."

    casey "Hey."

    player "Hey."

    casey "You don't have to tell me everything."
    pause 0.5
    casey "But if you want to talk, I'm here."

    pause 1.0

    if recall("casey_secret_shared") == True:
        ## Casey already knows - deeper conversation
        casey "I already know some of it."
        pause 0.5
        casey "I just want to know you're okay."

        player "I don't know if I am."

        casey "That's honest."
        pause 0.5
        casey "Whatever happens tomorrow — you're still you after it."
        pause 0.5
        casey "Don't forget that."

        $ casey_relationship += 10

    else:
        ## Casey doesn't know - general support
        casey "Whatever's going on..."
        pause 0.5
        casey "I'm not going anywhere."

        player "You don't know what's going on."

        casey "Doesn't matter."
        pause 1.0
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
    play music "audio/music/ambient_city.mp3" fadein 2.0

    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act3_anchor.mp3"

    "You go to the roof."
    "You don't know why. You just end up there."

    show anchor neutral at right

    "The Anchor is there."
    "Of course [anchor_pronoun_subject] is."

    anchor "Tomorrow."

    player "You know?"

    anchor "Word gets around."
    pause 1.0
    anchor "How are you sitting with it?"

    player "Not great."

    anchor "What are you afraid of?"

    pause 1.5

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
    pause 0.5
    anchor "Some of those people will stay angry."
    pause 0.5
    anchor "That's also real."
    pause 1.0
    anchor "The question is: what does it cost you NOT to?"

    pause 1.0

    "You don't answer."
    "But you think about it."

    jump anchor_pre_choice_end


label anchor_fear_self:

    $ truth += 10

    player "What it says about me if I stay silent."

    show anchor serious

    anchor "That's the harder fear."
    pause 0.5
    anchor "Easier to live with external consequences."
    pause 0.5
    anchor "Harder to live with knowing what you didn't do."

    jump anchor_pre_choice_end


label anchor_fear_wrong:

    $ mask += 5

    player "Saying the wrong thing. Making it worse somehow."

    show anchor neutral

    anchor "The wrong thing is a very precise fear."
    pause 0.5
    anchor "Usually means you already know what the right thing is."

    pause 1.0

    "You don't say anything."
    "The Anchor lets the silence be."

    jump anchor_pre_choice_end


label anchor_pre_choice_end:

    show anchor neutral

    anchor "Whatever you decide tomorrow."
    pause 0.5
    anchor "Make sure it's yours."
    pause 0.5
    anchor "Not theirs. Not Jordan's. Not Morgan's."
    pause 1.0
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
    play music "audio/music/tension_rising.mp3" fadein 2.0

    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act3_choice.mp3"

    "Dean Okafor's office."
    "Sunlight through old blinds."
    "Two university investigators on one side of the table."
    "An empty chair for you on the other."

    pause 1.0

    "They introduce themselves."
    "You don't retain the names."

    pause 0.5

    "One of them places a recorder on the table."

    "Investigator" "We understand you were present in the university library on the evening of October 14th."

    pause 0.5

    "Investigator" "We're asking you to share what you witnessed that night."

    pause 1.0

    "Investigator" "You are not under suspicion. You are being asked as a potential witness to events relevant to our review."

    pause 1.0

    "The recorder blinks."
    "The room waits."

    pause 1.5

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

    play music "audio/music/ambient_city.mp3" fadein 1.0

    "You take a breath."
    "And you start talking."

    pause 1.0

    player "I was in the library on October 14th. Around 11 PM."
    pause 0.5
    player "I saw Jordan and Morgan in the east reading room."
    pause 0.5
    player "They were arguing. Morgan had something on their laptop — files, I think. Records."
    pause 0.5
    player "Jordan wanted to report it. Morgan didn't — not yet."
    pause 0.5
    player "I heard enough to understand it was about Professor Harkins."
    pause 0.5
    player "About grades. About payments."
    pause 0.5
    player "And then I left."

    pause 1.5

    "Investigator" "And why did you leave?"

    pause 1.0

    player "Because I was scared."
    pause 0.5
    player "And I didn't want to be involved."
    pause 0.5
    player "I was wrong not to come forward sooner."

    pause 1.5

    "The investigator writes something."
    "The recorder blinks."
    "That's it."

    $ insights_unlocked.append("Telling the truth out loud is different from knowing it privately")
    show screen insight_popup("Telling the truth out loud is different from knowing it privately")
    pause
    hide screen insight_popup

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

    pause 1.0

    player "I don't think I have anything relevant to share."

    pause 1.0

    "The investigator's pen pauses."

    "Investigator" "You were in the library that evening?"

    player "I'm in the library most evenings."

    "Investigator" "Did you observe any interaction between students Jordan and Morgan?"

    pause 1.0

    player "I may have seen them. I didn't pay attention."

    pause 1.0

    "The investigator glances at their colleague."

    "Investigator" "Alright."
    pause 0.5
    "Investigator" "If you remember anything else, please reach out."

    pause 1.5

    "They hand you a card."
    "The session is over in four minutes."

    pause 1.0

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
    show screen insight_popup("Some silences cost other people more than yourself")
    pause
    hide screen insight_popup

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

    pause 0.5

    "Investigator" "This is a university conduct review, not a legal proceeding."

    player "I understand. But if what I share has implications — academic or otherwise — I want to make sure my standing isn't affected."

    pause 1.0

    "The two investigators look at each other."

    "Investigator" "Any information you provide would be treated as protected witness testimony."
    pause 0.5
    "Investigator" "Your academic record would not be part of this review."

    player "And what about my name in any public findings?"

    "Investigator" "Witnesses are not named in the official report."

    pause 1.0

    "You've gotten what you came for."

    pause 1.0

    "You tell them what you saw."
    "Everything."
    "Clearly. Accurately."
    "But only after you protected yourself first."

    pause 1.0

    $ truth += 10

    $ insights_unlocked.append("Pragmatism and morality don't always cancel each other out")
    show screen insight_popup("Pragmatism and morality don't always cancel each other out")
    pause
    hide screen insight_popup

    jump act3_aftermath_shared


## ==========================================
## PATH D — MORGAN GAMBIT
## ==========================================

label major_choice_D_morgan_gambit:

    $ truth += 5
    $ morgan_relationship += 5

    player "Could I have five minutes? There's someone I need to speak to first."

    pause 0.5

    "Investigator" "The session is scheduled for—"

    player "Five minutes. I'll be right back."

    pause 0.5

    "The investigator looks at the clock. Then nods."

    scene bg campus_day
    play music "audio/music/ambient_city.mp3" fadein 1.0

    show morgan nervous at center

    "Morgan is in the hallway. Pacing."

    morgan "How'd it go?"

    player "I asked for five minutes."
    pause 0.5
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
    pause 1.0
    morgan "Yeah."
    pause 0.5
    morgan "Okay."
    pause 0.5
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
    show screen insight_popup("Sometimes the right move is helping someone else do the right thing")
    pause
    hide screen insight_popup

    jump act3_aftermath_shared


label morgan_gambit_fail:

    show morgan serious

    morgan "I can't."
    pause 0.5
    morgan "I'm sorry. I can't."

    hide morgan

    "Morgan walks away."

    "You stand in the hallway."
    "Five minutes almost up."
    "You go back in alone."

    pause 1.0

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
    play music "audio/music/ambient_city.mp3" fadein 2.0

    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act3_aftermath.mp3"

    "You step out of the administration building."
    "Campus is loud."
    "Students between classes. Bikes. Pigeons."
    "None of them know what just happened in that room."

    pause 1.5

    "Your phone starts filling up."

    play sound "audio/sfx/phone_buzz.mp3"
    pause 0.3
    play sound "audio/sfx/phone_buzz.mp3"
    pause 0.3
    play sound "audio/sfx/phone_buzz.mp3"

    "Word travels fast."

    pause 1.0

    "Whatever you said in there — or didn't say — it's done."

    pause 1.5

    scene black with dissolve
    stop music fadeout 2.0
    pause 1.0

    show screen records_sidebar

    centered "CHAPTER 3 COMPLETE"
    pause 1.0
    centered "Your decision has been made."
    pause 2.0

    hide screen records_sidebar

    $ current_chapter = 4
    $ renpy.save("act3_checkpoint")

    jump act4_opening
