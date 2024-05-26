init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_food",
            category=['monika'],
            prompt="Whats you're favorite food?",
            pool=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        )
    )

label monika_food:
    m 2tsbsa "... you [player]"
    m 5hsbsb "ahaha, just messing with you"
    m 1rsd "to be honest, I don't have one"
    m 3ttb "I know that's not a useful answer, but that's a side effect of my memory"
    m 5fsb ".. I know, my favourite food is anything you make"
    m 5dkbsb "your love would make it the sweetest meal"
return