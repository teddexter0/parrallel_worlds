testcase chapter_one_controls:
    pause until screen "main_menu"
    run Start("act1_opening")
    advance until screen "choice"
    assert "Open Casey's text"
    click "Pause"
    assert screen "pause_menu"
    click "Save game"
    assert screen "save"
    run FileSave("pw-qa", slot=True, confirm=False)
    assert eval (renpy.can_load("pw-qa"))
    click "Back"
    click "Settings"
    assert screen "preferences"
    assert "Music volume"
    click "Back"
    click "Resume"
    assert screen "choice"
    run SetVariable("jordan_no_contact", True)
    click "Records"
    assert screen "records_sidebar"
    assert "Jordan (No contact)"
    click "Close"
    assert screen "choice"
    click "Open Casey's text"
    advance until screen "insight_popup"
    assert eval (recall("first_message_checked") == "casey")
    click "Continue"
    assert not screen "insight_popup"

testcase ending_records:
    run Jump("act4_game_end")
    pause until screen "ending_summary"
    click "View Records"
    assert screen "records_sidebar"
    click "Close"
    assert screen "ending_summary"

testcase authored_endings:
    parameter (route, honesty, reserve, morgan_score, bonding, outcome) = [
        ("chose_truth", 75, 32, 50, 50, "open_record"),
        ("chose_truth", 65, 32, 66, 75, "bridge"),
        ("convinced_morgan", 75, 32, 80, 50, "second_witness"),
        ("chose_silence", 72, 61, 50, 50, "silent_witness"),
        ("chose_silence", 40, 61, 50, 50, "protected_self"),
        ("chose_deal", 75, 32, 80, 75, "brokered_truth"),
    ]
    $ remember("act2_betrayal", route)
    $ store.truth, store.mask, store.ambition = honesty, reserve, 50
    $ store.jordan_relationship = store.casey_relationship = store.riley_relationship = bonding
    $ store.morgan_relationship = morgan_score
    assert eval (resolve_story_ending() == outcome)
