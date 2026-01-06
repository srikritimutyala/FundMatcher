def compatibility_score(founder, investor):
    score = 0

    if any(i in investor.get("preferred_industries", [])
           for i in founder.get("industry", [])):
        score += 30

    if founder.get("stage") in investor.get("preferred_stage", []):
        score += 20

    if founder.get("funding_needed", 0) <= investor.get("investment_range", [0, 0])[1]:
        score += 20

    if any(v in investor.get("values", [])
           for v in founder.get("values", [])):
        score += 30


    if founder.get("first_time_founder"):
        score += 10

    if founder.get("university_affiliation"):
        score += 10

    return score


#parameters are up for discussion and can be changed based on feedback