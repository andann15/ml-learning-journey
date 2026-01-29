# 04_functions.py
# Membuat fungsi agar kode rapi & reusable

def train_model(epoch):
    print(f"Training epoch {epoch}")

def evaluate_model(accuracy):
    if accuracy >= 0.9:
        return "Model bagus"
    else:
        return "Model perlu tuning"

# Pemanggilan fungsi
for i in range(1, 4):
    train_model(i)

result = evaluate_model(0.92)
print(result)
