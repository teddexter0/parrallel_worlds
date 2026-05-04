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

    if ui_is_small():
        frame:
            xalign 0.5
            yalign 0.5
            xsize 1740
            ymaximum 1010
            background "#08131df2"
            padding (54, 42)

            hbox:
                spacing 44

                vbox:
                    spacing 20
                    xsize 720

                    text "Parallel Worlds" size 56 color "#f5fbff" bold True
                    text "A choice-driven text RPG about pressure, secrets, and who you become." size 31 color "#b8e8f7" xmaximum 690

                    null height 4

                    textbutton "New Game":
                        action Start()
                        xsize 520
                        background "#2ec4b6"
                        padding (32, 20)
                        hover_background "#43dbc7"
                        text_color "#04111a"
                        text_size 32
                        text_xalign 0.5

                    textbutton "Continue":
                        action ShowMenu("load")
                        xsize 520
                        background "#ff9f1c"
                        padding (32, 20)
                        hover_background "#ffb347"
                        text_color "#1d1200"
                        text_size 32
                        text_xalign 0.5

                    hbox:
                        spacing 16

                        textbutton "Settings":
                            action ShowMenu("preferences")
                            xsize 252
                            background "#26384a"
                            padding (24, 16)
                            hover_background "#31495d"
                            text_color "#f8f9ff"
                            text_size 25
                            text_xalign 0.5

                        textbutton "Quit":
                            action Quit(confirm=True)
                            xsize 252
                            background "#26384a"
                            padding (24, 16)
                            hover_background "#31495d"
                            text_color "#f5fbff"
                            text_size 25
                            text_xalign 0.5

                frame:
                    xsize 840
                    background "#0e1d2be8"
                    padding (36, 32)

                    vbox:
                        spacing 20

                        text "How to play" size 40 color "#f5fbff" bold True
                        text "Read the scene, tap anywhere to move forward, then choose a response when the choice cards appear." size 29 color "#d9f2ff" xmaximum 760
                        text "Choices affect relationships, unlocked clues, and how later scenes read you." size 27 color "#b8e8f7" xmaximum 760
                        text "Use Records during play to review people, clues, and emotional stats." size 27 color "#b8e8f7" xmaximum 760

                        textbutton "Open quick guide":
                            action Show("web_howto_popup")
                            background "#f5fbff"
                            padding (28, 15)
                            hover_background "#d6f3ff"
                            text_color "#07141f"
                            text_size 25
                            text_xalign 0.5
                            xalign 0.0

    else:
        frame:
            xalign 0.07
            yalign 0.52
            xsize 690
            ysize 760
            background "#08131dee"
            padding (48, 42)

            vbox:
                spacing 20

                text "Parallel Worlds" size 58 color "#f5fbff" bold True
                text "A choice-driven text RPG about pressure, secrets, and who you become." size 24 color "#b8e8f7" xmaximum 580

                null height 4

                textbutton "New Game":
                    action Start()
                    xsize 410
                    background "#2ec4b6"
                    padding (26, 17)
                    hover_background "#43dbc7"
                    text_color "#04111a"
                    text_size 28
                    text_xalign 0.5

                textbutton "Continue":
                    action ShowMenu("load")
                    xsize 410
                    background "#ff9f1c"
                    padding (26, 17)
                    hover_background "#ffb347"
                    text_color "#1d1200"
                    text_size 28
                    text_xalign 0.5

                textbutton "Settings":
                    action ShowMenu("preferences")
                    xsize 410
                    background "#26384a"
                    padding (24, 15)
                    hover_background "#31495d"
                    text_color "#f8f9ff"
                    text_size 23
                    text_xalign 0.5

                textbutton "Refer Friends":
                    action Show("referral_screen")
                    xsize 410
                    background "#7c3058"
                    padding (24, 15)
                    hover_background "#91406a"
                    text_color "#fff8fb"
                    text_size 23
                    text_xalign 0.5

                textbutton "Quit":
                    action Quit(confirm=True)
                    xsize 410
                    background "#1f2a35"
                    padding (22, 14)
                    hover_background "#334556"
                    text_color "#f5fbff"
                    text_size 21
                    text_xalign 0.5

        frame:
            xalign 0.78
            yalign 0.46
            xsize 690
            background "#0e1d2bdd"
            padding (36, 32)

            vbox:
                spacing 18

                text "How to play" size 36 color "#f5fbff" bold True
                text "Read the scene, click or tap to continue, then choose your response when the cards appear." size 23 color "#d9f2ff" xmaximum 600
                text "Choices affect relationships, unlocked clues, and how later scenes respond to you." size 22 color "#b8e8f7" xmaximum 600
                text "Use Records during play to review people, clues, and emotional stats." size 22 color "#b8e8f7" xmaximum 600

                textbutton "Quick guide":
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
        xsize (1720 if ui_is_small() else 980)
        background "#0b1621f6"
        padding (48 if ui_is_small() else 42, 36 if ui_is_small() else 34)

        vbox:
            spacing (22 if ui_is_small() else 18)

            text "How to play" size (50 if ui_is_small() else 42) xalign 0.5 color "#f5fbff" bold True
            text "Read the scene, move forward, then pick your response when choice cards appear." size (31 if ui_is_small() else 23) xalign 0.5 color "#8ecae6" text_align 0.5

            frame:
                background "#122638"
                padding (28, 24)

                vbox:
                    spacing (16 if ui_is_small() else 12)
                    text "1. Start with New Game. Continue only works after you save." size (29 if ui_is_small() else 21) color "#f5fbff"
                    text "2. Advance with tap, click, Space, or Enter." size (29 if ui_is_small() else 21) color "#f5fbff"
                    text "3. When choices appear, pick the response you want to live with." size (29 if ui_is_small() else 21) color "#f5fbff"
                    text "4. Records keeps track of clues, people, and emotional stats." size (29 if ui_is_small() else 21) color "#f5fbff"

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
        ysize (360 if ui_is_small() else 300)
        left_padding (72 if ui_is_small() else 90)
        right_padding (72 if ui_is_small() else 90)
        top_padding (30 if ui_is_small() else 32)
        bottom_padding (38 if ui_is_small() else 38)

        if who is not None:
            text who id "who" color "#72ddf7" size (40 if ui_is_small() else 30) bold True xpos 0 ypos 0

        text what id "what" color "#f5fbff" size (42 if ui_is_small() else 32) xpos 0 ypos (70 if ui_is_small() else 58) xmaximum (1700 if ui_is_small() else 1500)


screen choice(items):

    modal True
    zorder 60

    frame:
        if ui_is_small():
            xalign 0.5
            xsize 1720
            yalign 0.46
        else:
            xalign 0.08
            xsize 780
            yalign 0.44
        background "#091723ed"
        padding (34 if ui_is_small() else 28, 30 if ui_is_small() else 28)

        vbox:
            spacing (22 if ui_is_small() else 18)

            text "Choose your move" size (30 if ui_is_small() else 23) color "#8ecae6" bold True

            for i in items:
                button:
                    action i.action
                    xfill True
                    background "#14324a"
                    hover_background "#214e70"
                    padding (30 if ui_is_small() else 24, 22 if ui_is_small() else 20)

                    text i.caption:
                        color "#f5fbff"
                        hover_color "#ffffff"
                        size (34 if ui_is_small() else 24)
                        xalign 0.0


## In-game HUD
screen game_hud():

    use records_button

    frame:
        xalign (0.98 if ui_is_small() else 0.965)
        yalign (0.035 if ui_is_small() else 0.05)
        background "#0b1621dd"
        padding (18 if ui_is_small() else 16, 10)

        text "Chapter [current_chapter] | Act [current_act]" size (22 if ui_is_small() else 16) color "#f5fbff"


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
