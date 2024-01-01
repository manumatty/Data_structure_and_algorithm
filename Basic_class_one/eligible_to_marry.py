#Based on age return eligible for marrage or not using condtional statements
def can_marry(bride_age,groom_age):
    if bride_age >= 18 and groom_age >=21:
        return "They can Marry"
    else:
        return "They cannot Marry"
