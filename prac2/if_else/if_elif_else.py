
score = int(input("Score : "))

if score < 0 or score > 100:
    result = "Invalid score"
elif score >= 90:
    result = "Excellent"
elif score >= 70:
    result = "Good"
elif score >= 50:
    result = "Satisfactory"
else:
    result = "Fail"

print("Result:", result)