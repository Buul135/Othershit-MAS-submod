init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_players",
            category=['dev'],
            prompt="players",
            pool=True
        )
    )

label monika_players:
    m "?"
    menu:
        "True":
            $ persistent._mas_pm_likes_spoops = "True"
            "player like spoops"

        "False":
            $ persistent._mas_pm_likes_spoops = "False"
            "player don't like spoops"