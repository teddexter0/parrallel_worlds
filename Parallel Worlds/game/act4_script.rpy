## FILE: game/act4_script.rpy
## ACT 4: THE RECKONING
## Chapters 5-7: Fallout, character epilogues, and the final ending.
## Four paths: A (Testified), B (Stayed Silent), C (Deal), D (Morgan Gambit)

## ==========================================
## ACT 4 OPENING
## ==========================================

label act4_opening:

    $ current_chapter = 5
    $ current_act = 4

    scene black with dissolve
    pause 1.0

    centered "ACT 4: THE RECKONING"
    pause 2.0

    scene bg campus_day
    play music "audio/music/ambient_city.wav" fadein 2.0

    show screen game_hud

    if persistent.narrator_enabled:
        pass

# voice "audio/narration/[persistent.narrator_voice]/act4_open.mp3"

    "Two weeks later."
    "The university posted a statement."
    "Professor Harkins has been placed on administrative leave pending a full review."


    "It's not an expulsion. It's not a conviction."
    "But it's something."


    "Your name is not in the statement."
    "But people who were in that building know."

    pause 1.0

    ## Route to different Act 4 paths based on Act 3 choice
    $ act2_choice = recall("act2_betrayal")

    if act2_choice == "chose_truth" or act2_choice == "convinced_morgan" or act2_choice == "tried_morgan_failed":
        jump act4_path_A_testified
    elif act2_choice == "chose_silence":
        jump act4_path_B_silent
    elif act2_choice == "chose_deal":
        jump act4_path_C_deal
    else:
        jump act4_path_A_testified


## ==========================================
## ACT 4 PATH A — TESTIFIED
## ==========================================

label act4_path_A_testified:

    scene bg campus_day

    if persistent.narrator_enabled:
        pass

# voice "audio/narration/[persistent.narrator_voice]/act4_pathA.mp3"

    "The first few days after, some people don't look at you."
    "Students who benefited from Harkins's system."
    "Students who liked him."
    "Students who are just scared of what the investigation might surface."


    "But other people do look at you."
    "Different students."
    "The ones who didn't have the grades to buy their way to safety."


    "One of them stops you after class."

    "Student" "You were the one who said something?"

    "You nod."

    "Student" "Thank you."


    "That's all."
    "They walk away."
    "It doesn't fix everything."
    "But it lands somewhere real."

    pause 1.5

    jump act4_A_riley_response


label act4_A_riley_response:

    scene bg library_steps_evening
    play music "audio/music/ambient_city.wav"

    show riley neutral at center

    if persistent.narrator_enabled:
        pass

# voice "audio/narration/[persistent.narrator_voice]/act4_A_riley.mp3"

    "Riley finds you at the library steps."
    "Same spot as before."
    "Different energy."

    riley "You came through."

    player "You went first. I just... followed."

    show riley quiet

    riley "That's not nothing."
    riley "Took me two months to find someone willing to follow."

    pause 1.0

    if riley_relationship >= 50:
        riley "I mean it. Thank you."
        $ riley_relationship += 10
    else:
        riley "I'm glad it's done."
        riley "For what it's worth."

    hide riley with dissolve

    jump act4_A_jordan_response


label act4_A_jordan_response:

    scene bg campus_day

    show jordan neutral at left

    if persistent.narrator_enabled:
        pass

# voice "audio/narration/[persistent.narrator_voice]/act4_A_jordan.mp3"

    "Jordan is waiting outside your class."

    jordan "Hey."

    player "Hey."

    pause 1.0

    if jordan_relationship >= 60:
        show jordan quiet

        jordan "I know what it took."
        jordan "I know it wasn't easy."
        jordan "You were always good."
        jordan "You just needed a minute to find it."

        $ jordan_relationship += 10

    elif jordan_relationship >= 40:
        jordan "It's done."
        jordan "That's what matters."

    else:
        show jordan serious

        jordan "You should have said something sooner."
        jordan "But you said it."
        jordan "So."

    hide jordan with dissolve

    jump act4_shared_morgan_check


## ==========================================
## ACT 4 PATH B — STAYED SILENT
## ==========================================

label act4_path_B_silent:

    scene bg campus_day

    if persistent.narrator_enabled:
        pass

# voice "audio/narration/[persistent.narrator_voice]/act4_pathB.mp3"

    "Riley's testimony went in alone."
    "Without corroboration."
    "The investigation stalled."


    "The university issued a statement about 'insufficient evidence for disciplinary action.'"
    "Professor Harkins returned to his classes."


    "You heard this from someone else."
    "You didn't follow the news closely."
    "You told yourself there was nothing you could have done differently."


    "You almost believe it."

    pause 1.0

    $ insights_unlocked.append("The version of you that stayed silent is still you")
    call screen insight_popup("The version of you that stayed silent is still you")

    jump act4_B_riley_response


