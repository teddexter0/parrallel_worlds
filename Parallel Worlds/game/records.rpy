## FILE: game/records.rpy
## Sidebar Records system

screen records_sidebar():
    modal True

    frame:
        xalign 0.0
        yalign 0.0
        xsize 430
        ysize 1080
        background "#091723f3"
        padding (26, 26)

        viewport:
            scrollbars "vertical"
            mousewheel True

            vbox:
                spacing 25

                vbox:
                    spacing 10
                    xalign 0.5

                    text "PARALLEL WORLDS" size 26 xalign 0.5 color "#f5fbff" bold True
                    text "RECORDS" size 20 xalign 0.5 color "#72ddf7"

                null height 14

                vbox:
                    spacing 12

                    text "CHARACTERS" size 20 color "#72ddf7" bold True

                    vbox:
                        spacing 8

                        $ jordan_status = " [NO CONTACT]" if jordan_no_contact else ""
                        $ jordan_color = "#5d7688" if jordan_no_contact else "#f5fbff"
                        textbutton "Jordan" + jordan_status:
                            action NullAction()
                            text_color jordan_color
                            text_size 16

                        $ casey_status = " [NO CONTACT]" if casey_no_contact else ""
                        $ casey_color = "#5d7688" if casey_no_contact else "#f5fbff"
                        textbutton "Casey" + casey_status:
                            action NullAction()
                            text_color casey_color
                            text_size 16

                        $ morgan_status = " [NO CONTACT]" if morgan_no_contact else ""
                        $ morgan_color = "#5d7688" if morgan_no_contact else "#f5fbff"
                        textbutton "Morgan" + morgan_status:
                            action NullAction()
                            text_color morgan_color
                            text_size 16

                        $ riley_status = " [NO CONTACT]" if riley_no_contact else ""
                        $ riley_color = "#5d7688" if riley_no_contact else "#f5fbff"
                        textbutton "Riley" + riley_status:
                            action NullAction()
                            text_color riley_color
                            text_size 16

                null height 12

                vbox:
                    spacing 12

                    text "LOCATIONS" size 20 color "#ffd166" bold True

                    vbox:
                        spacing 8

                        for location in locations_visited:
                            textbutton location:
                                action NullAction()
                                text_color "#f5fbff"
                                text_size 16

                        for location in locations_locked:
                            textbutton location + " (LOCKED)":
                                action NullAction()
                                text_color "#5d7688"
                                text_size 16

                null height 12

                vbox:
                    spacing 12

                    text "EMOTIONAL TRACK" size 20 color "#ff8fab" bold True

                    vbox:
                        spacing 15

                        vbox:
                            spacing 5
                            text "Mask (Social Conformity)" size 14 color "#d7e6f1"
                            hbox:
                                bar value mask range 100 xsize 250 ysize 20
                                text " [mask]%" size 14 color "#f5fbff"

                        vbox:
                            spacing 5
                            text "Truth (Integrity)" size 14 color "#d7e6f1"
                            hbox:
                                bar value truth range 100 xsize 250 ysize 20
                                text " [truth]%" size 14 color "#f5fbff"

                        vbox:
                            spacing 5
                            text "Ambition (Drive)" size 14 color "#d7e6f1"
                            hbox:
                                bar value ambition range 100 xsize 250 ysize 20
                                text " [ambition]%" size 14 color "#f5fbff"

                null height 12

                vbox:
                    spacing 12

                    $ insight_count = len(insights_unlocked)
                    text "INSIGHTS ([insight_count])" size 20 color "#c77dff" bold True

                    vbox:
                        spacing 8

                        for insight in insights_unlocked[-8:]:
                            text "- " + insight size 13 color "#d7e6f1"

                null height 12

                vbox:
                    spacing 12

                    text "ACTIVE THREADS" size 20 color "#8ee6b7" bold True

                    vbox:
                        spacing 8

                        for thread in active_threads:
                            text "- " + thread size 14 color "#f5fbff"

                null height 30

                textbutton "CLOSE RECORDS":
                    action Hide("records_sidebar")
                    xalign 0.5
                    background "#ef476f"
                    padding (30, 12)
                    hover_background "#f06184"
                    text_color "#f5fbff"
                    text_size 16


screen records_button():
    textbutton "RECORDS":
        xalign 0.08
        yalign 0.88
        action Show("records_sidebar")
        background "#0b1621dd"
        padding (22, 14)
        hover_background "#214e70"
        text_color "#f5fbff"
        text_size 17
