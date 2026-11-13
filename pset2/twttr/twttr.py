text = input("Input: ")

shortened = ""
for letter in text:
    if letter.lower() not in "aeiou":
        shortened += letter

print(shortened)
