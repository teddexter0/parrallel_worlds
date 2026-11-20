## FILE: game/script.rpy
## Main story script - Fixed and polished version

## ==========================================
## GAME START
## ==========================================

label start:

    ## Local-first profile. No account, email, payment, or server is required.
    if not persistent.player_name:
        call player_setup from _call_player_setup

    $ parent_name = persistent.parent_name
    $ parent_pronoun_subject = persistent.parent_pronoun_subject
    $ parent_pronoun_object = persistent.parent_pronoun_object
    $ parent_pronoun_possessive = persistent.parent_pronoun_possessive
    
    ## Gender assignment
    call assign_character_genders from _call_assign_character_genders
    
    ## Show the content notice once per browser/device.
    if not persistent.seen_content_notice:
        call show_disclaimer from _call_show_disclaimer
    
    ## Start game
    jump act1_opening

## ==========================================
## INITIAL SETUP
## ==========================================

label show_disclaimer:
    scene black

    "Content note: This story includes coercion, harassment, threats, and institutional abuse. You can save or step away from the Pause menu."

    $ persistent.seen_content_notice = True
    $ renpy.save_persistent()

    return

label player_setup:
    scene bg room_night

    $ player_name = renpy.input("What should the story call you?", default="Alex", length=24, exclude="{}[]")
    $ setup_name = player_name.strip() or "Alex"

    menu:
        "How should the story frame your character?"

        "Man":
            $ persistent.player_gender = "male"

        "Woman":
            $ persistent.player_gender = "female"

        "Non-binary":
            $ persistent.player_gender = "nonbinary"

    menu:
        "Who raised you primarily?"

        "My mother":
            $ persistent.parent_name = "Mom"
            $ persistent.parent_pronoun_subject = "she"
            $ persistent.parent_pronoun_object = "her"
            $ persistent.parent_pronoun_possessive = "her"

        "My father":
            $ persistent.parent_name = "Dad"
            $ persistent.parent_pronoun_subject = "he"
            $ persistent.parent_pronoun_object = "him"
            $ persistent.parent_pronoun_possessive = "his"

        "My guardian":
            $ persistent.parent_name = "Guardian"
            $ persistent.parent_pronoun_subject = "they"
            $ persistent.parent_pronoun_object = "them"
            $ persistent.parent_pronoun_possessive = "their"

    $ persistent.player_name = setup_name
    $ parent_name = persistent.parent_name
    $ parent_pronoun_subject = persistent.parent_pronoun_subject
    $ parent_pronoun_object = persistent.parent_pronoun_object
    $ parent_pronoun_possessive = persistent.parent_pronoun_possessive
    $ renpy.save_persistent()

    return

## ==========================================
## ACT 1: THE MESSAGE
## ==========================================

label act1_opening:
    
    $ current_chapter = 1
    $ current_act = 1
    
    scene bg room_night
    play music "audio/music/ambient_city.wav" fadein 2.0
    
    show screen game_hud
    
    "11:47 p.m. Your project is due at midnight. You reread the same line until your phone buzzes against the desk."
    play sound "audio/sfx/phone_buzz.wav"
    "[parent_name]: We need to talk."
    play sound "audio/sfx/phone_buzz.wav"
    "Casey: I heard something..."
    play sound "audio/sfx/phone_buzz.wav"
    "Unknown number: I know what you did."
    
    menu:
        "Which message do you check first?"
        
        "Open the text from [parent_name]":
            jump check_authority_first
        
        "Open Casey's text":
            jump check_casey_first
        
        "Open the text from the unknown number":
            jump check_unknown_first
        
        "Silence the phone and finish the project":
            jump ignore_all_messages

## CHOICE BRANCH 1A: Check Authority First
label check_authority_first:
    
    $ mask += 10
    $ ambition += 5
    $ remember("first_message_checked", "authority")
    $ choices_made.append("Checked parent message first")
    
    scene bg phone_screen
    play sound "audio/sfx/phone_unlock.wav"
    
    pause 0.5
    
    "You open the message from [parent_name]."
    
    pause 0.5
    
    ## Phone message display
    nvl clear
    "[parent_name.upper()]" "{size=14}11:45 PM{/size}"
    "[parent_name.upper()]" "We need to talk. Tomorrow morning. Don't be late."
    nvl clear
    
    if persistent.narrator_enabled:
        pass
        # voice "audio/narration/[persistent.narrator_voice]/act1_parent_message.mp3"
    
    "Your stomach tightens."
    "That tone. Never good."
    
    $ insights_unlocked.append("Authority figures make you anxious")
    call screen insight_popup("Authority figures make you anxious")
    
    scene bg room_night
    
    "You stare at the screen for a moment."
    "Two unread messages remain."
    
    jump post_first_message_check

