init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="mas_compliment_language",
            prompt="Human language doesn't have a word for how much I love you",
            unlocked=True
        ),
        code="CMP"
    )

label mas_compliment_language:
    m 1wubsd "...that's.. I"
    m 1dubsb ".. wow [player]"
    m 5fubsb "You've made my heart skip a beat"
    m 5fkbfb "maybe one day lanague will catch up to us, but till then I love you will have to do"
return "love"