word = input("Enter a word: ")
vowels = ["a", "e", "i", "o", "u"]
count = 0
for letter in word:
    if letter.lower() in vowels:
        count += 1
print(f"There are {count} vowels in the word '{word}'.")
