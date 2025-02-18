# Password_Generator_With_Strength_Calculator
This Python-based Password Generator is a simple yet effective tool to create secure passwords tailored to user-defined criteria. Whether you're securing personal accounts or managing professional credentials, this tool ensures your passwords are both strong and customizable.

# Prerequisites
* Python
  
# Features
* Customizable Password Criteria:
    * Minimum and maximum password length (6 to 50 characters).
    * Minimum number of uppercase letters, lowercase letters, numbers, and special characters.
* Random Password Generation:
    * Generates passwords that meet user-defined criteria.
    * Includes an intelligent mechanism to balance password composition.
* Password Strength Evaluation:
    * Analyzes the password's length and composition (uppercase, lowercase, numbers, special characters).
    * Classifies strength into three categories: Weak, Moderate, and Strong.
* User-Friendly Input Validation:
    * Ensures the sum of minimum character requirements doesn’t exceed the minimum length.
    * Checks for logical relationships between minimum and maximum length values. 

# How It Works
1. Users input their desired password criteria, such as:
    * Minimum/maximum length.
    * Minimum number of uppercase, lowercase, numeric, and special characters.
2. The program generates a password that meets these criteria while filling in additional characters if needed.
3. The generated password is displayed, along with an evaluation of its strength (Weak, Moderate, or Strong).

# Example Usage
1. Input criteria:
*     Enter minimum number of uppercase letters: 2
      Enter minimum number of lowercase letters: 2
      Enter minimum number of numbers: 2
      Enter minimum number of special characters: 2
      Enter the minimum length of the password (min 6): 12
      Enter the maximum length of the password (max 50): 16
2. Output:
*     Generated Password: D7@a#bC4&E5f
      Password Strength: Strong  