label act4_B_riley_response:

    scene bg library_steps_evening
    play music "audio/music/tension_rising.wav" fadein 2.0

    show riley serious at center

    "Riley finds you."
    "You don't know how. You've been avoiding the east side of campus."

    riley "I wanted to look you in the face."

    "You let [riley_pronoun_object]."

    riley "You were there."

    "You don't answer."

    riley "You saw what I saw and you went in there and said nothing."


    menu:
        "What do you say?"

        "I know. I'm sorry.":
            jump B_riley_sorry

        "It's complicated.":
            jump B_riley_deflect

        "I had reasons.":
            jump B_riley_justify


label B_riley_sorry:

    $ truth += 10
    $ mask -= 5

    player "I know. I'm sorry."

    show riley quiet

    riley "..."
    riley "I believe you."
    riley "That doesn't help the people Harkins still has power over."
    riley "But I believe you're sorry."

    $ riley_relationship += 5

    jump B_riley_end


label B_riley_deflect:

    $ mask += 5
    $ riley_relationship -= 10

    player "It's complicated."

    show riley serious

    riley "It wasn't that complicated."

    "Riley walks away."
    "You watch [riley_pronoun_object] go."

    jump B_riley_end


label B_riley_justify:

    $ ambition += 5
    $ riley_relationship -= 15

    player "I had reasons."

    show riley neutral

    riley "Everyone does."

    "That's all [riley_pronoun_subject] says."
    "[riley_pronoun_subject.capitalize()] walks away."

    jump B_riley_end


label B_riley_end:

    hide riley with dissolve
    stop music fadeout 2.0
    play music "audio/music/ambient_city.wav" fadein 2.0

    pause 1.0

    "Late at night your phone buzzes."
    play sound "audio/sfx/phone_buzz.wav"
    pause 0.5

    scene bg phone_screen

    nvl clear
    "UNKNOWN" "{size=14}11:59 PM{/size}"
    "UNKNOWN" "i thought you were different."
    nvl clear

    scene bg room_night

    "You stare at it."
    "You don't know what to reply."
    "So you don't."

    jump act4_shared_morgan_check


## ==========================================
## ACT 4 PATH C — THE DEAL
## ==========================================

label act4_path_C_deal:

    scene bg campus_day

    if persistent.narrator_enabled:
        pass

# voice "audio/narration/[persistent.narrator_voice]/act4_pathC.mp3"

    "You testified."
    "But not before you got your guarantees."


    "Some people call it smart."
    "Jordan doesn't call it anything."
    "Not to your face."


    "The investigation moved forward."
    "Your name stayed out of the report, just like they promised."
    "Harkins is on leave."


    "You got what you wanted."
    "The outcome you wanted."
    "By the method you chose."

    pause 1.5

    $ insights_unlocked.append("Getting the right result the 'wrong' way still gets the result")
    call screen insight_popup("Getting the right result the 'wrong' way still gets the result")

    jump act4_C_morgan_response


label act4_C_morgan_response:

    scene bg cafe
    play sound "audio/sfx/cafe_ambience.wav"

    show morgan neutral at left

    morgan "You negotiated."

    player "I made sure I was protected."

    show morgan neutral

    morgan "I respect that actually."
    morgan "I wish I'd thought that clearly when I found the files."

    if morgan_relationship >= 60:
        morgan "Maybe we're more alike than I thought."
        $ morgan_relationship += 10
    else:
        morgan "Anyway. It's done."

    hide morgan with dissolve

    jump act4_C_anchor_response


label act4_C_anchor_response:

    scene bg rooftop_night
    play music "audio/music/ambient_city.wav"

    show anchor serious at right

    anchor "I heard you asked for protections before you said anything."

    player "I did."

    anchor "Smart."
    anchor "Is that how you feel about it?"


    menu:
        "How do you feel about it?"

        "Yes. I protected myself and still did the right thing.":
            jump C_feel_proud

        "Mostly. There's a small thing I'd rather not examine too closely.":
            jump C_feel_uneasy

        "Honestly? I'm not sure it was the right thing.":
            jump C_feel_doubt


label C_feel_proud:

    $ ambition += 10

    player "I protected myself and still did the right thing."

    anchor "And those two things can coexist for you."

    player "Can't they?"

    anchor "For some people."
    anchor "Good for you if you're one of them."

    jump act4_shared_final_anchor


