## FILE: game/memory_system.rpy
## Characters remember player choices and details

init python:
    def remember(key, value):
        """Store a memory that characters can reference later"""
        memory_bank[key] = value
        choices_made.append({"key": key, "value": value, "act": current_act, "chapter": current_chapter})
        return
    
    def recall(key):
        """Retrieve a stored memory"""
        return memory_bank.get(key, None)
    
    def character_remembers(character, memory_key):
        """Check if character should reference a past memory"""
        memory = recall(memory_key)
        if memory:
            return True
        return False
    
    def get_callback_dialogue(character, context):
        """Generate dialogue that references past choices"""
        
        ## Example callbacks based on Act 1 choices
        if context == "act3_confrontation":
            first_message = recall("first_message_checked")
            
            if character == "jordan":
                if first_message == "authority":
                    return "You always put them first. Even back when this started."
                elif first_message == "casey":
                    return "You checked on Casey first that night. I noticed."
                elif first_message == "unknown":
                    return "You went straight for that threat. Always chasing problems."
                elif first_message == "none":
                    return "You ignored everyone that night. Including me."
        
        return None

## Usage in script:
## $ remember("favorite_food", "pizza")
## 
## Later in Act 3:
## $ callback = get_callback_dialogue("jordan", "act3_confrontation")
## if callback:
##     jordan "[callback]"