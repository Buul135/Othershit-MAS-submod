init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_play_sports",
            category=['monika'],
            prompt="Do you like any sports",
            pool=True
        )
    )

label monika_play_sports:
    m 4eud "Do I like any sports?"
    m 5eud "Well, I've talked about ice-skating"
    m 2rud "But sport was never anything that interested me"
    m 2eud "I only exercised to keep fit"
    m 3hud "Maybe, martial arts"
    m 5eub "Those forms look beautiful"
    m 1eublb "Maybe we can learn together?"
    m 5eublb "I'm sure any sport would be fun with you!"
return