## CHOICE BRANCH 1B: Check Casey First
label check_casey_first:
    
    $ truth += 5
    $ casey_relationship += 5
    $ remember("first_message_checked", "casey")
    $ choices_made.append("Checked Casey message first")
    
    scene bg phone_screen
    play sound "audio/sfx/phone_unlock.wav"
    
    pause 0.5
    
    "You open Casey's message."
    
    pause 0.5
    
    nvl clear
    "CASEY" "{size=14}11:43 PM{/size}"
    "CASEY" "hey"
    "CASEY" "{size=14}11:44 PM{/size}"
    "CASEY" "i heard something about you"
    "CASEY" "{size=14}11:45 PM{/size}"
    "CASEY" "is it true?"
    nvl clear
    
    if persistent.narrator_enabled:
        pass
        # voice "audio/narration/[persistent.narrator_voice]/act1_casey_message.mp3"
    
    "Your heart races."
    "What did [casey_pronoun_subject] hear?"
    "Who told [casey_pronoun_object]?"
    
    $ insights_unlocked.append("Casey knows something")
    call screen insight_popup("Casey knows something")
    
    scene bg room_night
    
    "Your hands hover over the keyboard."
    "Two other messages are still waiting."
    
    jump post_first_message_check

## CHOICE BRANCH 1C: Check Unknown First
label check_unknown_first:
    
    $ truth += 10
    $ ambition -= 5
    $ remember("first_message_checked", "unknown")
    $ choices_made.append("Checked unknown message first")
    
    scene bg phone_screen
    play sound "audio/sfx/phone_unlock.wav"
    play music "audio/music/tension_rising.wav" fadein 1.0
    
    pause 0.5
    
    "You open the message from the unknown number."
    
    pause 1.0
    
    nvl clear
    "UNKNOWN" "{size=14}11:46 PM{/size}"
    "UNKNOWN" "I know what you did."
    pause 1.0
    "UNKNOWN" "{size=14}11:47 PM{/size}"
    "UNKNOWN" "You have 24 hours."
    nvl clear
    
    if persistent.narrator_enabled:
        pass
        # voice "audio/narration/[persistent.narrator_voice]/act1_unknown_message.mp3"
    
    pause 1.0
    
    "The words blur."
    "Your hands shake."
    
    pause 1.0
    
    "What do they know?"
    "How did they find out?"
    
    $ insights_unlocked.append("You're hiding something")
    call screen insight_popup("You're hiding something")
    
    scene bg room_night
    stop music fadeout 2.0
    play music "audio/music/ambient_city.wav" fadein 2.0
    
    "You set the phone down."
    "Your chest feels tight."
    
    jump post_first_message_check

## CHOICE BRANCH 1D: Ignore All
label ignore_all_messages:
    
    $ ambition += 15
    $ mask += 5
    $ jordan_relationship -= 10
    $ casey_relationship -= 10
    $ remember("first_message_checked", "none")
    $ choices_made.append("Ignored all messages")
    
    scene bg room_night
    
    if persistent.narrator_enabled:
        pass
        # voice "audio/narration/[persistent.narrator_voice]/act1_ignore.mp3"
    
    "You silence your phone and turn back to your work."
    
    pause 1.0
    
    "Problems can wait."
    "This deadline can't."
    
    $ insights_unlocked.append("You prioritize work over people")
    call screen insight_popup("You prioritize work over people")
    
    play sound "audio/sfx/phone_buzz.wav"
    pause 0.3
    play sound "audio/sfx/phone_buzz.wav"
    pause 0.3
    play sound "audio/sfx/phone_buzz.wav"
    
    "Your phone keeps buzzing."
    "But you don't look."
    
    pause 1.0
    
    "An hour passes."
    
    jump post_first_message_check

## ==========================================
## POST FIRST CHOICE - CONVERGENCE
## ==========================================

label post_first_message_check:
    
    scene bg room_night
    
    if persistent.narrator_enabled:
        pass
        # voice "audio/narration/[persistent.narrator_voice]/act1_scene02.mp3"
    
    if recall("first_message_checked") != "none":
        "The other messages are still glowing on your screen."
        "Waiting."
    else:
        "Your phone finally goes quiet."
        "But when you check it..."
        "All three messages are still there."
    
    pause 1.0
    
    "You know they won't just disappear."
    
    pause 1.0
    
    ## Transition to morning
    scene black with dissolve
    pause 1.0
    
    if persistent.narrator_enabled:
        pass
        # voice "audio/narration/[persistent.narrator_voice]/act1_morning.mp3"
    
    "Morning comes too quickly."
    
    pause 1.0
    
    ## NEXT MAJOR SCENE
    jump act1_morning_confrontation

