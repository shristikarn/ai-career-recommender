from recommder import recommend_career
from analysis import skill_gap, get_roadmap, get_projects, personalized_roadmap

# 🔹 User Input
user_skills = input("Enter skills (comma separated): ").split(",")
user_interest = input("Enter interest: ")
level = input("Enter level (beginner/intermediate/advanced): ")

# 🔹 Recommendation
recommended = recommend_career(user_skills, user_interest, level)

if not recommended:
    print("No career recommendations found.")
    exit()

top_career = recommended[0][0]

print("\n==============================")
print(" BEST CAREER:", top_career)
print("==============================")

# 🔹 Skill Gap
print("\n SKILL GAP:")
gap = skill_gap(top_career, user_skills)

if isinstance(gap[0], str):
    print(gap[0])
else:
    for skill in gap:
        print(f" - {skill}")

# Roadmap
print("\n ROADMAP:")

roadmap = get_roadmap(top_career)

if isinstance(roadmap[0], str):
    print(roadmap[0])
else:
    for step in roadmap:
        print(f"Step {step['step']}: {step['description']}")

#  Personalized Roadmap (ADVANCED)
print("\n PERSONALIZED ROADMAP:")

p_roadmap = personalized_roadmap(top_career, user_skills)

if isinstance(p_roadmap[0], str):
    print(p_roadmap[0])
else:
    for step in p_roadmap:
        print(f"Step {step['step']}: {step['description']} [{step['priority']}]")

#  Projects
print("\n PROJECT SUGGESTIONS:")

projects = get_projects(top_career)

if isinstance(projects[0], str):
    print(projects[0])
else:
    for p in projects:
        print(f" - {p['project']} ({p['difficulty']})")

print("\n==============================")
print("Career Analysis Complete")
print("==============================")