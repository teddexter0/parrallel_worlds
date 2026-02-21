## FILE: game/script.rpy
## Main story script - Complete Act 1 + Framework

## ==========================================
## GAME START
## ==========================================

label start:
    
    ## Check if player has account
    if not persistent.player_email:
        call account_creation
    
    ## Check narrator preference
    if persistent.narrator_enabled is None:
        call narrator_setup
    
    ## Check chapter unlock status
    call check_chapter_unlock
    
    ## Gender assignment
    call assign_character_genders
    
    ## Show disclaimer
    call show_disclaimer
    
    ## Start game
    jump act1_opening

## ==========================================
## INITIAL SETUP
## ==========================================

label show_disclaimer:
    
    scene black
    
    centered "PARALLEL WORLDS"
    pause 1.0
    centered "This is a story about choices and consequences."
    pause 1.0
    centered "Your decisions matter. There's no going back."
    pause 1.5
    centered "Recommended: 30 minutes per day over one week."
    pause 2.0
    
    return

label account_creation:
    
    scene bg room_night
    
    centered "Welcome to Parallel Worlds."
    pause 1.0
    centered "Before we begin, let's set up your account."
    
    $ player_email = renpy.input("Enter your email:", default="your@email.com")
    $ persistent.player_email = player_email.strip()
    
    $ player_name = renpy.input("What's your name?", default="Alex")
    $ persistent.player_name = player_name.strip()
    
    menu:
        "Select your gender:"
        
        "Male":
            $ persistent.player_gender = "male"
        
        "Female":
            $ persistent.player_gender = "female"
    
    menu:
        "Who raised you primarily?"

        "My mother":
            $ parent_name = "Mom"
            $ parent_pronoun_subject = "she"
            $ parent_pronoun_object = "her"
            $ parent_pronoun_possessive = "her"

        "My father":
            $ parent_name = "Dad"
            $ parent_pronoun_subject = "he"
            $ parent_pronoun_object = "him"
            $ parent_pronoun_possessive = "his"

        "My guardian":
            $ parent_name = "Guardian"
            $ parent_pronoun_subject = "they"
            $ parent_pronoun_object = "them"
            $ parent_pronoun_possessive = "their"

    ## Generate referral code
    $ persistent.referral_code = generate_referral_code(persistent.player_email)
    
    centered "Your account is ready, [persistent.player_name]."
    pause 1.0
    centered "Your referral code is: [persistent.referral_code]"
    pause 1.0
    centered "Share it with friends to unlock chapters!"
    pause 2.0
    
    return

label narrator_setup:
    
    scene black
    
    centered "This game features optional narration."
    pause 1.0
    
    menu:
        "Would you like it enabled?"
        
        "Yes - Male narrator (London accent)":
            $ persistent.narrator_enabled = True
            $ persistent.narrator_voice = "male"
        
        "Yes - Female narrator (California accent)":
            $ persistent.narrator_enabled = True
            $ persistent.narrator_voice = "female"
        
        "No narration (text only)":
            $ persistent.narrator_enabled = False
    
    return

label check_chapter_unlock:
    
    python:
        import datetime
        today = datetime.date.today()
        days_diff = 0

        if persistent.last_played_date:
            last_date = datetime.datetime.strptime(persistent.last_played_date, "%Y-%m-%d").date()
            days_diff = (today - last_date).days

            if days_diff == 1:
                ## Played yesterday - continue streak
                persistent.play_streak += 1
                renpy.show_screen("streak_notification", days=persistent.play_streak)
                renpy.pause(3.5)
                renpy.hide_screen("streak_notification")
            elif days_diff > 1:
                ## Broke streak
                persistent.play_streak = 1
        else:
            ## First time playing
            persistent.play_streak = 1

        ## Update last played date
        persistent.last_played_date = today.strftime("%Y-%m-%d")

        ## Unlock next chapter if it's a new day
        if persistent.chapters_unlocked < current_chapter and not persistent.paid_unlock:
            if days_diff >= 1:
                persistent.chapters_unlocked = current_chapter

    ## Check if current chapter is locked
    if current_chapter > persistent.chapters_unlocked and not persistent.paid_unlock:
        call screen chapter_locked
        
        if _return == "pay":
            ## TODO: Integrate Pesapal payment
            "Redirecting to payment..."
            ## After successful payment:
            ## $ persistent.paid_unlock = True
            ## $ persistent.chapters_unlocked = 7  # Unlock all
        
        elif _return == "wait":
            centered "Come back tomorrow to continue your journey."
            $ MainMenu(confirm=False)()
    
    return

## ==========================================
## ACT 1: THE MESSAGE
## ==========================================

