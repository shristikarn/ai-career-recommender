from mysql_connector import my_connector

# ================= SKILL GAP =================
def skill_gap(career_name, user_skills):

    conn =my_connector()
    cursor = conn.cursor()

    user_skills = set([skill.strip().lower() for skill in user_skills])

    query = """
    SELECT s.skill_name
    FROM skills s
    JOIN career_skills cs ON s.skill_id = cs.skill_id
    JOIN careers c ON c.career_id = cs.career_id
    WHERE LOWER(c.career_name) = LOWER(%s)
    """

    cursor.execute(query, (career_name,))
    required_skills = set([row[0].strip().lower() for row in cursor.fetchall()])

    conn.close()

    gap = sorted(list(required_skills - user_skills))

    if len(gap) == 0:
        return ["No skill gap .You are job-ready!"]

    return gap


# ================= ROADMAP =================
def get_roadmap(career_name):

    conn = my_connector()
    cursor = conn.cursor()

    query = """
    SELECT r.step_order, r.step_description
    FROM roadmap r
    JOIN careers c ON r.career_id = c.career_id
    WHERE LOWER(c.career_name) = LOWER(%s)
    ORDER BY r.step_order
    """

    cursor.execute(query, (career_name,))
    data = cursor.fetchall()

    conn.close()

    if not data:
        return ["No roadmap available"]

    roadmap = []
    for step_order, step_description in data:
        roadmap.append({
            "step": step_order,
            "description": step_description
        })

    return roadmap


# ================= PERSONALIZED ROADMAP =================
def personalized_roadmap(career_name, user_skills):

    full_roadmap = get_roadmap(career_name)
    gap = skill_gap(career_name, user_skills)

    if isinstance(full_roadmap[0], str):
        return full_roadmap

    personalized = []

    for step in full_roadmap:
        step_text = step["description"].lower()

        if any(skill in step_text for skill in gap):
            personalized.append({**step, "priority": "HIGH"})
        else:
            personalized.append({**step, "priority": "NORMAL"})

    return personalized
def get_projects(career_name):

    conn = my_connector()
    cursor = conn.cursor()

    #  Normalize input
    career_name = career_name.strip()

    # Fetch projects
    query = """
    SELECT p.project_name, p.difficulty
    FROM projects p
    JOIN careers c ON p.career_id = c.career_id
    WHERE LOWER(c.career_name) = LOWER(%s)
    """

    cursor.execute(query, (career_name,))
    data = cursor.fetchall()

    conn.close()

    # Handle no data
    if not data:
        return ["No project suggestions available"]

    #  Format output
    projects = []
    for name, difficulty in data:
        projects.append({
            "project": name,
            "difficulty": difficulty
        })

    return projects