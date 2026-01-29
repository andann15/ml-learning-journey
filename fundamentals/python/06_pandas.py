# 06_pandas.py
# Manipulasi data real (CSV, tabel)

import pandas as pd

# DataFrame manual
data = {
    "umur": [20, 21, 22, 23],
    "nilai": [80, 85, 90, 88]
}

df = pd.DataFrame(data)

print("Data:")
print(df)

print("\nRata-rata nilai:", df["nilai"].mean())

# Filtering
print("\nMahasiswa nilai >= 85:")
print(df[df["nilai"] >= 85])
