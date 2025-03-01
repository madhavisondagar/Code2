import random
import string

def generate_password(length=12, complexity=3):
    """
    Generate a random password based on specified length and complexity.
    :param length: Length of the password.
    :param complexity: Complexity level (1 - low, 3 - high)
    :return: A random password string.
    """
    
    # Define the character sets based on complexity
    lower_case = string.ascii_lowercase  # a-z
    upper_case = string.ascii_uppercase  # A-Z
    digits = string.digits  # 0-9
    special_chars = string.punctuation  # Special characters like !, @, #, etc.

    # AI-based logic for complexity (e.g., how many types of characters to include)
    if complexity == 1:
        # Low complexity: Only lowercase letters
        char_pool = lower_case
    elif complexity == 2:
        # Medium complexity: Lowercase + Uppercase + Digits
        char_pool = lower_case + upper_case + digits
    elif complexity == 3:
        # High complexity: Lowercase + Uppercase + Digits + Special characters
        char_pool = lower_case + upper_case + digits + special_chars
    else:
        raise ValueError("Complexity must be between 1 and 3.")
    
    # Generate password using random.choice() from the chosen character pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

# Example usage:
print("Password Generator")
length = int(input("Enter password length: "))
complexity = int(input("Enter password complexity (1 - low, 3 - high): "))

password = generate_password(length, complexity)
print(f"Generated Password: {password}")
