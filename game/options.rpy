## FILE: game/options.rpy
## Game configuration and settings

define config.name = _("Parallel Worlds")
define gui.show_name = True
define config.version = "1.0.0"
define gui.about = _("A choice-driven narrative game about identity, connection, and consequences.")

define build.name = "ParallelWorlds"
define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

define config.save_directory = "ParallelWorlds-1.0"

## Screen dimensions
define config.screen_width = 1920
define config.screen_height = 1080

## Narrator voice setting
default persistent.narrator_enabled = True
default persistent.narrator_voice = "male"

## Monetization
default persistent.paid_unlock = False
default persistent.chapters_unlocked = 1
default persistent.last_played_date = None
default persistent.play_streak = 0

## Referral system
default persistent.referral_code = None
default persistent.referred_friends = []
default persistent.referral_unlocks = 0

## Player data
default persistent.player_email = None
default persistent.player_name = None
default persistent.player_gender = None

## Season 2 teaser
default persistent.seen_teaser = False
default persistent.wants_season2_emails = False

## Build configuration
init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    
    build.documentation('*.html')
    build.documentation('*.txt')