label act1_opening:
    
    $ current_chapter = 1
    $ current_act = 1
    
    scene bg room_night
    play music "audio/music/ambient_city.mp3" fadein 2.0
    
    show screen game_hud
    
    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act1_scene01.mp3"
    
    "It's 11:47 PM."
    "Your room is dimly lit by the glow of your laptop screen."
    "You've been working on the same project for hours, but your mind keeps drifting."
    
    pause 1.0
    
    "Your phone vibrates."
    play sound "audio/sfx/phone_buzz.mp3"
    pause 0.5
    
    "Once."
    play sound "audio/sfx/phone_buzz.mp3"
    pause 0.5
    
    "Twice."
    play sound "audio/sfx/phone_buzz.mp3"
    pause 0.5
    
    "Three times."
    
    show screen notification_popup("Unknown", "I know what you did...")
    pause 2.0
    hide screen notification_popup
    
    show screen notification_popup("Casey", "Hey... I heard something...")
    pause 2.0
    hide screen notification_popup
    
    show screen notification_popup("Parent", "We need to talk.")
    pause 2.0
    hide screen notification_popup
    
    "Three messages. All at once. From three different people."
    
    pause 1.0
    
    menu:
        "Which message do you check first?"
        
        "Check the message from your parent":
            jump check_authority_first
        
        "Check the message from Casey":
            jump check_casey_first
        
        "Check the message from Unknown Number":
            jump check_unknown_first
        
        "Ignore them all and keep working":
            jump ignore_all_messages

## CHOICE BRANCH 1A: Check Authority First
label check_authority_first:
    
    $ mask += 10
    $ ambition += 5
    $ remember("first_message_checked", "authority")
    $ choices_made.append("Checked parent message first")
    
    scene bg phone_screen
    play sound "audio/sfx/phone_unlock.mp3"
    
    pause 0.5
    
    "You open the message from your parent."
    
    pause 0.5
    
    ## Phone message display
    nvl clear
    "PARENT" "{size=14}11:45 PM{/size}"
    "PARENT" "We need to talk. Tomorrow morning. Don't be late."
    nvl clear
    
    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act1_parent_message.mp3"
    
    "Your stomach tightens."
    "That tone. Never good."
    
    $ insights_unlocked.append("Authority figures make you anxious")
    show screen insight_popup("Authority figures make you anxious")
    pause
    hide screen insight_popup
    
    scene bg room_night
    
    "You stare at the screen for a moment."
    "The other two messages are still there. Waiting."
    
    jump post_first_message_check

## CHOICE BRANCH 1B: Check Casey First
label check_casey_first:
    
    $ truth += 5
    $ casey_relationship += 5
    $ remember("first_message_checked", "casey")
    $ choices_made.append("Checked Casey message first")
    
    scene bg phone_screen
    play sound "audio/sfx/phone_unlock.mp3"
    
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
        voice "audio/narration/[persistent.narrator_voice]/act1_casey_message.mp3"
    
    "Your heart races."
    "What did [casey_pronoun_subject] hear?"
    "Who told [casey_pronoun_object]?"
    
    $ insights_unlocked.append("Casey knows something")
    show screen insight_popup("Casey knows something")
    pause
    hide screen insight_popup
    
    scene bg room_night
    
    "Your hands hover over the keyboard."
    "Do you reply now? Or check the other messages first?"
    
    jump post_first_message_check

## CHOICE BRANCH 1C: Check Unknown First
label check_unknown_first:
    
    $ truth += 10
    $ ambition -= 5
    $ remember("first_message_checked", "unknown")
    $ choices_made.append("Checked unknown message first")
    
    scene bg phone_screen
    play sound "audio/sfx/phone_unlock.mp3"
    play music "audio/music/tension_rising.mp3" fadein 1.0
    
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
        voice "audio/narration/[persistent.narrator_voice]/act1_unknown_message.mp3"
    
    pause 1.0
    
    "The words blur."
    "Your hands shake."
    
    pause 1.0
    
    "What do they know?"
    "How did they find out?"
    
    $ insights_unlocked.append("You're hiding something")
    show screen insight_popup("You're hiding something")
    pause
    hide screen insight_popup
    
    scene bg room_night
    stop music fadeout 2.0
    play music "audio/music/ambient_city.mp3" fadein 2.0
    
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
        voice "audio/narration/[persistent.narrator_voice]/act1_ignore.mp3"
    
    "You silence your phone and turn back to your work."
    
    pause 1.0
    
    "Problems can wait."
    "This deadline can't."
    
    $ insights_unlocked.append("You prioritize work over people")
    show screen insight_popup("You prioritize work over people")
    pause
    hide screen insight_popup
    
    play sound "audio/sfx/phone_buzz.mp3"
    pause 0.3
    play sound "audio/sfx/phone_buzz.mp3"
    pause 0.3
    play sound "audio/sfx/phone_buzz.mp3"
    
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
        voice "audio/narration/[persistent.narrator_voice]/act1_scene02.mp3"
    
    if recall("first_message_checked") != "none":
        "The other messages are still there."
        "Glowing. Waiting."
    else:
        "Your phone finally goes quiet."
        "But the messages are still there."
    
    pause 1.0
    
    "You know you can't ignore them forever."
    
    pause 1.0
    
    ## Transition to morning
    scene black with dissolve
    pause 1.0
    
    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act1_morning.mp3"
    
    "Morning comes too quickly."
    
    pause 1.0
    
    ## NEXT MAJOR SCENE
    jump act1_morning_confrontation

