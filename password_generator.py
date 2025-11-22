import random
import string

class PasswordGenerator:
    def __init__(self):
        self.generated_passwords = []
    
    def generate_password(self, length=12, use_uppercase=True, use_lowercase=True, 
                         use_numbers=True, use_symbols=True, exclude_similar=True):
        """
        Generate a customizable password
        - exclude_similar: Exclude similar characters like l, 1, I, O, 0
        """
        characters = ""
        
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation
        
        # Exclude similar characters if requested
        if exclude_similar:
            similar_chars = "l1IoO0"
            characters = ''.join(c for c in characters if c not in similar_chars)
        
        # Ensure minimum requirements can be met
        if len(characters) == 0:
            return "Error: No character types selected!"
        
        # Ensure we have at least one of each selected character type
        password = []
        if use_lowercase and string.ascii_lowercase:
            password.append(random.choice(string.ascii_lowercase))
        if use_uppercase and string.ascii_uppercase:
            password.append(random.choice(string.ascii_uppercase))
        if use_numbers and string.digits:
            password.append(random.choice(string.digits))
        if use_symbols and string.punctuation:
            password.append(random.choice(string.punctuation))
        
        # Fill the rest randomly
        remaining_length = length - len(password)
        if remaining_length < 0:
            remaining_length = 0
        
        password.extend(random.choice(characters) for _ in range(remaining_length))
        
        # Shuffle the password
        random.shuffle(password)
        final_password = ''.join(password)
        
        # Store generated password
        self.generated_passwords.append(final_password)
        
        return final_password
    
    def password_strength(self, password):
        """Check password strength"""
        score = 0
        if len(password) >= 12: score += 2
        elif len(password) >= 8: score += 1
        
        if any(c.islower() for c in password): score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in string.punctuation for c in password): score += 1
        
        if score >= 5: return "Strong 💪"
        elif score >= 3: return "Medium 👍"
        else: return "Weak 👎"
    
    def show_history(self):
        """Show previously generated passwords"""
        if not self.generated_passwords:
            print("No passwords generated yet!")
            return
            
        print("\n" + "="*40)
        print("📜 PASSWORD HISTORY")
        print("="*40)
        for i, pwd in enumerate(self.generated_passwords[-5:], 1):
            strength = self.password_strength(pwd)
            print(f"{i}. {pwd} - {strength}")

def main_menu():
    generator = PasswordGenerator()
    
    while True:
        print("\n" + "="*50)
        print("🔐 ADVANCED PASSWORD GENERATOR")
        print("="*50)
        print("1. Generate Custom Password")
        print("2. Generate Quick Strong Password")
        print("3. View Password History")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")
        
        if choice == '1':
            # Custom password generation
            print("\n--- Custom Password Settings ---")
            try:
                length_input = input("Password length (default 12): ")
                length = int(length_input) if length_input else 12
                
                use_upper = input("Include uppercase? (y/n, default y): ").lower() != 'n'
                use_lower = input("Include lowercase? (y/n, default y): ").lower() != 'n'
                use_nums = input("Include numbers? (y/n, default y): ").lower() != 'n'
                use_sym = input("Include symbols? (y/n, default y): ").lower() != 'n'
                exclude_sim = input("Exclude similar characters? (y/n, default y): ").lower() != 'n'
                
                password = generator.generate_password(
                    length=length,
                    use_uppercase=use_upper,
                    use_lowercase=use_lower,
                    use_numbers=use_nums,
                    use_symbols=use_sym,
                    exclude_similar=exclude_sim
                )
                
                print(f"\nGenerated Password: {password}")
                print(f"Strength: {generator.password_strength(password)}")
                
            except ValueError:
                print("Please enter valid numbers!")
                
        elif choice == '2':
            # Quick strong password
            password = generator.generate_password(length=16)
            print(f"\nStrong Password: {password}")
            print(f"Strength: {generator.password_strength(password)}")
        
        elif choice == '3':
            generator.show_history()
            
        elif choice == '4':
            print("Thanks for using the Password Generator!")
            break
            
        else:
            print("Invalid choice! Please try again.")
# Start the program
if __name__ == "__main__":
    main_menu()