init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Blumen",
            category=['monika'],
            prompt="Whats your favourite flower?",
            pool=True
        )
    )

$ _history_list.pop()
label monika_Blumen:
    m "Hmm, let me think"
    m "... Tulips"
    m "They came in some many differnt colours, whenever I see I field of Tulips I just melt"
    m "althought, i've never seen a field of Tulips in real life before"
    menu:
         "I'll take you to one":
            $ persistent.PKMLB = "True"
            m "Really!, that would be wonderful!"
         "That's a shame":
            $ persistent.PKMLB = "True"
            m "Well, I see one someday"
return
