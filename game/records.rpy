## FILE: game/records.rpy
## Sidebar Records system (detective-style)

screen records_sidebar():
    modal True
    
    frame:
        xalign 0.0
        yalign 0.0
        xsize 400
        ysize 1080
        background "#0a0a0a"
        padding (25, 25)
        
        viewport:
            scrollbars "vertical"
            mousewheel True
            
            vbox:
                spacing 25
                
                ## HEADER
                vbox:
                    spacing 10
                    xalign 0.5
                    
                    text "PARALLEL WORLDS" size 26 xalign 0.5 color "#FFD700" bold True
                    text "RECORDS" size 20 xalign 0.5 color "#FFF"
                
                null height 20
                
                ## CHARACTERS
                vbox:
                    spacing 12
                    
                    text "📖 CHARACTERS" size 20 color "#4A90E2" bold True
                    
                    vbox:
                        spacing 8
                        
                        $ jordan_status = " [NO CONTACT]" if jordan_no_contact else ""
                        $ jordan_color = "#555" if jordan_no_contact else "#FFF"
                        textbutton "Jordan" + jordan_status:
                            action NullAction()
                            text_color jordan_color
                            text_size 16
                        
                        $ casey_status = " [NO CONTACT]" if casey_no_contact else ""
                        $ casey_color = "#555" if casey_no_contact else "#FFF"
                        textbutton "Casey" + casey_status:
                            action NullAction()
                            text_color casey_color
                            text_size 16
                        
                        $ morgan_status = " [NO CONTACT]" if morgan_no_contact else ""
                        $ morgan_color = "#555" if morgan_no_contact else "#FFF"
                        textbutton "Morgan" + morgan_status:
                            action NullAction()
                            text_color morgan_color
                            text_size 16
                        
                        $ riley_status = " [NO CONTACT]" if riley_no_contact else ""
                        $ riley_color = "#555" if riley_no_contact else "#FFF"
                        textbutton "Riley" + riley_status:
                            action NullAction()
                            text_color riley_color
                            text_size 16
                
                null height 20
                
                ## LOCATIONS
                vbox:
                    spacing 12
                    
                    text "📍 LOCATIONS" size 20 color "#F39C12" bold True
                    
                    vbox:
                        spacing 8
                        
                        for location in locations_visited:
                            textbutton location:
                                action NullAction()
                                text_color "#FFF"
                                text_size 16
                        
                        for location in locations_locked:
                            textbutton location + " (LOCKED)":
                                action NullAction()
                                text_color "#555"
                                text_size 16
                
                null height 20
                
                ## EMOTIONAL TRACK
                vbox:
                    spacing 12
                    
                    text "💭 EMOTIONAL TRACK" size 20 color "#E94B3C" bold True
                    
                    vbox:
                        spacing 15
                        
                        vbox:
                            spacing 5
                            text "Mask (Social Conformity)" size 14 color "#CCC"
                            hbox:
                                bar value mask range 100 xsize 250 ysize 20
                                text " [mask]%" size 14 color "#FFF"
                        
                        vbox:
                            spacing 5
                            text "Truth (Integrity)" size 14 color "#CCC"
                            hbox:
                                bar value truth range 100 xsize 250 ysize 20
                                text " [truth]%" size 14 color "#FFF"
                        
                        vbox:
                            spacing 5
                            text "Ambition (Drive)" size 14 color "#CCC"
                            hbox:
                                bar value ambition range 100 xsize 250 ysize 20
                                text " [ambition]%" size 14 color "#FFF"
                
                null height 20
                
                ## INSIGHTS
                vbox:
                    spacing 12
                    
                    $ insight_count = len(insights_unlocked)
                    text "💡 INSIGHTS ([insight_count])" size 20 color "#9B59B6" bold True
                    
                    vbox:
                        spacing 8
                        
                        for insight in insights_unlocked[-8:]:  ## Show last 8
                            text "• " + insight size 13 color "#CCC"
                
                null height 20
                
                ## ACTIVE THREADS
                vbox:
                    spacing 12
                    
                    text "🎯 ACTIVE THREADS" size 20 color "#27AE60" bold True
                    
                    vbox:
                        spacing 8
                        
                        for thread in active_threads:
                            text "• " + thread size 14 color "#FFF"
                
                null height 40
                
                textbutton "CLOSE RECORDS":
                    action Hide("records_sidebar")
                    xalign 0.5
                    background "#E94B3C"
                    padding (30, 12)
                    hover_background "#C0392B"
                    text_color "#FFF"
                    text_size 16

## Button to open Records (always visible during gameplay)
screen records_button():
    textbutton "📖 RECORDS":
        xalign 0.05
        yalign 0.05
        action Show("records_sidebar")
        background "#1a1a1a"
        padding (20, 12)
        hover_background "#4A90E2"
        text_color "#FFF"
        text_size 16