label C_feel_uneasy:

    $ truth += 5

    player "Mostly."

    anchor "That 'mostly' is doing a lot of work."

    player "I know."

    anchor "Keep paying attention to it."

    jump act4_shared_final_anchor


label C_feel_doubt:

    $ truth += 15

    player "I'm not sure it was the right thing."

    anchor "Why not?"

    player "Because I made it about me first."

    anchor "And yet it still helped people."


    anchor "Most choices aren't clean."
    anchor "The question is whether you keep growing inside the mess."

    jump act4_shared_final_anchor


## ==========================================
## SHARED MORGAN CHECK (PATHS A + B)
## ==========================================

label act4_shared_morgan_check:

    scene bg campus_day

    if persistent.narrator_enabled:
        pass

# voice "audio/narration/[persistent.narrator_voice]/act4_morgan.mp3"

    "Morgan messages you."

    scene bg phone_screen

    nvl clear
    "MORGAN" "however you're feeling about all this"
    "MORGAN" "i'm sorry you got pulled into it"
    "MORGAN" "that's on me"
    nvl clear

    scene bg campus_day

    menu:
        "How do you reply?"

        "You don't have to apologize.":
            jump morgan_reply_kind

        "Thank you for saying that.":
            jump morgan_reply_accept

        "You're right. It is on you.":
            jump morgan_reply_cold


label morgan_reply_kind:

    $ morgan_relationship += 10

    scene bg phone_screen

    nvl clear
    "YOU" "you don't have to apologize"
    "MORGAN" "yeah i do"
    "MORGAN" "but thank you"
    nvl clear

    scene bg campus_day

    jump act4_shared_final_anchor


label morgan_reply_accept:

    $ morgan_relationship += 5

    scene bg phone_screen

    nvl clear
    "YOU" "thank you for saying that"
    "MORGAN" "i mean it"
    nvl clear

    scene bg campus_day

    jump act4_shared_final_anchor


label morgan_reply_cold:

    $ morgan_relationship -= 15
    $ truth += 5

    scene bg phone_screen

    nvl clear
    "YOU" "you're right. it is."
    "MORGAN" "..."
    nvl clear

    scene bg campus_day

    "Morgan doesn't reply after that."

    jump act4_shared_final_anchor


## ==========================================
## FINAL ANCHOR SCENE (ALL PATHS)
## ==========================================

label act4_shared_final_anchor:

    scene bg rooftop_night
    play music "audio/music/ambient_city.wav" fadein 2.0

    if persistent.narrator_enabled:
        pass

# voice "audio/narration/[persistent.narrator_voice]/act4_anchor_final.mp3"

    "The roof."
    "Last time for a while, maybe."
    "The semester is almost over."

    show anchor neutral at right

    anchor "So."

    player "So."


    anchor "How are you?"
    anchor "And I mean actually."

    pause 1.5

    ## Dynamic reflection based on stats
    if truth >= 70:
        player "Tired. But clear."
        anchor "Clear is rare."
        anchor "Hold onto it."

    elif mask >= 70:
        player "Fine. I think."
        anchor "You think."
        anchor "Keep thinking."

    elif ambition >= 70:
        player "I got through it. I'm still here."
        anchor "You are."
        anchor "The question is who 'here' is."

    else:
        player "I don't fully know yet."
        anchor "That's the most honest thing you've said."
        anchor "Good."


    anchor "You know what I've learned?"

    player "What?"

    show anchor quiet

    anchor "Character isn't what you do when everything is easy."
    anchor "It's what you do when the cost is real."


    "The city stretches out below."
    "The semester ends."
    "Whatever comes next — it comes."

    pause 1.0

    hide anchor with dissolve

    jump act4_epilogue


## ==========================================
## EPILOGUE — RELATIONSHIP ENDINGS
## ==========================================

