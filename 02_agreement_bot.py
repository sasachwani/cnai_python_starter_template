# Problem Statement
    # Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).
    # Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):
    # What's your favorite animal? cow
    # My favorite animal is also cow!



# Function to check if the first letter is a vowel
def vowel(word):
    return word[0].lower() in 'aeiou'

# Ask the user for their favorite animal
animal_name: str= input("What is your favorite animal is? ")
animal_name = animal_name.lower()

# Check if the animal name starts with a vowel
if vowel(animal_name):
    print(f"Mya favorit animal is also an {animal_name}!")
else:
    print(f"Mya favorit animal is also a {animal_name}!")
