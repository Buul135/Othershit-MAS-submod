init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_proud",
            category=["you"],
            prompt="proud of you",
            random=True
        )
    )

label monika_proud:
    m 1wub "Hey [player] guess what"
    m 1hublb "I'm proud of you"
return