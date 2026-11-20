## Shared game interface.

init python:
    def ui_is_small():
        return renpy.variant("small") or renpy.variant("touch")


style pw_action is button:
    background "#243649"
    hover_background "#39556d"
    selected_background "#39556d"
    insensitive_background "#182534"
    padding (24, 15)
    yminimum 64

style pw_action_text is button_text:
    color "#f8f4ee"
    insensitive_color "#a8b4bf"
    size 32

style pw_primary is pw_action:
    background "#f3c77c"
    hover_background "#ffe0aa"

style pw_primary_text is pw_action_text:
    color "#161b24"
    bold True

style pw_action_button is pw_action
style pw_action_button_text is pw_action_text
style pw_primary_button is pw_primary
style pw_primary_button_text is pw_primary_text


screen main_menu():
    tag menu

    add "gui/main_menu.png"
    add Solid("#07142336")

    frame:
        xalign (0.07 if ui_is_small() else 0.09)
        yalign 0.52
        xsize (880 if ui_is_small() else 730)
        background "#0b1423e8"
        padding (50, 48)

        vbox:
            spacing 22

            text "Parallel Worlds" size (86 if ui_is_small() else 75) color "#fff8ea" bold True
            text "Three texts arrive just before midnight. One comes from a number you don't know." size (41 if ui_is_small() else 35) color "#e5e8ec" line_spacing 5

            null height 10

            if renpy.list_saved_games():
                textbutton "Continue" style_prefix "pw_primary" action Continue() xfill True
                textbutton "New game" style_prefix "pw_action" action Start() xfill True
            else:
                textbutton "Start story" style_prefix "pw_primary" action Start() xfill True

            hbox:
                spacing 14
                textbutton "Load" style_prefix "pw_action" action ShowMenu("load")
                textbutton "Settings" style_prefix "pw_action" action ShowMenu("preferences")
                textbutton "How to play" style_prefix "pw_action" action Show("web_howto_popup")

            text "Your profile and saves stay on this device." size (30 if ui_is_small() else 25) color "#cbd6df"


screen web_howto_popup(first_time=False):
    modal True
    zorder 200
    key "game_menu" action Hide("web_howto_popup")
    add Solid("#070f1bda")

    frame:
        xalign 0.5
        yalign 0.5
        xsize (1500 if ui_is_small() else 1050)
        background "#142235"
        padding (46, 38)

        vbox:
            spacing 24
            text "How to play" size 52 color "#fff8ea" bold True
            text "Tap, click, or press Space to advance. When a decision appears, select the response you want to take." size 35 color "#e5e8ec" line_spacing 5
            text "Open Pause to save, load, or change audio and text speed. Records tracks clues and relationships." size 35 color "#e5e8ec" line_spacing 5
            hbox:
                spacing 14
                textbutton "Back" style_prefix "pw_primary" action Hide("web_howto_popup")
                textbutton "Asset credits" style_prefix "pw_action" action [Hide("web_howto_popup"), Show("asset_credits")]


screen asset_credits():
    modal True
    zorder 200
    key "game_menu" action Hide("asset_credits")

    use pw_game_menu("Asset credits"):
        text "Cover and opening room: AI-generated artwork made for this game." size 34 color "#fff8ea"
        text "Café: {a=https://www.pexels.com/photo/interior-of-a-cafe-with-a-glass-wall-20281791/}Eren Arıcı{/a}. Nairobi skyline: {a=https://www.pexels.com/photo/stunning-nairobi-skyline-at-dusk-29069329/}Ken Mwaura{/a}. Both photographs are cropped and color-graded under the {a=https://www.pexels.com/license/}Pexels license{/a}." size 34 color "#fff8ea"
        text "Remaining backgrounds and portraits: procedural illustrations." size 34 color "#fff8ea"
        text "City, café and suspense audio: synthesized for this game." size 34 color "#fff8ea"
        textbutton "Back" style_prefix "pw_primary" action [Hide("asset_credits"), Show("web_howto_popup")]


screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        background "#0c1523f4"
        xalign 0.5
        yalign 0.98
        xsize (1820 if ui_is_small() else 1600)
        yminimum (250 if ui_is_small() else 220)
        padding (50, 30)

        vbox:
            spacing 12
            if who is not None:
                text who id "who" color "#f3c77c" size (42 if ui_is_small() else 35) bold True
            text what id "what" color "#fff8ea" size (50 if ui_is_small() else 43) line_spacing 5


screen choice(items):
    modal True
    zorder 60

    frame:
        xalign 0.5
        yalign 0.53
        xsize (1610 if ui_is_small() else 1150)
        background "#0c1523fa"
        padding (36, 30)

        viewport:
            ymaximum 680
            draggable True
            mousewheel True
            scrollbars ("vertical" if len(items) > 5 else None)

            vbox:
                spacing 16

                for item in items:
                    if item.action is None and not item.kwargs.get("disabled", False):
                        text item.caption size (47 if ui_is_small() else 39) color "#f3c77c" bold True
                    else:
                        textbutton item.caption:
                            style_prefix "pw_action"
                            action item.action
                            xfill True
                            yminimum (124 if ui_is_small() else 76)
                            text_size (42 if ui_is_small() else 35)


screen game_hud():
    zorder 70

    hbox:
        xalign 0.975
        yalign 0.032
        spacing 15

        text "Chapter [current_chapter]" yalign 0.5 size (37 if ui_is_small() else 27) color "#fff8ea" outlines [(3, "#0b1423")]
        textbutton "Records" style_prefix "pw_action" action Show("records_sidebar") yminimum (120 if ui_is_small() else 64)
        textbutton "Pause" style_prefix "pw_action" action ShowMenu("pause_menu") yminimum (120 if ui_is_small() else 64)


screen pw_game_menu(title):
    add "gui/main_menu.png"
    add Solid("#07111ddc")

    frame:
        xalign 0.5
        yalign 0.5
        xsize (1650 if ui_is_small() else 1280)
        ymaximum 960
        background "#101c2bf5"
        padding (44, 38)

        vbox:
            spacing 20
            text title size (65 if ui_is_small() else 52) color "#fff8ea" bold True
            transclude


screen pause_menu():
    tag menu
    key "game_menu" action Return()

    use pw_game_menu("Paused"):
        textbutton "Resume" style_prefix "pw_primary" action Return() xfill True
        textbutton "Save game" style_prefix "pw_action" action ShowMenu("save") xfill True
        textbutton "Load game" style_prefix "pw_action" action ShowMenu("load") xfill True
        textbutton "Settings" style_prefix "pw_action" action ShowMenu("preferences") xfill True
        textbutton "Main menu" style_prefix "pw_action" action MainMenu(confirm=True) xfill True


screen save():
    tag menu
    use pw_slots("Save game", FileSave)

screen load():
    tag menu
    use pw_slots("Load game", FileLoad, show_checkpoints=True)

screen pw_slots(title, slot_action, show_checkpoints=False):
    $ back_action = Return() if main_menu else ShowMenu("pause_menu")
    key "game_menu" action back_action

    use pw_game_menu(title):
        grid 3 2:
            spacing 14

            for slot in range(1, 7):
                textbutton FileTime(slot, format="%d %b, %H:%M", empty="Empty slot"):
                    style_prefix "pw_action"
                    action slot_action(slot)
                    xsize (500 if ui_is_small() else 388)
                    ysize 115
                    text_size (35 if ui_is_small() else 28)

        hbox:
            spacing 14
            textbutton "Auto" style_prefix "pw_action" action FilePage("auto")
            textbutton "Quick" style_prefix "pw_action" action FilePage("quick")
            for page in range(1, 5):
                textbutton str(page) style_prefix "pw_action" action FilePage(page)

        if show_checkpoints:
            hbox:
                spacing 14
                for slot, title in (("act1_checkpoint", "Chapter 2"), ("act2_checkpoint", "Chapter 3"), ("act3_checkpoint", "Chapter 5"), ("act4_final_save", "Ending")):
                    if renpy.can_load(slot):
                        textbutton title style_prefix "pw_action" action FileLoad(slot, slot=True)

        textbutton "Back" style_prefix "pw_primary" action back_action


