import csv
from datetime import datetime
from password_generator import generate_password
from utils import get_int_input

print("Welcome to the Bulk Password Generator!")

# Get number of users
num_users = get_int_input("How many users/passwords do you want to generate? ", min_val=1)

# Get password length
length = get_int_input("Enter desired password length: ", min_val=6)

# Get character type choices
print("\nInclude the following in the password? (yes for y/no for n)")
while True:
    use_lower = input("Lowercase (a-z)? ").strip().lower() in ['yes', 'y']
    use_upper = input("Uppercase (A-Z)? ").strip().lower() in ['yes', 'y']
    use_digit = input("Digits (0-9)? ").strip().lower() in ['yes', 'y']
    use_special = input("Special (!@#$&*) ? ").strip().lower() in ['yes', 'y']

    if any([use_lower, use_upper, use_digit, use_special]):
        break
    else:
        print("You must select at least one character type. Please try again.")

# Ensure length meets the requirement
min_length_required = sum([use_lower, use_upper, use_digit, use_special])
while length < min_length_required:
    print(f"Password length must be at least {min_length_required} to include all chosen types.")
    length = get_int_input(f"Enter a new password length (≥ {min_length_required}): ", min_val=min_length_required)

# Get usernames
print("\nEnter the usernames (one per line):")
usernames = []
for i in range(num_users):
    while True:
        try:
            name = input(f"User {i+1} name: ").strip()
            if not name:
                raise ValueError("Username cannot be empty.")
            if name in usernames:
                raise ValueError("Duplicate username. Please enter a unique one.")
            usernames.append(name)
            break
        except ValueError as e:
            print(f"{e}")

# Save to CSV
csv_filename = "generated_passwords.csv"
try:
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['S.No', 'Timestamp', 'Username', 'Password', 'Length'])

        for index, username in enumerate(usernames, start=1):
            try:
                password = generate_password(length, use_lower, use_upper, use_digit, use_special)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([index, timestamp, username, password, length])
            except ValueError as ve:
                print(f"Error for {username}: {ve}")
except PermissionError:
    print(f"Cannot write to '{csv_filename}'. File may be open or locked.")
except Exception as e:
    print(f"Unexpected error while saving CSV: {e}")
else:
    print(f"\n{num_users} passwords saved to '{csv_filename}' successfully!")
