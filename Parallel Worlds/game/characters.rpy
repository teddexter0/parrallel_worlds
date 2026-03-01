## FILE: game/characters.rpy
## Character definitions with dynamic gender assignment

## Define characters with dynamic pronouns
define narrator = Character(None, kind=nvl)
define parent = DynamicCharacter("parent_name",
    image="parent",
    who_color="#8B4513")

default parent_name = "Parent"
default parent_pronoun_subject = "they"
default parent_pronoun_object = "them"
default parent_pronoun_possessive = "their"
define jordan = DynamicCharacter("jordan_name", 
    image="jordan",
    who_color="#4A90E2")

define casey = DynamicCharacter("casey_name",
    image="casey",
    who_color="#E94B3C")

define morgan = DynamicCharacter("morgan_name",
    image="morgan",
    who_color="#F39C12")

define riley = DynamicCharacter("riley_name",
    image="riley",
    who_color="#9B59B6")

define anchor = DynamicCharacter("anchor_name",
    image="anchor",
    who_color="#27AE60")

## Character names (displayed in dialogue)
default jordan_name = "Jordan"
default casey_name = "Casey"
default morgan_name = "Morgan"
default riley_name = "Riley"
default anchor_name = "The Anchor"

## Player character
define player = DynamicCharacter("[persistent.player_name]",
    who_color="#FFFFFF")

## Assign genders based on player choice
label assign_character_genders:
    
    if persistent.player_gender == "male":
        ## Player is MALE
        $ jordan_gender = "male"
        $ jordan_pronoun_subject = "he"
        $ jordan_pronoun_object = "him"
        $ jordan_pronoun_possessive = "his"
        
        $ casey_gender = "female"
        $ casey_pronoun_subject = "she"
        $ casey_pronoun_object = "her"
        $ casey_pronoun_possessive = "her"
        
        $ morgan_gender = "male"
        $ morgan_pronoun_subject = "he"
        $ morgan_pronoun_object = "him"
        $ morgan_pronoun_possessive = "his"
        
        $ riley_gender = "female"
        $ riley_pronoun_subject = "she"
        $ riley_pronoun_object = "her"
        $ riley_pronoun_possessive = "her"
        
        $ anchor_gender = "male"
        $ anchor_pronoun_subject = "he"
        $ anchor_pronoun_object = "him"
        $ anchor_pronoun_possessive = "his"
        
    elif persistent.player_gender == "female":
        ## Player is FEMALE
        $ jordan_gender = "male"
        $ jordan_pronoun_subject = "he"
        $ jordan_pronoun_object = "him"
        $ jordan_pronoun_possessive = "his"
        
        $ casey_gender = "male"
        $ casey_pronoun_subject = "he"
        $ casey_pronoun_object = "him"
        $ casey_pronoun_possessive = "his"
        
        $ morgan_gender = "female"
        $ morgan_pronoun_subject = "she"
        $ morgan_pronoun_object = "her"
        $ morgan_pronoun_possessive = "her"
        
        $ riley_gender = "male"
        $ riley_pronoun_subject = "he"
        $ riley_pronoun_object = "him"
        $ riley_pronoun_possessive = "his"
        
        $ anchor_gender = "female"
        $ anchor_pronoun_subject = "she"
        $ anchor_pronoun_object = "her"
        $ anchor_pronoun_possessive = "her"
    
    return

## Character image definitions (sprites will be loaded based on gender)
init python:
    def get_character_sprite(character_name, expression, gender):
        """Return correct sprite path based on character gender"""
        if character_name == "jordan":
            # Jordan always uses the single jordan folder
            return f"images/characters/jordan/{expression}.png"
        elif character_name == "casey":
            # Casey adapts
            if gender == "male":
                return f"images/characters/casey_male/{expression}.png"
            else:
                return f"images/characters/casey_female/{expression}.png"
        elif character_name == "morgan":
            if gender == "male":
                return f"images/characters/morgan_male/{expression}.png"
            else:
                return f"images/characters/morgan_female/{expression}.png"
        elif character_name == "riley":
            if gender == "male":
                return f"images/characters/riley_male/{expression}.png"
            else:
                return f"images/characters/riley_female/{expression}.png"
        elif character_name == "anchor":
            if gender == "male":
                return f"images/characters/anchor_male/{expression}.png"
            else:
                return f"images/characters/anchor_female/{expression}.png"