## ==========================================
## SECOND MAJOR CHOICE: Morning Confrontation
## ==========================================

label act1_morning_confrontation:
    
    scene bg kitchen_morning
    play music "audio/music/ambient_city.wav" fadein 2.0
    
    if persistent.narrator_enabled:
        pass
        # voice "audio/narration/[persistent.narrator_voice]/act1_confrontation.mp3"
    
    "[parent_name] is already at the table when you come down."
    "Coffee. Newspaper. The usual morning routine."
    "But [parent_pronoun_possessive] face is different today."
    
    pause 1.0
    
    parent "Sit down."
    
    "It's not a request."
    
    menu:
        "How do you respond?"
        
        "Sit down without saying anything":
            jump confrontation_comply
        
        "Ask what this is about":
            jump confrontation_question
        
        "Make an excuse to leave":
            jump confrontation_avoid

label confrontation_comply:
    
    $ mask += 15
    $ truth -= 5
    $ remember("parent_confrontation_outcome", "complied")
    
    "You sit."
    "Say nothing."
    "Wait for [parent_pronoun_object] to speak first."
    
    parent "I got a call yesterday."
    pause 0.5
    parent "From the university."
    
    "Your stomach drops."
    
    jump confrontation_reveal

label confrontation_question:
    
    $ truth += 10
    $ mask -= 5
    $ remember("parent_confrontation_outcome", "questioned")
    
    player "What's this about?"
    
    parent "Don't play games with me."
    pause 0.5
    parent "You know exactly what this is about."
    
    "But you don't."
    "Or do you?"
    
    jump confrontation_reveal

label confrontation_avoid:
    
    $ ambition += 10
    $ mask -= 10
    $ remember("parent_confrontation_outcome", "avoided")
    
    player "I actually have to..."
    
    parent "Sit. Down."
    
    "The tone leaves no room for argument."
    
    "You sit."
    
    jump confrontation_reveal

label confrontation_reveal:
    parent "Someone reached out to the university."
    pause 0.5
    parent "Made some... allegations."
    
    if persistent.narrator_enabled:
        pass
        # voice "audio/narration/[persistent.narrator_voice]/act1_allegations.mp3"
    
    "The room feels smaller."
    
    parent "They claim you witnessed something."
    pause 0.5
    parent "Something serious."
    pause 0.5
    parent "And that you never reported it."
    
    pause 1.0
    
    "Your mind races."
    "What did you see?"
    "When?"
    
    pause 1.0
    
    ## Memory callback
    $ remember("secret_type", "witness")
    $ active_threads.append("What Did You Witness?")
    
    menu:
        "What do you say?"
        
        "Deny everything":
            jump confrontation_deny
        
        "Ask what they're talking about specifically":
            jump confrontation_clarify
        
        "Admit you saw something but say it's complicated":
            jump confrontation_partial_admit

label confrontation_deny:
    
    $ truth -= 15
    $ mask += 10
    $ memory_bank["first_lie_told"] = "denied_witnessing"
    
    player "I don't know what you're talking about."
    
    parent "Really."
    pause 0.5
    parent "Because whoever made this claim seems pretty certain."
    
    "[parent_pronoun_possessive] eyes bore into you."
    
    parent "And they have proof."
    
    $ insights_unlocked.append("Lying to authority makes things worse")
    call screen insight_popup("Lying to authority makes things worse")
    
    jump confrontation_aftermath

label confrontation_clarify:
    
    $ truth += 5
    $ ambition += 5
    
    player "What exactly are they saying I saw?"
    
    parent "They didn't specify."
    pause 0.5
    parent "Just that it happened on campus."
    pause 0.5
    parent "Two months ago."
    
    "Two months ago."
    
    if persistent.narrator_enabled:
        pass
        # voice "audio/narration/[persistent.narrator_voice]/act1_memory_trigger.mp3"
    
    "Something flashes in your memory."
    "Late night. Library. Voices."
    
    $ remember("memory_trigger", "library_two_months_ago")
    
    jump confrontation_aftermath

label confrontation_partial_admit:
    
    $ truth += 10
    $ mask -= 10
    
    player "I... might have seen something."
    pause 0.5
    player "But it's not what you think."
    
    parent "Then tell me what it is."
    
    pause 1.0
    
    menu:
        "Do you tell them now?"
        
        "Tell them the truth":
            jump early_truth_reveal
        
        "Say you need time to think":
            jump postpone_truth

