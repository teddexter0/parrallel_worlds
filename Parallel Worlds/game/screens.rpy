## FILE: game/screens.rpy
## UI Screens and menus

init python:
    def ui_is_small():
        return renpy.variant("small")


screen main_menu():

    tag menu

    add Solid("#07141f")
    add "gui/main_menu.png"
    add Solid("#07141fcc")

    frame:
        xalign 0.08
        yalign 0.52
        xsize 760
        ysize 860
        background "#08131dee"
        padding (55, 50)

        vbox:
            spacing 24

            text "PARALLEL WORLDS" size 66 color "#f5fbff" bold True
            text "A social thriller about pressure, secrets, and who you become online and off." size 23 color "#8ecae6" xmaximum 620

            null height 8

            textbutton "NEW GAME":
                action Start()
                xsize 430
                background "#2ec4b6"
                padding (28, 20)
                hover_background "#43dbc7"
                text_color "#04111a"
                text_size 28
                text_xalign 0.5

            textbutton "CONTINUE":
                action ShowMenu("load")
                xsize 430
                background "#ff9f1c"
                padding (28, 20)
                hover_background "#ffb347"
                text_color "#1d1200"
                text_size 28
                text_xalign 0.5

            textbutton "SETTINGS":
                action ShowMenu("preferences")
                xsize 430
                background "#5e60ce"
                padding (28, 20)
                hover_background "#7275da"
                text_color "#f8f9ff"
                text_size 24
                text_xalign 0.5

            textbutton "REFER FRIENDS":
                action Show("referral_screen")
                xsize 430
                background "#ef476f"
                padding (28, 20)
                hover_background "#f06184"
                text_color "#fff8fb"
                text_size 24
                text_xalign 0.5

            textbutton "QUIT":
                action Quit(confirm=True)
                xsize 430
                background "#1f2a35"
                padding (28, 20)
                hover_background "#334556"
                text_color "#f5fbff"
                text_size 22
                text_xalign 0.5

    frame:
        xalign 0.80
        yalign 0.36
        xsize 620
        background "#0e1d2bdd"
        padding (34, 30)

        vbox:
            spacing 18

            text "PLAY ON WEB" size 32 color "#f5fbff" bold True
            text "Tap or click NEW GAME first. Browser audio normally unlocks after your first interaction." size 21 color "#d9f2ff" xmaximum 540

            hbox:
                spacing 14

                frame:
                    xsize 258
                    background "#14324acc"
                    padding (20, 18)

                    vbox:
                        spacing 10
                        text "HOW IT FEELS" size 20 color "#72ddf7" bold True
                        text "Branching dialogue, message screens, pop-up alerts, and relationship choices." size 17 color "#eef8ff"

                frame:
                    xsize 258
                    background "#2d1532cc"
                    padding (20, 18)

                    vbox:
                        spacing 10
                        text "CURRENT BUILD" size 20 color "#ff8fab" bold True
                        text "Some art and sound are still placeholder assets, but the story flow is playable." size 17 color "#fff0f4"

            textbutton "HOW TO PLAY":
                action Show("web_howto_popup")
                background "#f5fbff"
                padding (22, 14)
                hover_background "#d6f3ff"
                text_color "#07141f"
                text_size 20
                text_xalign 0.5
                xalign 0.0

    if not persistent.seen_web_howto:
        use web_howto_popup(first_time=True)


screen web_howto_popup(first_time=False):

    modal True
    zorder 200

    add Solid("#02070cb8")

    frame:
        xalign 0.5
        yalign 0.52
        xsize 980
        background "#0b1621f6"
        padding (42, 34)

        vbox:
            spacing 18

            text "HOW TO PLAY" size 42 xalign 0.5 color "#f5fbff" bold True
            text "Think of this build like an interactive drama feed: read, tap forward, and pick your response when cards appear." size 23 xalign 0.5 color "#8ecae6" text_align 0.5

            frame:
                background "#122638"
                padding (24, 22)

                vbox:
                    spacing 12
                    text "1. Start with NEW GAME. CONTINUE only works after you have a save." size 21 color "#f5fbff"
                    text "2. Advance with click, tap, Space, or Enter." size 21 color "#f5fbff"
                    text "3. Choice cards now appear away from the browser menu so they are easier to hit." size 21 color "#f5fbff"
                    text "4. If sound is silent, interact once and check the in-game Preferences volume." size 21 color "#f5fbff"
                    text "5. Use RECORDS during play to review unlocked clues and relationship state." size 21 color "#f5fbff"

            hbox:
                spacing 20
                xalign 0.5

                textbutton "START PLAYING":
                    action [SetField(persistent, "seen_web_howto", True), Hide("web_howto_popup")]
                    background "#2ec4b6"
                    padding (30, 14)
                    hover_background "#43dbc7"
                    text_color "#04111a"
                    text_size 20

                if not first_time:
                    textbutton "CLOSE":
                        action Hide("web_howto_popup")
                        background "#233241"
                        padding (30, 14)
                        hover_background "#31495d"
                        text_color "#f5fbff"
                        text_size 20


