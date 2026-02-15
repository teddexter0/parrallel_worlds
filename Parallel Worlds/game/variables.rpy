## FILE: game/variables.rpy
## Core game variables and stats

## STATS (0-100)
default mask = 50      # Social conformity
default truth = 50     # Honesty/integrity
default ambition = 50  # Career/goal focus

## RELATIONSHIPS (0-100)
default jordan_relationship = 50
default casey_relationship = 50
default morgan_relationship = 50
default riley_relationship = 50
default anchor_relationship = 0  # Unlocked in Act 2

## NO CONTACT STATUS
default jordan_no_contact = False
default casey_no_contact = False
default morgan_no_contact = False
default riley_no_contact = False

## CHARACTER GENDERS (dynamically assigned based on player choice)
default jordan_gender = "male"
default casey_gender = "female"
default morgan_gender = "male"
default riley_gender = "female"
default anchor_gender = "male"

## PRONOUNS (dynamically set)
default jordan_pronoun_subject = "he"
default jordan_pronoun_object = "him"
default jordan_pronoun_possessive = "his"

default casey_pronoun_subject = "she"
default casey_pronoun_object = "her"
default casey_pronoun_possessive = "her"

default morgan_pronoun_subject = "he"
default morgan_pronoun_object = "him"
default morgan_pronoun_possessive = "his"

default riley_pronoun_subject = "she"
default riley_pronoun_object = "her"
default riley_pronoun_possessive = "her"

default anchor_pronoun_subject = "he"
default anchor_pronoun_object = "him"
default anchor_pronoun_possessive = "his"

## ROMANTIC PURSUIT TRACKING
default pursuing_jordan = False
default pursuing_casey = False
default pursuing_morgan = False

## MEMORY SYSTEM (Characters remember)
default memory_bank = {
    "favorite_food": None,
    "biggest_fear": None,
    "first_lie_told": None,
    "jordan_birthday_attended": False,
    "casey_secret_shared": False,
    "morgan_coffee_order": None,
    "riley_dream_mentioned": None,
    "act1_major_choice": None,
    "act2_betrayal": None,
    "parent_confrontation_outcome": None,
    "first_message_checked": None,
    "unknown_caller_response": None
}

## INSIGHTS UNLOCKED (for Records sidebar)
default insights_unlocked = []

## LOCATIONS VISITED
default locations_visited = ["Your Room"]
default locations_locked = ["The Rooftop", "Casey's Place", "Morgan's Studio", "The Underground Spot"]

## ACTIVE QUESTS/THREADS
default active_threads = [
    "The Threatening Message",
    "Unknown Caller Identity"
]

## CURRENT CHAPTER
default current_chapter = 1
default current_act = 1

## CHOICE TRACKING (for memory callbacks)
default choices_made = []