import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "database" / "job_roles.csv"


def normalize_skill(skill):
    """Normalize skill text to make matching case-insensitive."""
    return " ".join(skill.strip().lower().split())


def load_job_roles():
    """Read job roles, required skills and suggestions from the CSV file."""
    roles = []
    with open(DATABASE_PATH, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            required = [normalize_skill(s) for s in row["required_skills"].split(";") if s.strip()]
            suggestions = [s.strip() for s in row["learning_suggestions"].split(";") if s.strip()]
            roles.append({
                "role": row["job_role"].strip(),
                "required_skills": required,
                "suggestions": suggestions,
                "interests": [x.strip().lower() for x in row.get("career_interest", "").split(";") if x.strip()]
            })
    return roles


def recommend_jobs(student_skills, interests=None):
    """Rank every job role by the percentage of its required skills the student has."""
    student_set = {normalize_skill(s) for s in student_skills if normalize_skill(s)}
    selected_interests = {x.strip().lower() for x in (interests or [])}
    results = []

    for job in load_job_roles():
        required_set = set(job["required_skills"])
        matched = student_set & required_set
        missing = required_set - student_set
        score = (len(matched) / len(required_set) * 100) if required_set else 0.0

        # Interest is a small tie-breaker only; it does not replace skill matching.
        interest_bonus = 2 if selected_interests.intersection(job["interests"]) else 0
        results.append({
            "role": job["role"],
            "match_percentage": round(min(score, 100.0), 2),
            "matched_skills": sorted(matched),
            "missing_skills": sorted(missing),
            "required_skills": sorted(required_set),
            "suggestions": job["suggestions"],
            "_sort_score": score + interest_bonus
        })

    results.sort(key=lambda item: (item["_sort_score"], item["match_percentage"]), reverse=True)
    for item in results:
        item.pop("_sort_score", None)
    return results[:3]
