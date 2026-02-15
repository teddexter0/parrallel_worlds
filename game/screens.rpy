## FILE: game/screens.rpy
## UI Screens and menus

## Main menu
screen main_menu():
    
    tag menu
    
    ## Background
    add "gui/main_menu.png"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 500
        background "#0a0a0aCC"
        padding (40, 40)
        
        vbox:
            spacing 35
            xalign 0.5
            
            text "PARALLEL WORLDS" size 52 xalign 0.5 color "#FFD700" bold True
            text "Where every choice echoes" size 18 xalign 0.5 color "#CCC" italic True
            
            null height 20
            
            textbutton "NEW GAME":
                action Start()
                xalign 0.5
                xsize 300
                background "#4A90E2"
                padding (20, 15)
                hover_background "#357ABD"
                text_color "#FFF"
                text_size 20
                text_xalign 0.5
            
            textbutton "CONTINUE":
                action ShowMenu("load")
                xalign 0.5
                xsize 300
                background "#27AE60"
                padding (20, 15)
                hover_background "#1E8449"
                text_color "#FFF"
                text_size 20
                text_xalign 0.5
            
            textbutton "REFER FRIENDS":
                action Show("referral_screen")
                xalign 0.5
                xsize 300
                background "#F39C12"
                padding (20, 15)
                hover_background "#D68910"
                text_color "#FFF"
                text_size 20
                text_xalign 0.5
            
            textbutton "SETTINGS":
                action ShowMenu("preferences")
                xalign 0.5
                xsize 300
                background "#9B59B6"
                padding (20, 15)
                hover_background "#7D3C98"
                text_color "#FFF"
                text_size 20
                text_xalign 0.5
            
            textbutton "QUIT":
                action Quit(confirm=True)
                xalign 0.5
                xsize 300
                background "#E74C3C"
                padding (20, 15)
                hover_background "#C0392B"
                text_color "#FFF"
                text_size 20
                text_xalign 0.5

## In-game HUD
screen game_hud():
    
    ## Records button (always visible)
    use records_button
    
    ## Chapter indicator
    frame:
        xalign 0.95
        yalign 0.05
        background "#1a1a1aCC"
        padding (15, 10)
        
        text "Chapter [current_chapter] • Act [current_act]" size 16 color "#FFF"

## General notification system
screen show_notification(message, notification_type="neutral"):
    
    zorder 100
    
    frame:
        xalign 1.0
        yalign 0.15
        xsize 350
        padding (20, 15)
        
        at notification_slide
        
        if notification_type == "good":
            background "#27AE60"
        elif notification_type == "bad":
            background "#E74C3C"
        elif notification_type == "mystery":
            background "#F39C12"
        else:
            background "#7F8C8D"
        
        text message size 16 color "#FFF"
    
    timer 3.5 action Hide("show_notification")

transform notification_slide:
    xoffset 500
    easein 0.4 xoffset 0
    pause 2.7
    easeout 0.4 xoffset 500

## Lightbulb insight popup
screen insight_popup(insight_text):
    
    zorder 100
    modal True
    
    frame:
        xalign 0.5
        yalign 0.3
        xsize 600
        background "#0a0a0aEE"
        padding (40, 30)
        
        vbox:
            spacing 25
            xalign 0.5
            
            text "💡 INSIGHT UNLOCKED" size 28 xalign 0.5 color "#FFD700"
            text insight_text size 18 xalign 0.5 color "#FFF" text_align 0.5
            
            null height 10
            
            textbutton "Saved to Records":
                action Hide("insight_popup")
                xalign 0.5
                background "#4A90E2"
                padding (30, 12)
                hover_background "#357ABD"
                text_color "#FFF"
                text_size 16

## Streak notification
screen streak_notification(days):
    
    zorder 100
    
    frame:
        xalign 0.5
        yalign 0.2
        background "#27AE60"
        padding (40, 25)
        
        vbox:
            spacing 10
            xalign 0.5
            
            text "🔥 [days] DAY STREAK!" size 36 xalign 0.5 color "#FFF" bold True
            text "Keep it going!" size 18 xalign 0.5 color "#FFF"

## Chapter unlock screen
screen chapter_locked():
    
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 550
        background "#0a0a0aF0"
        padding (50, 40)
        
        vbox:
            spacing 35
            xalign 0.5
            
            text "CHAPTER LOCKED" size 36 xalign 0.5 color "#E74C3C" bold True
            
            text "Unlock next chapter by:" size 20 xalign 0.5 color "#FFF"
            
            null height 10
            
            vbox:
                spacing 18
                xalign 0.5
                
                text "⏰ Wait until tomorrow (free)" size 18 color "#27AE60"
                text "💰 Pay $2 to unlock now" size 18 color "#F39C12"
                text "👥 Refer 5 friends (need [get_referral_progress()] more)" size 18 color "#4A90E2"
            
            null height 25
            
            hbox:
                spacing 25
                xalign 0.5
                
                textbutton "WAIT":
                    action Return("wait")
                    background "#27AE60"
                    padding (35, 15)
                    hover_background "#1E8449"
                    text_color "#FFF"
                    text_size 18
                
                textbutton "PAY $2":
                    action Return("pay")
                    background "#F39C12"
                    padding (35, 15)
                    hover_background "#D68910"
                    text_color "#FFF"
                    text_size 18
                
                textbutton "REFER":
                    action [Hide("chapter_locked"), Show("referral_screen")]
                    background "#4A90E2"
                    padding (35, 15)
                    hover_background "#357ABD"
                    text_color "#FFF"
                    text_size 18