init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_hand_kiss",
            category=['interact'],
            prompt="Kiss Monika's hand",
            pool=True,
            unlocked=True
        )
    )

label monika_hand_kiss:
    m 2wubst "..."
    m 5fubfb "that was quite romantic [player]"
    m 1nubfb "maybe next time it can be on the lips?"
return