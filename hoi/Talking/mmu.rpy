init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_pmu",
            category=['us'],
            prompt="Would you do my makeup?",
            pool=True
        )
    )

label monika_pmu:
if persistent.gender == "M":
    m 1wst "I didn't expect you to say ask that!"
    m 1wsblb ".. If you want me too, I'd love too,"
    m 5ltblb "I wonder what type of lipstick would suit you most"

else:
    m 3eubsb "of course [mas_get_player_nickname()]"
    m 5eubsb "I'd never thought about doing that"
    m 1hubsb "But it sounds so fun"

return