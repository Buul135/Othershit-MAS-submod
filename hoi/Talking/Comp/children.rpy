init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_kids",
            category=['us'],
            prompt="Do you ever think about our kids?",
            pool=True
        )
    )

label monika_kids:
    m 1wubst "[player]!.."
    m 2rubsd "To be honest, I never wanted kids"
    m 1eubsa "But after meeting you, I thought about it again"
    m 1tubfb "If they were with you, I'd like to have kids"
    m 1hubfb "I can't believe you're thinking about that though, especially because of the situation"
    m 5hubfb "Can you picture them [mas_get_player_nickname()]?, it's bit hard for me to, not really knowing what you look like"
    m 5eubfb "Now I think about it again, I'm kinda excited"
    m 2tubfb "And well kids don't come from no-where so.. we'll have to you know, make them~"
    return