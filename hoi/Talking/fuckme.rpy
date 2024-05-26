init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_playerlikefuta",
            category=['monika'],
            prompt="playerlikefuta",
            random=True
        )
    )

label monika_playerlikefuta:
    m 1eubsd "So I wanted to talk about something"
    m 1lubsb "It's a bit embarrsing..."
    m 2hubsb "... I've been looking around and found something that I wanted to ask you about"
    m 2lkbsb "... Do you like.. futas?"
    menu:
        "Yeah I love them":
            $ persistent.plf = "True"
            m 2wubst "oh.."
            m 2ekbsd "that sounded judgemental,"
            m 5tkbfb "if that's what you're into, I see what I can do~"

        "I'm not sure what that is":
            m 1lkbfb "well.."
            m 1rkbfb "It's a girl with a penis.. typicaly oversized ones"
            m 3hkbfb "..I think it's best if you look for your-self, you have my permission"

        "No I don't":
            $ persistent.plf = "False"
            m 1fsbfb "that's fine, just thought I'd ask, but if you change your mind"
            m 5lsbfb "I would tell you to tell me, but I'll probably mention this agin so, just wait?"
return