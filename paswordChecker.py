import re

def evaluate_password_strength(pwd):
    # Criteria for password strength
    is_length_valid = len(pwd) >= 8
    has_uppercase = bool(re.search(r'[A-Z]', pwd))
    has_lowercase = bool(re.search(r'[a-z]', pwd))
    has_digit = bool(re.search(r'\d', pwd))
    has_special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd))

    # Assessing the password based on defined criteria
    if all([is_length_valid, has_uppercase, has_lowercase, has_digit, has_special_char]):
        return "Your password is strong! 👍 - Anchal Sharma"
    else:
        feedback = "Your password is weak. Consider the following enhancements:\n"
        if not is_length_valid:
            feedback += "- Increase the length to at least 8 characters\n"
        if not has_uppercase:
            feedback += "- Add at least one uppercase letter\n"
        if not has_lowercase:
            feedback += "- Add at least one lowercase letter\n"
        if not has_digit:
            feedback += "- Include at least one numeric digit\n"
        if not has_special_char:
            feedback += "- Add at least one special character (!@#$%^&*(),.?\":{}|<>)\n"

        return feedback

def run_checker():
    print("Password Strength Evaluator by Anchal Sharma")

    # User input for password
    pwd = input("Please enter your password: ")

    # Evaluate and provide feedback on the password's strength
    result = evaluate_password_strength(pwd)
    print(result)

if __name__ == "__main__":
    run_checker()