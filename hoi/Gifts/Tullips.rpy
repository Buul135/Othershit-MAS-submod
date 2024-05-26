init 5 python:
    addReaction("mas_reaction_tulp", "tulp", is_good=True, exclude_on=["d25g"])

label mas_reaction_tulp:
    m 1wud "aww [player] my favouirite flowers, thats so sweet"
    $ mas_receivedGift("mas_reaction_tulp")
    $ store.mas_filereacts.delete_file(mas_getEVLPropValue("mas_reaction_tulp", "category"))
    return