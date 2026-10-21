#A program to classify person's into age groups based on their age (Child, Teenager, Adult, Senior, Elderly)

age = int(input("How old are you? "))

if age <=12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 35:
    print("Adult")
elif age <= 55:
    print("Senior")
else:
    print("Elderly")