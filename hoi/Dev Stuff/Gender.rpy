init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_fucl",
            category=['dev'],
            prompt="gender",
            pool=True
        )
    )

label monika_fucl:
    m "?"
    menu:
        "male":
            $ persistent.gender = "M"
            "player male"
        "female":
            $ persistent.gender = "F"
            "player female"
        "non":
            $ persistent.gender = "X"
            "player NB"
return