label early_truth_reveal:
    
    $ truth += 20
    $ mask -= 15
    $ remember("truth_reveal_timing", "early")
    
    player "I saw two students..."
    pause 0.5
    player "In the library. Late."
    pause 0.5
    player "They were... arguing. About something."
    
    parent "And?"
    
    player "One of them had... evidence. Of something."
    pause 0.5
    player "Against a professor."
    
    $ insights_unlocked.append("Academic corruption is involved")
    call screen insight_popup("Academic corruption is involved")
    
    jump confrontation_aftermath

label postpone_truth:
    
    $ truth -= 5
    $ ambition += 5
    $ remember("truth_reveal_timing", "postponed")
    
    player "I need to think about this."
    pause 0.5
    player "Make sure I remember it correctly."
    
    parent "You have until tonight."
    pause 0.5
    parent "After that, I'm calling the dean myself."
    
    jump confrontation_aftermath

label confrontation_aftermath:
    parent "This is serious, [persistent.player_name]."
    pause 0.5
    parent "Whatever you saw, whatever you know..."
    pause 0.5
    parent "It's going to come out."
    
    pause 1.0
    
    if persistent.narrator_enabled:
        pass
        # voice "audio/narration/[persistent.narrator_voice]/act1_aftermath.mp3"
    
    "[parent_pronoun_subject.capitalize()] leaves you alone at the table."
    
    pause 1.0
    
    "Your phone buzzes."
    play sound "audio/sfx/phone_buzz.wav"
    
    "Another message."
    
    jump act1_cliffhanger

## ==========================================
## CLIFFHANGER ENDING (Spider-Man NWH style)
## ==========================================

label act1_cliffhanger:
    
    scene bg room_night
    play music "audio/music/tension_rising.wav" fadein 2.0
    
    "Back in your room, you finally check your phone."
    
    pause 1.0
    
    "A new message."
    "From the unknown number."
    
    pause 1.0
    
    scene bg phone_screen
    
    nvl clear
    "UNKNOWN" "{size=14}3:42 PM{/size}"
    "UNKNOWN" "Check your email."
    nvl clear
    
    pause 2.0
    
    scene bg room_night
    
    "Your laptop is still open."
    "One unread email."
    
    pause 1.0
    
    "You click it."
    
    pause 2.0
    
    scene black
    
    "Subject: The Truth About You"
    
    pause 2.0
    
    "Attached: One video file."
    
    pause 2.0
    
    "Your hand hovers over the trackpad."
    
    pause 1.5
    
    "You click play."
    
    pause 3.0
    
    ## Screen flashes white
    scene white
    pause 0.3
    scene black
    
    ## Distorted audio effect (if you add audio later)
    play sound "audio/sfx/chair_scrape.wav"
    
    "..."
    
    pause 2.0
    
    "No."
    
    pause 1.0
    
    "No no no no no."
    
    pause 2.0
    
    "They weren't supposed to have this."
    
    pause 2.0
    
    "How did they..."
    
    pause 1.5
    
    ## Phone rings
    play sound "audio/sfx/phone_buzz.wav"
    
    "Your phone rings."
    
    pause 1.0
    
    "Unknown number."
    
    pause 2.0
    
    ## Cut to black with text
    scene black
    
    centered "{size=36}Everything changes now.{/size}"
    
    pause 3.0
    
    jump end_of_chapter_1

## ==========================================
## END OF CHAPTER 1
## ==========================================

label end_of_chapter_1:
    
    scene black with dissolve
    
    pause 1.0
    
    centered "{size=48}CHAPTER 1 COMPLETE{/size}"
    pause 1.5
    centered "Your choices have been recorded. The story continues now."
    pause 1.5

    $ current_chapter = 2
    $ renpy.save("act1_checkpoint")

    menu:
        "What would you like to do?"

        "Continue to Chapter 2":
            jump act2_opening

        "View Records":
            show screen records_sidebar
            "Press ESC when done viewing."
            pause
            hide screen records_sidebar
            jump end_of_chapter_1

        "Save & Exit":
            $ MainMenu()()

## Season 2 Teaser (Post-credits)
label season2_teaser:
    
    scene black
    
    pause 3.0
    
    centered "ONE YEAR LATER..."
    
    pause 2.0
    
    scene bg unknown_location
    play music "audio/music/tension_rising.wav"
    
    "???" "You thought it was over?"
    
    pause 1.0
    
    "???" "It's only just beginning."
    
    pause 1.0
    
    scene black with dissolve
    stop music fadeout 2.0
    
    centered "{size=48}PARALLEL WORLDS{/size}"
    pause 1.0
    centered "{size=32}SEASON 2{/size}"
    pause 1.0
    centered "COMING SOON"
    
    pause 2.0
    
    $ persistent.seen_teaser = True
    $ renpy.save_persistent()

    centered "Season 1 is complete. Your save remains on this device."
    pause 2.0

    $ MainMenu()()
    
    return

