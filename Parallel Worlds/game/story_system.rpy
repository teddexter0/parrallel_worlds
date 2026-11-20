## Story outcome resolver and end-of-season recap.
## Keeps branching rules in one place so narrative scripts stay readable.

default ending_id = "open_record"
default ending_title = "The Open Record"
default ending_summary = "You put your name beside the truth and helped make the record impossible to erase."
default ending_path_label = "Unresolved"
default dominant_trait = "Balanced"

init python:
    import store

    ENDING_TITLES = {
        "open_record": "The Open Record",
        "bridge": "The Bridge",
        "second_witness": "The Second Witness",
        "silent_witness": "The Silent Witness",
        "protected_self": "The Protected Self",
        "brokered_truth": "The Brokered Truth",
    }

    ENDING_SUMMARIES = {
        "open_record": "You put your name beside the truth and helped make the record impossible to erase.",
        "bridge": "You left with people still willing to cross the distance toward you.",
        "second_witness": "You turned one frightened witness into two, and neither of you had to stand alone.",
        "silent_witness": "You stayed silent in the room, then chose to live honestly with the cost.",
        "protected_self": "You kept yourself safe, but safety became a room with no one else inside it.",
        "brokered_truth": "You forced the institution to pay a price for your truth before it could use it.",
    }

    PATH_LABELS = {
        "chose_truth": "Testified",
        "convinced_morgan": "Morgan testified with you",
        "tried_morgan_failed": "Testified after Morgan refused",
        "chose_silence": "Stayed silent",
        "chose_deal": "Negotiated protections",
    }

    def clamp_story_state():
        """Keep every visible score within its documented 0-100 range."""
        fields = (
            "mask", "truth", "ambition", "jordan_relationship",
            "casey_relationship", "morgan_relationship",
            "riley_relationship", "anchor_relationship",
        )
        for field in fields:
            value = getattr(store, field, 0)
            setattr(store, field, max(0, min(100, value)))

    def story_dominant_trait():
        scores = {
            "Truth": store.truth,
            "Mask": store.mask,
            "Ambition": store.ambition,
        }
        highest = max(scores.values())
        leaders = [name for name, value in scores.items() if value == highest]
        return leaders[0] if len(leaders) == 1 else "Balanced"

    def relationship_average():
        values = (
            store.jordan_relationship,
            store.casey_relationship,
            store.morgan_relationship,
            store.riley_relationship,
        )
        return sum(values) / float(len(values))

    def resolve_story_ending():
        """Resolve one of six authored outcomes from the major choice and accumulated state."""
        path = recall("act2_betrayal")

        if path == "chose_silence":
            return "silent_witness" if store.truth >= store.mask else "protected_self"
        if path == "chose_deal":
            return "brokered_truth"
        if path in ("convinced_morgan", "tried_morgan_failed") and store.morgan_relationship >= 60:
            return "second_witness"
        if relationship_average() >= 65:
            return "bridge"
        if store.truth >= store.mask and store.truth >= store.ambition:
            return "open_record"
        # Every remaining state still resolves to an authored ending. A guarded
        # player gets the relationship-led route; a more candid one goes public.
        return "bridge" if store.mask > store.truth else "open_record"

    def finalize_story_ending():
        clamp_story_state()
        store.ending_id = resolve_story_ending()
        store.ending_title = ENDING_TITLES[store.ending_id]
        store.ending_summary = ENDING_SUMMARIES[store.ending_id]
        path = recall("act2_betrayal")
        store.ending_path_label = PATH_LABELS.get(path, "Testified")
        store.dominant_trait = story_dominant_trait()

        if persistent.endings_unlocked is None:
            persistent.endings_unlocked = []
        if store.ending_id not in persistent.endings_unlocked:
            persistent.endings_unlocked.append(store.ending_id)
        renpy.save_persistent()
