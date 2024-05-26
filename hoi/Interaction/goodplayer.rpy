init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_player_goodgbp",
            category=['monika'],
            prompt="Can you call me a good [boy]",
            pool=True
        )
    )

label monika_player_goodgbp:
    m 1wubsb "Of course"
    m 5fubsb "You're a good [boy] [player]"
return
