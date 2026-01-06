from db import users

users.insert_many([
    {
        "user_type": "founder",
        "name": "Student AI Founder",
        "industry": ["AI"],
        "stage": "idea",
        "funding_needed": 20000,
        "values": ["diversity", "education"],
        "first_time_founder": True,
        "university_affiliation": "UIUC"
    },
    {
        "user_type": "investor",
        "name": "Impact Angel",
        "preferred_industries": ["AI", "EdTech"],
        "preferred_stage": ["idea"],
        "investment_range": [10000, 50000],
        "values": ["diversity"]
    }
])
