# SkillMatch AI Pro
# AI Recommendation Logic Project

career_database = {
    "AI Engineer": {
        "skills": ["python", "machine learning", "data analysis", "statistics"]
    },
    "Web Developer": {
        "skills": ["html", "css", "javascript", "python"]
    },
    "Data Analyst": {
        "skills": ["python", "sql", "excel", "statistics"]
    },
    "Cyber Security Analyst": {
        "skills": ["networking", "linux", "python", "security"]
    },
    "UI/UX Designer": {
        "skills": ["figma", "creativity", "wireframing", "prototyping"]
    }
}

print("=" * 50)
print("🚀 Welcome to SkillMatch AI Pro")
print("=" * 50)

user_input = input(
    "\nEnter your skills separated by commas:\n"
)

user_skills = [skill.strip().lower()
               for skill in user_input.split(",")]

recommendations = []

for career, details in career_database.items():

    career_skills = details["skills"]

    matched = len(
        set(user_skills).intersection(set(career_skills))
    )

    similarity_score = (
        matched / len(career_skills)
    ) * 100

    recommendations.append(
        (career, similarity_score, career_skills)
    )

recommendations.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\n🎯 Top Career Recommendations")
print("-" * 50)

for career, score, skills in recommendations[:3]:

    missing_skills = [
        skill for skill in skills
        if skill not in user_skills
    ]

    print(f"\n💼 Career: {career}")
    print(f"📊 Match Score: {score:.0f}%")

    if missing_skills:
        print("📚 Skills To Learn:")
        print(", ".join(missing_skills))
    else:
        print("✅ Perfect Match!")

print("\n🔥 Personalized Learning Roadmap")

top_career = recommendations[0]

roadmap = [
    skill for skill in top_career[2]
    if skill not in user_skills
]

for step, skill in enumerate(roadmap, start=1):
    print(f"Step {step}: Learn {skill}")

print("\nThank you for using SkillMatch AI Pro!")