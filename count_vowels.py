# count vowels in a sentence or word

# list out the vowels
vowels = ["a", "e", "i", "o", "u"]

text = input("Enter a word or sentence: ").lower()

# setting a counter
counter = 0

# implementing a while loop to iterate through text

for i in text:
    for j in vowels:
        if i == j:
            counter += 1
print(counter)