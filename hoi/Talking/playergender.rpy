init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_BG",
            category=["you"],
            prompt="I'm questioning my gender",
            pool=True
        )
    )

label monika_BG:
    m 1fsbsb "..[mas_get_player_nickname()], I know this is a very personal subject"
    m 1hsbsb "I'm so glad you trust me enought to tell me"
    m 5fsbsb "just know I'll always surport you with whatever you're going thought"
    m 5fsbsb "I love you, no matter what gender you project yourself as, or lack of gender"
return "love"