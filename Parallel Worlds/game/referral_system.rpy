## FILE: game/referral_system.rpy
## Referral system: 5 friends = 1 chapter unlock

init python:
    import hashlib
    
    def generate_referral_code(email):
        """Generate unique referral code based on email"""
        hash_object = hashlib.md5(email.encode())
        code = hash_object.hexdigest()[:8].upper()
        return code
    
    def add_referral(friend_email):
        """Add referred friend and check if unlock threshold reached"""
        if friend_email not in persistent.referred_friends:
            persistent.referred_friends.append(friend_email)
            
            ## Every 5 referrals = 1 chapter unlock
            if len(persistent.referred_friends) % 5 == 0:
                persistent.referral_unlocks += 1
                persistent.chapters_unlocked += 1
                return True  ## Unlocked new chapter
        return False
    
    def get_referral_progress():
        """Return how many more referrals needed for next unlock"""
        current = len(persistent.referred_friends) % 5
        remaining = 5 - current
        return remaining

## Referral screen (shown in main menu)
screen referral_screen():
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 500
        background "#1a1a1a"
        
        vbox:
            spacing 30
            xalign 0.5
            yalign 0.5
            
            text "REFER FRIENDS, UNLOCK CHAPTERS" size 28 xalign 0.5 color "#FFD700"
            
            null height 20
            
            text "Your Referral Code:" size 20 color "#FFF"
            text "[persistent.referral_code]" size 40 bold True xalign 0.5 color "#4A90E2"
            
            null height 20
            
            text "Friends Referred: [len(persistent.referred_friends)]" size 18 color "#FFF"
            text "Chapters Unlocked via Referrals: [persistent.referral_unlocks]" size 18 color "#FFF"
            
            null height 10
            
            text "Need [get_referral_progress()] more referrals for next unlock!" size 20 color "#F39C12"
            
            null height 30
            
            textbutton "CLOSE":
                action Hide("referral_screen")
                xalign 0.5
                style "button"

style button:
    background "#4A90E2"
    padding (30, 15)
    hover_background "#E94B3C"

style button_text:
    size 20
    color "#FFF"