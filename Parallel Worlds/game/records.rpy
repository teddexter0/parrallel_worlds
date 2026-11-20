## FILE: game/records.rpy
## Sidebar Records system

screen records_sidebar(from_story=False):
    modal True
    zorder 90
    $ close_records = Return() if from_story else Hide("records_sidebar")
    key "game_menu" action close_records

    frame:
        xalign 0.0
        yalign 0.0
        xsize (990 if ui_is_small() else 570)
        ysize 1080
        background "#211b22f3"
        padding (34 if renpy.variant("small") else 26, 30 if renpy.variant("small") else 26)

        vbox:
            spacing 20

            hbox:
                spacing 28
                text "Records" size (48 if ui_is_small() else 39) color "#fff4df" bold True yalign 0.5
                textbutton "Close" style_prefix "pw_action" action close_records yminimum (100 if ui_is_small() else 64)

            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                ymaximum (865 if ui_is_small() else 900)

                use records_contents


screen records_contents():
    vbox:
        spacing 25

        vbox:
            spacing 12

            text "Characters" size (28 if ui_is_small() else 20) color "#e0b15f" bold True

            vbox:
                spacing 8

                $ jordan_status = " (No contact)" if jordan_no_contact else ""
                $ jordan_color = "#8f8477" if jordan_no_contact else "#fff4df"
                text "Jordan" + jordan_status color jordan_color size (24 if ui_is_small() else 16)

                $ casey_status = " (No contact)" if casey_no_contact else ""
                $ casey_color = "#8f8477" if casey_no_contact else "#fff4df"
                text "Casey" + casey_status color casey_color size (24 if ui_is_small() else 16)

                $ morgan_status = " (No contact)" if morgan_no_contact else ""
                $ morgan_color = "#8f8477" if morgan_no_contact else "#fff4df"
                text "Morgan" + morgan_status color morgan_color size (24 if ui_is_small() else 16)

                $ riley_status = " (No contact)" if riley_no_contact else ""
                $ riley_color = "#8f8477" if riley_no_contact else "#fff4df"
                text "Riley" + riley_status color riley_color size (24 if ui_is_small() else 16)

        null height 12

        vbox:
            spacing 12

            text "Locations" size (28 if ui_is_small() else 20) color "#ffd166" bold True

            vbox:
                spacing 8

                for location in locations_visited:
                    text location color "#fff4df" size (24 if ui_is_small() else 16)

                for location in locations_locked:
                    text location + " (Locked)" color "#8f8477" size (24 if ui_is_small() else 16)

        null height 12

        vbox:
            spacing 12

            text "Emotional Track" size (28 if ui_is_small() else 20) color "#ff8fab" bold True

            vbox:
                spacing 15

                vbox:
                    spacing 5
                    text "Mask (Social Conformity)" size (21 if ui_is_small() else 14) color "#dec9aa"
                    hbox:
                        bar value mask range 100 xsize (560 if ui_is_small() else 250) ysize (30 if ui_is_small() else 20)
                        text " [mask]%" size (21 if ui_is_small() else 14) color "#fff4df"

                vbox:
                    spacing 5
                    text "Truth (Integrity)" size (21 if ui_is_small() else 14) color "#dec9aa"
                    hbox:
                        bar value truth range 100 xsize (560 if ui_is_small() else 250) ysize (30 if ui_is_small() else 20)
                        text " [truth]%" size (21 if ui_is_small() else 14) color "#fff4df"

                vbox:
                    spacing 5
                    text "Ambition (Drive)" size (21 if ui_is_small() else 14) color "#dec9aa"
                    hbox:
                        bar value ambition range 100 xsize (560 if ui_is_small() else 250) ysize (30 if ui_is_small() else 20)
                        text " [ambition]%" size (21 if ui_is_small() else 14) color "#fff4df"

        null height 12

        vbox:
            spacing 12

            $ insight_count = len(insights_unlocked)
            text "Insights ([insight_count])" size (28 if ui_is_small() else 20) color "#d7a0a8" bold True

            vbox:
                spacing 8

                for insight in insights_unlocked[-8:]:
                    text "- " + insight size (20 if ui_is_small() else 13) color "#dec9aa"

        null height 12

        vbox:
            spacing 12

            text "Active Threads" size (28 if ui_is_small() else 20) color "#8ee6b7" bold True

            vbox:
                spacing 8

                for thread in active_threads:
                    text "- " + thread size (21 if ui_is_small() else 14) color "#fff4df"