screen say(who, what):

    style_prefix "say"

    window:
        id "window"
        background "#07131ee8"
        xalign 0.5
        yalign 1.0
        xfill True
        ysize 320
        left_padding 90
        right_padding 90
        top_padding 34
        bottom_padding 42

        if who is not None:
            text who id "who" color "#72ddf7" size 34 bold True xpos 0 ypos 0

        text what id "what" color "#f5fbff" size 34 xpos 0 ypos 62 xmaximum 1500


screen choice(items):

    modal True
    zorder 60

    frame:
        if ui_is_small():
            xpos 32
            xsize 1016
            yalign 0.43
        else:
            xpos 86
            xsize 760
            yalign 0.44
        background "#091723ed"
        padding (28, 28)

        vbox:
            spacing 18

            text "Choose your move" size 23 color "#8ecae6" bold True

            for i in items:
                button:
                    action i.action
                    xfill True
                    background "#14324a"
                    hover_background "#214e70"
                    padding (24, 20)

                    text i.caption:
                        color "#f5fbff"
                        hover_color "#ffffff"
                        size (24 if not ui_is_small() else 30)
                        xalign 0.0


## In-game HUD
screen game_hud():

    use records_button

    frame:
        xalign 0.965
        yalign 0.05
        background "#0b1621dd"
        padding (16, 10)

        text "Chapter [current_chapter] | Act [current_act]" size 16 color "#f5fbff"


## General notification system
screen show_notification(message, notification_type="neutral"):

    zorder 100

    frame:
        xalign 0.96
        yalign 0.16
        xsize 420
        padding (22, 18)

        at notification_slide

        if notification_type == "good":
            background "#0f5132"
        elif notification_type == "bad":
            background "#7a1f2b"
        elif notification_type == "mystery":
            background "#7a4a10"
        else:
            background "#264653"

        text message size 17 color "#f5fbff"

    timer 3.5 action Hide("show_notification")


transform notification_slide:
    xoffset 500
    easein 0.35 xoffset 0
    pause 2.8
    easeout 0.35 xoffset 500


screen insight_popup(insight_text):

    zorder 100
    modal True

    frame:
        xalign 0.5
        yalign 0.28
        xsize 700
        background "#08131ff2"
        padding (42, 32)

        vbox:
            spacing 24
            xalign 0.5

            text "NEW INSIGHT" size 31 xalign 0.5 color "#ff8fab" bold True
            text insight_text size 20 xalign 0.5 color "#f5fbff" text_align 0.5

            textbutton "Save to Records":
                action Hide("insight_popup")
                xalign 0.5
                background "#2ec4b6"
                padding (30, 12)
                hover_background "#43dbc7"
                text_color "#04111a"
                text_size 18


screen streak_notification(days):

    zorder 100

    frame:
        xalign 0.5
        yalign 0.18
        background "#123524"
        padding (42, 26)

        vbox:
            spacing 8
            xalign 0.5

            text "[days] DAY STREAK" size 34 xalign 0.5 color "#f5fbff" bold True
            text "Keep the momentum going." size 18 xalign 0.5 color "#8ee6b7"


screen chapter_locked():

    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xsize 760
        ysize 560
        background "#08131ff5"
        padding (50, 40)

        vbox:
            spacing 28
            xalign 0.5

            text "CHAPTER LOCKED" size 38 xalign 0.5 color "#ff8fab" bold True
            text "Unlock the next chapter in one of these ways:" size 22 xalign 0.5 color "#f5fbff"

            frame:
                xalign 0.5
                background "#112434"
                padding (24, 22)

                vbox:
                    spacing 14
                    text "Wait until tomorrow for the free unlock." size 20 color "#8ee6b7"
                    text "Pay $2 to unlock immediately." size 20 color "#ffd166"
                    text "Refer 5 friends. Remaining: [get_referral_progress()]." size 20 color "#72ddf7"

            hbox:
                spacing 22
                xalign 0.5

                textbutton "WAIT":
                    action Return("wait")
                    background "#2b9348"
                    padding (35, 15)
                    hover_background "#3bac59"
                    text_color "#f5fbff"
                    text_size 18

                textbutton "PAY $2":
                    action Return("pay")
                    background "#ff9f1c"
                    padding (35, 15)
                    hover_background "#ffb347"
                    text_color "#1d1200"
                    text_size 18

                textbutton "REFER":
                    action [Hide("chapter_locked"), Show("referral_screen")]
                    background "#3a86ff"
                    padding (35, 15)
                    hover_background "#5a9cff"
                    text_color "#f5fbff"
                    text_size 18
