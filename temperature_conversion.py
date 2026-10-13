# celsius to fahrenheit
temp_celsius = float(input("What is the temperature in degree celsius? "))

temp_fahrenheit = round((temp_celsius * (9/5)) + 32, 2)

print(f"{temp_celsius} degree celsius is {temp_fahrenheit} in degree fahrenheit.")


# Fahrenheit to celsius
degree_fahrenheit = float(input("What's the temperature in fahrenheit? "))

degree_celsius = round(((degree_fahrenheit - 32) / 1.8), 2)

print(f"{degree_fahrenheit} degree fahrenheit is {degree_celsius} in degree celsius.")