screen preferences():
    tag menu
    $ back_action = Return() if main_menu else ShowMenu("pause_menu")
    key "game_menu" action back_action

    use pw_game_menu("Settings"):
        for label, setting in [("Text speed", "text speed"), ("Music volume", "music volume"), ("Sound effects", "sound volume")]:
            text label size (38 if ui_is_small() else 32) color "#fff8ea"
            bar value Preference(setting) ysize (62 if ui_is_small() else 36)
        textbutton "Mute all" style_prefix "pw_action" action Preference("all mute", "toggle")
        textbutton "Back" style_prefix "pw_primary" action back_action


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

        text message size 17 color "#fff4df"

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
        xsize (1300 if ui_is_small() else 920)
        background "#211b22f2"
        padding (42, 32)

        vbox:
            spacing 24
            xalign 0.5

            text "Added to Records" size (42 if ui_is_small() else 33) xalign 0.5 color "#e7a36f" bold True
            text insight_text size (41 if ui_is_small() else 32) xalign 0.5 color "#fff4df" text_align 0.5 line_spacing 4

            textbutton "Continue":
                action Return()
                style_prefix "pw_primary"
                xalign 0.5


screen ending_summary():

    modal True
    zorder 180

    add Solid("#100d12f2")

    frame:
        xalign 0.5
        yalign 0.5
        xsize (1740 if ui_is_small() else 1160)
        background "#211b22f5"
        padding (54 if ui_is_small() else 48, 44 if ui_is_small() else 38)

        vbox:
            spacing (24 if ui_is_small() else 20)

            text "Your ending" size (34 if ui_is_small() else 25) color "#e0b15f" bold True
            text ending_title size (58 if ui_is_small() else 46) color "#fff4df" bold True
            text ending_summary size (31 if ui_is_small() else 23) color "#dec9aa" line_spacing 5 xmaximum (1580 if ui_is_small() else 1040)

            null height 6

            hbox:
                spacing (48 if ui_is_small() else 34)

                vbox:
                    spacing 8
                    text "Defining choice" size (24 if ui_is_small() else 17) color "#b7aa9a"
                    text ending_path_label size (29 if ui_is_small() else 21) color "#fff4df" bold True

                vbox:
                    spacing 8
                    text "Dominant trait" size (24 if ui_is_small() else 17) color "#b7aa9a"
                    text dominant_trait size (29 if ui_is_small() else 21) color "#fff4df" bold True

                vbox:
                    spacing 8
                    text "Endings found" size (24 if ui_is_small() else 17) color "#b7aa9a"
                    text "[len(persistent.endings_unlocked)] of 6" size (29 if ui_is_small() else 21) color "#fff4df" bold True

            frame:
                background "#312936"
                padding (28, 24)

                grid 2 2:
                    spacing 18
                    text "Casey  [casey_relationship]/100" size (27 if ui_is_small() else 20) color "#fff4df"
                    text "Jordan  [jordan_relationship]/100" size (27 if ui_is_small() else 20) color "#fff4df"
                    text "Morgan  [morgan_relationship]/100" size (27 if ui_is_small() else 20) color "#fff4df"
                    text "Riley  [riley_relationship]/100" size (27 if ui_is_small() else 20) color "#fff4df"

            hbox:
                spacing 22

                textbutton "View Records":
                    action Return("records")
                    background "#3b333c"
                    padding (30, 15)
                    hover_background "#4c414b"
                    text_color "#fff4df"
                    text_size (26 if ui_is_small() else 19)

                textbutton "Continue":
                    action Return("continue")
                    background "#d9a441"
                    padding (30, 15)
                    hover_background "#f0bd58"
                    text_color "#20150a"
                    text_size (26 if ui_is_small() else 19)
