"""
01_basic_syntax.py
Author  : andann15
Purpose : Python fundamentals for Machine Learning Engineer
"""

# =========================
# Basic Variables
# =========================

name = "Andan"
role = "Machine Learning Engineer (aspiring)"
age = 21
is_student = True

print(name, role, age, is_student)

# =========================
# Numeric Operations (ML sering pakai ini)
# =========================

x = 10
y = 3

print("Addition:", x + y)
print("Division:", x / y)
print("Power:", x ** y)

# =========================
# List (dataset sederhana)
# =========================

scores = [80, 85, 90, 88, 92]

print("Scores:", scores)
print("First score:", scores[0])
print("Average score:", sum(scores) / len(scores))

# =========================
# Dictionary (struktur data ML-friendly)
# =========================

student = {
    "name": "Andan",
    "major": "Computer Engineering",
    "skills": ["Python", "Linux", "Git"],
    "target_role": "Machine Learning Engineer"
}

print(student)
print("Skills:", student["skills"])

# =========================
# Loop (iterasi data)
# =========================

for skill in student["skills"]:
    print(f"Learning {skill}")

# =========================
# Conditional (logic dasar model & preprocessing)
# =========================

average_score = sum(scores) / len(scores)

if average_score >= 90:
    print("Excellent performance")
elif average_score >= 80:
    print("Good performance")
else:
    print("Needs improvement")

# =========================
# Function (penting untuk ML pipeline)
# =========================

def calculate_mean(data):
    """
    Calculate mean value of a list
    """
    return sum(data) / len(data)


mean_score = calculate_mean(scores)
print("Mean score:", mean_score)

# =========================
# Entry Point (best practice)
# =========================

if __name__ == "__main__":
    print("Python basic syntax for ML completed 🚀")
