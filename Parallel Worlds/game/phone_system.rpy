## FILE: game/phone_system.rpy
## Phone messaging system with timestamps and images

## Phone screen
screen phone_screen(character_name, messages_list):
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 450
        ysize 800
        background "#000"
        padding (20, 20)
        
        vbox:
            spacing 15
            
            ## Header
            hbox:
                spacing 20
                yalign 0.0
                
                textbutton "◀":
                    action Return()
                    text_size 24
                    text_color "#007AFF"
                
                text "[character_name]" size 22 color "#FFF"
            
            null height 30
            
            ## Message thread
            viewport:
                scrollbars "vertical"
                ysize 600
                
                vbox:
                    spacing 20
                    
                    for msg in messages_list:
                        if msg["sender"] == "them":
                            hbox:
                                xalign 0.0
                                frame:
                                    background "#2C2C2E"
                                    padding (15, 12)
                                    xmaximum 350
                                    vbox:
                                        spacing 5
                                        text msg["content"] size 16 color "#FFF"
                                        text msg["time"] size 12 color "#8E8E93"
                        
                        elif msg["sender"] == "you":
                            hbox:
                                xalign 1.0
                                frame:
                                    background "#007AFF"
                                    padding (15, 12)
                                    xmaximum 350
                                    vbox:
                                        spacing 5
                                        text msg["content"] size 16 color "#FFF"
                                        text msg["time"] size 12 color "#B3D7FF"
                        
                        elif msg["sender"] == "image":
                            python:
                                image_align = 0.0 if msg.get("from") == "them" else 1.0
                                image_bg = "#2C2C2E" if msg.get("from") == "them" else "#007AFF"
                            
                            hbox:
                                xalign image_align
                                frame:
                                    padding (8, 8)
                                    background image_bg
                                    add msg["image_path"] xsize 300
            
            null height 20
            
            ## Response options (if provided)
            if messages_list[-1].get("prompt_reply", False):
                textbutton "Reply":
                    action Return("reply")
                    xalign 0.5
                    background "#007AFF"
                    padding (40, 15)
                    text_color "#FFF"
                    text_size 18

## Function to show phone conversation
label show_phone_conversation(character_name, messages):
    call screen phone_screen(character_name, messages)
    return

## Notification popup (appears during gameplay)
screen notification_popup(sender, message_preview):
    
    zorder 100
    
    frame:
        xalign 0.5
        yalign 0.1
        xsize 400
        background "#2C2C2E"
        padding (20, 15)
        
        at phone_notification_slide

        vbox:
            spacing 8

            text "[sender]" size 18 bold True color "#FFF"
            text "[message_preview]" size 14 color "#8E8E93"

    timer 4.0 action Hide("notification_popup")

transform phone_notification_slide:
    yoffset -100
    alpha 0.0
    easein 0.3 yoffset 0 alpha 1.0
    pause 3.4
    easeout 0.3 yoffset -100 alpha 0.0