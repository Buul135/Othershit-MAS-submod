init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_boyfriend",
            category=['monika'],
            prompt="How come you've never called me your [boy]friend",
            pool=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        )
    )

label monika_boyfriend:
    m 1ekd "Have I not?, I apologize if that's upset you"
    m 5eublb "well, you're the best [boy]friend I could wish for, I love you [mas_get_player_nickname()]"
return "love"