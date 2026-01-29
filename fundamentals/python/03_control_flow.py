# 03_control_flow.py
# Mengatur alur logika program

# IF - ELSE
accuracy = 0.87

if accuracy >= 0.9:
    print("Model siap digunakan")
else:
    print("Model perlu ditingkatkan")

# FOR LOOP
print("\nTraining model:")
for epoch in range(1, 6):
    print(f"Epoch {epoch} selesai")

# WHILE LOOP
loss = 1.0
print("\nOptimasi loss:")
while loss > 0.1:
    loss *= 0.7
    print(f"Loss sekarang: {loss:.4f}")

# BREAK & CONTINUE
print("\nEarly stopping:")
for epoch in range(1, 10):
    if epoch == 5:
        print("Training dihentikan (early stopping)")
        break
    print(f"Epoch {epoch}")
