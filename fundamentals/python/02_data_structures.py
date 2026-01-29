"""
02_data_structures.py
Author  : andann15
Purpose : Core Python data structures for Machine Learning
"""

# =========================
# LIST (ordered, mutable)
# =========================
# Biasanya dipakai untuk:
# - dataset kecil
# - batch data
# - feature values

scores = [80, 85, 90, 88, 92]

print("Scores:", scores)
print("First score:", scores[0])

scores.append(95)          # tambah data
scores.remove(85)          # hapus data

print("Updated scores:", scores)

# =========================
# TUPLE (ordered, immutable)
# =========================
# Dipakai untuk:
# - data tetap (shape, coordinate)
# - konfigurasi model

image_shape = (224, 224, 3)
print("Image shape:", image_shape)

# image_shape[0] = 256  ❌ (akan error, immutable)

# =========================
# DICTIONARY (key-value)
# =========================
# Sangat sering dipakai di ML:
# - metadata
# - parameter
# - feature mapping

student = {
    "name": "Andan",
    "major": "Computer Engineering",
    "semester": 6,
    "skills": ["Python", "Linux", "Git"],
}

print("Student name:", student["name"])
print("Skills:", student["skills"])

student["target_role"] = "Machine Learning Engineer"
print("Updated student:", student)

# =========================
# SET (unique values)
# =========================
# Dipakai untuk:
# - menghilangkan duplikasi
# - class labels

labels = ["cat", "dog", "cat", "bird", "dog"]
unique_labels = set(labels)

print("Unique labels:", unique_labels)

# =========================
# DATA STRUCTURES IN ML CONTEXT
# =========================

dataset = [
    {"feature": 1.2, "label": 0},
    {"feature": 2.3, "label": 1},
    {"feature": 0.8, "label": 0},
]

for data in dataset:
    print(f"Feature: {data['feature']} | Label: {data['label']}")

# =========================
# Entry Point
# =========================

if __name__ == "__main__":
    print("Python data structures for ML completed 🚀")
