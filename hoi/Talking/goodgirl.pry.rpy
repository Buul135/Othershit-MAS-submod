init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_good_girl",
            category=['monika'],
            prompt="You're a good girl",
            pool=True
        )
    )

label monika_good_girl:
    m 1wubsb "[player]..."
    m 1lubst "that was a little random,"
    m 2hubfb "I liked it though, could you say it again?"
    menu:
        "You're a Good girl":
            m 5dubfa "I'm glad you think I'm a good girl, it feel so nice hearing you say that"
            
            if persistent.gender == "M":
                m 5tubfb "Just so you know"
                m 5tubfb "You're a good boy"
            
            elif persistent.gender == "F":
                m 5tubfb "You're a good girl too"

            elif persistent.gender == "X":
                m 5tubfb "You're a good... NB?, sorry I'm not sure what to say"
return

