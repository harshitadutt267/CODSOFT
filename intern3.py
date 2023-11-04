import random
import string

def generate_password(length, complexity):
    character_sets = []

    if complexity == "easy":
        # Use only lowercase letters and digits for an easy password
        character_sets = [string.ascii_lowercase, string.digits]
    elif complexity == "medium":
        # Use lowercase letters, uppercase letters, and digits for a medium password
        character_sets = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    elif complexity == "complex":
        # Use all character sets for a complex password
        character_sets = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    else:
        print("Invalid choice for password complexity.")
        return

    # Combine the selected character sets
    all_characters = ''.join(character_sets)

    # Check if the length is valid
    if length < 8:
        print("Password length should be at least 8 characters.")
        return

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    print(" GENERATE YOUR PASSWORD")
    while True:
        # Ask the user for the desired complexity inside the loop
        while True:
            complexity = input("Choose a password complexity: 'easy,' 'medium,' or 'complex': ").lower()
            if complexity in ["easy", "medium", "complex"]:
                break
            else:
                print("Invalid choice. Please select 'easy,' 'medium,' or 'complex'.")

        # Prompt the user for password length
        while True:
            length = int(input("Enter the desired length of the password: "))

            password = generate_password(length, complexity)

            if password:
                print("Generated Password:", password)  # Displaying the password on the screen
                another_password = input("Do you want to generate another password? (yes/no): ").lower()
                if another_password != "yes":
                    break

if __name__ == "__main__":
    main()



