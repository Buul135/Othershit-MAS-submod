init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_Fvocaloid",
            category=['monika'],
            prompt="Whos your favourite vocaloid?",
            pool=True
        )
    )

label monika_Fvocaloid:
    m 5eud "I've talked about them, and I do find them interrsting, but it's never been my style of music"
    m 4hub "Don't get me wrong, I don't hate them and they are good songs"
    m 5rud "I suppose Hatsune Miku, as shes the only one I really know about"
    m 1fkblb "I'm really glad you want to learn more about me though, it shows me how much you care [player]"
return