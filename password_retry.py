# password retry system

PASSWORD = "Rahat@2234.2026"

# ask user for password
# password = input("Enter your password: ")

"""if password == PASSWORD:
    print("Login successful!")
else:
    print("Login Failed!")"""

# implementing this using a while loop
# give user 3 tries to get the password right before locking them out

retry = 3

i = 0

while i < retry:
    password = input("Enter your password: ")
    if password == PASSWORD:
        print("Login successful!")
        break
    print("Incorrect password.")
    i += 1
else:
    print("Login Failed! You have been locked out.")