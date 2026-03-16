import random
import string

def check_strength(password):

    score = 0

    if len(password) >= 8: score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    if any(c.isupper() for c in password) and any(c.islower() for c in password): score += 1
    
    ratings = {0: "Weak", 1: "Weak", 2: "Medium", 3: "Medium", 4: "Strong"}
    return ratings.get(score, "Strong")

def generate_password():

    print("--- Simple Password Generator ---")
    
    try:

        length = int(input("Enter password length: ").strip())
        include_nums = input("Include numbers? (y/n): ").strip().lower() == 'y'
        include_spec = input("Include special characters? (y/n): ").strip().lower() == 'y'
        
        pool = list(string.ascii_letters)
        if include_nums: pool.extend(string.digits)
        if include_spec: pool.extend(string.punctuation)
        
        password = "".join(random.choice(pool) for _ in range(length))
        
        print(f"\nResult: {password}")
        print(f"Strength: {check_strength(password)}")
        
        print("\n" + "-"*20)
        input("Press Enter to close this window...") 

    except ValueError:

        print(" Error: Please enter a number.")
        input("Press Enter to exit...")

if __name__ == "__main__":

    generate_password()