label act4_epilogue:

    $ current_chapter = 6

    scene black with dissolve
    stop music fadeout 2.0
    pause 1.0

    centered "EPILOGUE"
    pause 2.0

    ## Casey
    if casey_relationship >= 70:
        scene bg cafe
        play music "audio/music/ambient_city.wav" fadein 2.0
        show casey neutral at center

        "Casey is waiting for you at your usual table."
        "Coffee already ordered."
        "Knows your order by heart."

        casey "You look better."
        player "I feel better."
        casey "Good."

        if pursuing_casey:
            casey "We should celebrate somehow."
            player "Yeah?"
            casey "Yeah."
            "Something in [casey_pronoun_possessive] smile stays."
            $ insights_unlocked.append("You and Casey found each other in the wreckage")
            call screen insight_popup("You and Casey found each other in the wreckage")

        hide casey with dissolve

    elif casey_relationship <= 30:
        "Casey is still around."
        "But there's a distance that wasn't there before."
        "You made choices [casey_pronoun_subject] couldn't fully understand."
        "Or maybe couldn't forgive."
        pause 1.0

    ## Jordan
    if jordan_relationship >= 70:
        scene bg campus_day
        show jordan neutral at center

        "Jordan finds you before the last day of term."
        jordan "Next semester."
        player "What about it?"
        jordan "Don't be a stranger."

        $ insights_unlocked.append("Jordan respects you now")
        call screen insight_popup("Jordan respects you now")

        hide jordan with dissolve

    elif jordan_relationship <= 30:
        "Jordan and you orbit the same campus without overlapping."
        "Some things don't repair easily."
        pause 1.0

    ## Morgan
    if morgan_relationship >= 60:
        scene bg campus_day
        show morgan neutral at center

        morgan "I'm going to start over next year."
        morgan "Transfer. Different school."
        player "Running?"
        show morgan serious
        morgan "Resetting."
        morgan "There's a difference."

        hide morgan with dissolve

    ## Riley
    if riley_relationship >= 50:
        scene bg library_steps_evening
        show riley neutral at center

        "Riley on the library steps."
        "Like the first time."
        "But lighter."

        riley "I'm writing it all down."
        player "For what?"
        riley "So it doesn't get erased."
        riley "Things like this — they get erased if no one keeps the record."

        $ insights_unlocked.append("Riley will keep the record")
        call screen insight_popup("Riley will keep the record")

        hide riley with dissolve

    jump act4_final_ending


## ==========================================
## FINAL ENDING — BASED ON DOMINANT STAT
## ==========================================

label act4_final_ending:

    scene bg room_night
    play music "audio/music/ambient_city.wav" fadein 2.0

    if persistent.narrator_enabled:
        pass

# voice "audio/narration/[persistent.narrator_voice]/act4_final.mp3"

    "Your room."
    "Late."
    "Same laptop. Same light."
    "But you're not the same."

    pause 2.0

    $ finalize_story_ending()

    if ending_id == "open_record":
        "You put your name beside Riley's in the final record."
        "Other students add theirs. Then staff. Then alumni."
        "The truth stops belonging to any one person, which is why it becomes harder to bury."

    elif ending_id == "bridge":
        "The messages do not stop when the case does."
        "Casey checks in. Jordan argues, then listens. Morgan sends a song without explanation."
        "You did not save every relationship, but you learned how to stay when staying is difficult."

    elif ending_id == "second_witness":
        "Morgan's statement reaches you before midnight."
        "It begins with your name and ends with theirs."
        "Neither of you was brave alone. Together, you were enough."

    elif ending_id == "silent_witness":
        "You write the testimony you could not say in the room."
        "It does not undo your silence, but it refuses to disguise it."
        "Tomorrow, you will ask Riley whether the record still has room for one late voice."

    elif ending_id == "protected_self":
        "Your calendar fills again. Your grades recover. The noise moves elsewhere."
        "Safety feels exactly like you asked it to feel."
        "Only now do you understand how quiet an empty room can become."

    elif ending_id == "brokered_truth":
        "The protections arrive in writing before your statement becomes public."
        "The university calls it procedure. You call it leverage."
        "You told the truth, but you also taught the institution that your safety was not free."

    $ ending_insight = "Ending unlocked: " + ending_title
    if ending_insight not in insights_unlocked:
        $ insights_unlocked.append(ending_insight)

    call screen insight_popup(ending_insight)

    pause 1.5

    "Your phone is face-down."
    "No messages waiting."
    "The first quiet evening in weeks."


    "You open a new document."
    "Blank page."
    "Cursor blinking."


    "You start typing."

    pause 2.0

    scene black with dissolve
    stop music fadeout 3.0
    pause 1.5

    jump act4_game_end


## ==========================================
## GAME END / CHAPTER 7 COMPLETE
## ==========================================

label act4_game_end:

    $ current_chapter = 7

    hide screen game_hud
    $ renpy.save("act4_final_save")

    call screen ending_summary
    while _return == "records":
        call screen records_sidebar(from_story=True)
        call screen ending_summary

    ## Hand off to the existing season 2 teaser logic
    if not persistent.seen_teaser:
        jump season2_teaser
    else:
        return


