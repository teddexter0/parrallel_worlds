## FILE: game/records.rpy
## Sidebar Records system

screen records_sidebar():
    modal True
    zorder 90
    key "game_menu" action Hide("records_sidebar")

    frame:
        xalign 0.0
        yalign 0.0
        xsize (990 if ui_is_small() else 570)
        ysize 1080
        background "#211b22f3"
        padding (34 if renpy.variant("small") else 26, 30 if renpy.variant("small") else 26)

        viewport:
            scrollbars "vertical"
            mousewheel True

            vbox:
                spacing 25

                vbox:
                    spacing 10
                    xalign 0.5

                    text "Parallel Worlds" size (34 if renpy.variant("small") else 26) xalign 0.5 color "#fff4df" bold True
                    text "Records" size (27 if renpy.variant("small") else 20) xalign 0.5 color "#e0b15f"

                null height 14

                vbox:
                    spacing 12

                    text "Characters" size (28 if renpy.variant("small") else 20) color "#e0b15f" bold True

                    vbox:
                        spacing 8

                        $ jordan_status = " [No Contact]" if jordan_no_contact else ""
                        $ jordan_color = "#8f8477" if jordan_no_contact else "#fff4df"
                        textbutton "Jordan" + jordan_status:
                            action NullAction()
                            text_color jordan_color
                            text_size (24 if renpy.variant("small") else 16)

                        $ casey_status = " [No Contact]" if casey_no_contact else ""
                        $ casey_color = "#8f8477" if casey_no_contact else "#fff4df"
                        textbutton "Casey" + casey_status:
                            action NullAction()
                            text_color casey_color
                            text_size (24 if renpy.variant("small") else 16)

                        $ morgan_status = " [No Contact]" if morgan_no_contact else ""
                        $ morgan_color = "#8f8477" if morgan_no_contact else "#fff4df"
                        textbutton "Morgan" + morgan_status:
                            action NullAction()
                            text_color morgan_color
                            text_size (24 if renpy.variant("small") else 16)

                        $ riley_status = " [No Contact]" if riley_no_contact else ""
                        $ riley_color = "#8f8477" if riley_no_contact else "#fff4df"
                        textbutton "Riley" + riley_status:
                            action NullAction()
                            text_color riley_color
                            text_size (24 if renpy.variant("small") else 16)

                null height 12

                vbox:
                    spacing 12

                    text "Locations" size (28 if renpy.variant("small") else 20) color "#ffd166" bold True

                    vbox:
                        spacing 8

                        for location in locations_visited:
                            textbutton location:
                                action NullAction()
                                text_color "#fff4df"
                                text_size (24 if renpy.variant("small") else 16)

                        for location in locations_locked:
                            textbutton location + " (Locked)":
                                action NullAction()
                                text_color "#8f8477"
                                text_size (24 if renpy.variant("small") else 16)

                null height 12

                vbox:
                    spacing 12

                    text "Emotional Track" size (28 if renpy.variant("small") else 20) color "#ff8fab" bold True

                    vbox:
                        spacing 15

                        vbox:
                            spacing 5
                            text "Mask (Social Conformity)" size (21 if renpy.variant("small") else 14) color "#dec9aa"
                            hbox:
                                bar value mask range 100 xsize (560 if renpy.variant("small") else 250) ysize (30 if renpy.variant("small") else 20)
                                text " [mask]%" size (21 if renpy.variant("small") else 14) color "#fff4df"

                        vbox:
                            spacing 5
                            text "Truth (Integrity)" size (21 if renpy.variant("small") else 14) color "#dec9aa"
                            hbox:
                                bar value truth range 100 xsize (560 if renpy.variant("small") else 250) ysize (30 if renpy.variant("small") else 20)
                                text " [truth]%" size (21 if renpy.variant("small") else 14) color "#fff4df"

                        vbox:
                            spacing 5
                            text "Ambition (Drive)" size (21 if renpy.variant("small") else 14) color "#dec9aa"
                            hbox:
                                bar value ambition range 100 xsize (560 if renpy.variant("small") else 250) ysize (30 if renpy.variant("small") else 20)
                                text " [ambition]%" size (21 if renpy.variant("small") else 14) color "#fff4df"

                null height 12

                vbox:
                    spacing 12

                    $ insight_count = len(insights_unlocked)
                    text "Insights ([insight_count])" size (28 if renpy.variant("small") else 20) color "#d7a0a8" bold True

                    vbox:
                        spacing 8

                        for insight in insights_unlocked[-8:]:
                            text "- " + insight size (20 if renpy.variant("small") else 13) color "#dec9aa"

                null height 12

                vbox:
                    spacing 12

                    text "Active Threads" size (28 if renpy.variant("small") else 20) color "#8ee6b7" bold True

                    vbox:
                        spacing 8

                        for thread in active_threads:
                            text "- " + thread size (21 if renpy.variant("small") else 14) color "#fff4df"

                null height 30

                textbutton "Close Records":
                    action Hide("records_sidebar")
                    xalign 0.5
                    background "#8d5d66"
                    padding (30, 12)
                    hover_background "#a06f77"
                    text_color "#fff4df"
                    text_size (24 if renpy.variant("small") else 16)


screen records_button():
    textbutton "Records":
        xalign (0.03 if renpy.variant("small") else 0.08)
        yalign (0.82 if renpy.variant("small") else 0.88)
        action Show("records_sidebar")
        background "#211b22dd"
        padding (26 if renpy.variant("small") else 22, 15 if renpy.variant("small") else 14)
        hover_background "#4c414b"
        text_color "#fff4df"
        text_size (23 if renpy.variant("small") else 17)
