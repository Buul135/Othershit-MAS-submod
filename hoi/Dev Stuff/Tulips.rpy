
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_LB",
            category=['monika'],
            prompt="LB",
            pool=True
        )
    )

$ _history_list.pop()
label monika_LB:
    "?"
    menu:
         "Known":
            $ persistent.PKMLB = "True"
            m "a"
         "Not Known":
            $ persistent.PKMLB = "False"
            m "a"
return