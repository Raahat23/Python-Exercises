# Personal Information Formatter

# Ask user for their full name
full_name = input("Enter your full name: ").title().strip()

# Ask user for their initials
name_initials = input("Enter your initials: ").upper().strip()

# Ask user for their age
age = int(input("How old are you? "))

# Ask user for their email address
email = input("Enter your email address: ").lower().strip()

# Ask user for their occupation
occupation = input("What's your occupation? ").title().strip()

# Ask user for the city they reside in
city = input("City you live in: ").title().strip()

# display information in a well formatted form
print("------- PERSONAL PROFILE -------")
print(f"""Name: {full_name}\nInitials: {name_initials}\nAge: {age}\nEmail: {email}
Occupation: {occupation}\nCity: {city}""")
print(f"{'-' * 32}")