## ==========================================
## SECOND MAJOR CHOICE: Morning Confrontation
## ==========================================

label act1_morning_confrontation:
    
    scene bg kitchen_morning
    play music "audio/music/ambient_city.mp3" fadein 2.0
    
    show parent neutral at center
    
    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act1_confrontation.mp3"
    
    "Your parent is already at the table when you come down."
    "Coffee. Newspaper. The usual morning routine."
    "But their face is different today."
    
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
    "Wait for them to speak first."
    
    show parent serious
    
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
    
    show parent angry
    
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
    
    player "I actually have to—"
    
    show parent angry
    
    parent "Sit. Down."
    
    "The tone leaves no room for argument."
    
    "You sit."
    
    jump confrontation_reveal

label confrontation_reveal:
    
    show parent serious
    
    parent "Someone reached out to the university."
    pause 0.5
    parent "Made some... allegations."
    
    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act1_allegations.mp3"
    
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
    
    show parent suspicious
    
    parent "Really."
    pause 0.5
    parent "Because whoever made this claim seems pretty certain."
    
    "Their eyes bore into you."
    
    parent "And they have proof."
    
    $ insights_unlocked.append("Lying to authority makes things worse")
    show screen insight_popup("Lying to authority makes things worse")
    pause
    hide screen insight_popup
    
    jump confrontation_aftermath

label confrontation_clarify:
    
    $ truth += 5
    $ ambition += 5
    
    player "What exactly are they saying I saw?"
    
    show parent neutral
    
    parent "They didn't specify."
    pause 0.5
    parent "Just that it happened on campus."
    pause 0.5
    parent "Two months ago."
    
    "Two months ago."
    
    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act1_memory_trigger.mp3"
    
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
    
    show parent serious
    
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
    
    show parent listening
    
    parent "And?"
    
    player "One of them had... evidence. Of something."
    pause 0.5
    player "Against a professor."
    
    $ insights_unlocked.append("Academic corruption is involved")
    show screen insight_popup("Academic corruption is involved")
    pause
    hide screen insight_popup
    
    jump confrontation_aftermath

label postpone_truth:
    
    $ truth -= 5
    $ ambition += 5
    $ remember("truth_reveal_timing", "postponed")
    
    player "I need to think about this."
    pause 0.5
    player "Make sure I remember it correctly."
    
    show parent frustrated
    
    parent "You have until tonight."
    pause 0.5
    parent "After that, I'm calling the dean myself."
    
    jump confrontation_aftermath

label confrontation_aftermath:
    
    show parent neutral
    
    parent "This is serious."
    pause 0.5
    parent "Whatever you saw, whatever you know..."
    pause 0.5
    parent "It's going to come out."
    
    pause 1.0
    
    hide parent with dissolve
    
    if persistent.narrator_enabled:
        voice "audio/narration/[persistent.narrator_voice]/act1_aftermath.mp3"
    
    "They leave you alone at the table."
    
    pause 1.0
    
    "Your phone buzzes."
    play sound "audio/sfx/phone_buzz.mp3"
    
    "Another message."
    
    jump act1_phone_messages

## ==========================================
## TO BE CONTINUED...
## (Acts 2-4 would continue from here with 15+ more major scenes)
## ==========================================

label act1_phone_messages:
    
    ## Placeholder for next scene
    "TO BE CONTINUED..."
    
    jump end_of_chapter_1

label end_of_chapter_1:
    
    scene black with dissolve
    
    pause 1.0
    
    show screen records_sidebar
    
    centered "CHAPTER 1 COMPLETE"
    pause 1.0
    centered "Your choices have been recorded."
    
    pause 3.0
    
    hide screen records_sidebar
    
    ## Save game
    $ renpy.save("act1_checkpoint")
    
    ## Check if player wants Season 2 teaser
    if not persistent.seen_teaser:
        jump season2_teaser
    else:
        return

## Season 2 Teaser (Post-credits)
label season2_teaser:
    
    scene black
    
    pause 3.0
    
    centered "ONE YEAR LATER..."
    
    pause 2.0
    
    scene bg unknown_location
    play music "audio/music/tension_rising.mp3"
    
    "???" "You thought it was over?"
    
    pause 1.0
    
    "???" "It's only just beginning."
    
    pause 1.0
    
    scene black with dissolve
    stop music fadeout 2.0
    
    centered "PARALLEL WORLDS: SEASON 2"
    pause 1.0
    centered "COMING SOON"
    
    pause 2.0
    
    menu:
        "Want to be notified when Season 2 launches?"
        
        "Yes - Send me updates":
            $ persistent.wants_season2_emails = True
            centered "We'll email you at [persistent.player_email] when Season 2 is ready."
            pause 2.0
        
        "No thanks":
            pass
    
    $ persistent.seen_teaser = True
    
    return