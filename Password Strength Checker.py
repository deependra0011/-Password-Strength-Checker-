import re

def check_password_strength(password):
    score = 0
    
    # Conditions
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[@$!%*?&]", password):
        score += 1

    # Result based on score
    if score == 5:
        return "Very Strong 💪"
    elif score == 4:
        return "Strong 🙂"
    elif score == 3:
        return "Moderate 😐"
    else:
        return "Weak ⚠️"


# Main Program
print("=== Password Strength Checker ===")
user_password = input("Enter a password to check: ")
result = check_password_strength(user_password)
print("\nPassword Strength:", result)
