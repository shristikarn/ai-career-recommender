from mysql_connector import my_connector
def recommend_career(user_skills, user_interest, level):
    conn=my_connector()
    cursor=conn.cursor()
    # Normalize user skills
    user_skills = [skill.strip().lower() for skill in user_skills]

    # Fetch data with importance
    cursor.execute("""
        SELECT c.career_name, s.skill_name, cs.importance_level
        FROM careers c
        JOIN career_skills cs ON c.career_id = cs.career_id
        JOIN skills s ON cs.skill_id = s.skill_id
    """)

    data = cursor.fetchall()

    career_scores = {}

    #Step 1: Skill Matching (Weighted)
    for career_name, skill, importance in data:

        if career_name not in career_scores:
            career_scores[career_name] = 0

        if skill.lower() in user_skills:
            career_scores[career_name] += importance   # weighted score

    # Step 2: Interest Boost
    interest_map = {
        "ai": ["Machine Learning Engineer", "AI Engineer", "Data Scientist"],
        "security": ["Cybersecurity Analyst", "Ethical Hacker"],
        "development": ["Backend Developer", "Frontend Developer", "Full Stack Developer"],
        "cloud": ["Cloud Engineer", "DevOps Engineer"],
        "data": ["Data Scientist", "Data Analyst"]
    }

    user_interest = user_interest.lower()

    for key, careers in interest_map.items():
        if key in user_interest:
            for c in careers:
                if c in career_scores:
                    career_scores[c] += 10  # boost

    # Step 3: Level Filtering
    if level == "beginner":
        remove = ["AI Researcher", "Machine Learning Engineer", "Blockchain Developer"]
    elif level == "intermediate":
        remove = ["AI Researcher"]
    else:
        remove = []

    for r in remove:
        career_scores.pop(r, None)

    #Step 4: Sort Careers
    sorted_careers = sorted(
        career_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    #  Step 5: Return Top 3
    return sorted_careers[:3]
