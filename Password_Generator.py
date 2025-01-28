import random
import string

#Function to get user input for password criteria
def get_user_input():
    min_uppercase = int(input("Enter minimum number of uppercase letters: "))
    min_lowercase = int(input("Enter minimum number of lowercase letters: "))
    min_numbers = int(input("Enter minimum number of numbers: "))
    min_special = int(input("Enter minimum number of special characters: "))
    
    min_length = int(input("Enter the minimum length of the password (min 6): "))
    max_length = int(input("Enter the maximum length of the password (max 50): "))

    if min_length < 6 :
        print("Invalid input. Minimum length must be at least 6 or more than more than 6. ")
    if max_length > 50 :
        print("Invalid input. Maximum Length must be 50 or Less Than 50. ")
    elif min_length >= max_length :
        print("Invalid Input. Maximum Length must be more than Minimum Length. ")
        return get_user_input()
    return min_length, max_length, min_uppercase, min_lowercase, min_numbers, min_special
 
# Function to generate a password based on user input
def generate_password(min_length, max_length, min_uppercase, min_lowercase, min_numbers, min_special):
    if min_length < min_uppercase + min_lowercase + min_numbers + min_special:
        print("The sum of minimum required characters exceeds the minimum password length.")
        return
    
    #Randomly selecting the length of the password within the range 
    length = random.randint(min_length, max_length)

    password = []
    password += random.choices(string.ascii_uppercase, k=min_uppercase)
    password += random.choices(string.ascii_lowercase, k=min_lowercase)
    password += random.choices(string.digits, k=min_numbers)
    password += random.choices(string.punctuation, k=min_special)

   
    remaining_length = length - len(password)  #Calculate the remaining length needed
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password += random.choices(all_characters, k=remaining_length)

    random.shuffle(password)
    return ''.join(password)

#Function to calculate the strength of the generated password
def calculate_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    strength = 0
    if length >= 12:
        strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_number:
        strength += 1
    if has_special:
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    elif strength >= 4:
        return "Strong"

def main():
    min_length, max_length, min_uppercase, min_lowercase, min_numbers, min_special = get_user_input()
    password = generate_password(min_length, max_length, min_uppercase, min_lowercase, min_numbers, min_special)
    if password:
        print("Generated Password:", password)
        print("Password Strength:", calculate_strength(password))

if __name__ == "__main__":
    main()
 