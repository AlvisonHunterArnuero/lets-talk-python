# --------  Conditional if with several cases --------
number = 1

# Check if the number is greater than 3
if number > 3:
    print("Number is greater than 3")

# Check if the number is equal to 3
elif number == 3:
    print("Number is equal to 3")

# The number is less than 3
else:
    print("Number is less than 3")


# -------- Ternary Operator Example --------
gender = "B"
print("Masculine" if gender == "M" else "Femenine")

# Switch case Example (Simulation since this only exist on ver 3.10)

term_to_pass = "python"


def switch_case(search_term: str) -> str:
    language_dict = {
        "JAVASCRIPT": "You can be a web developer",
        "JAVA": "You can be a mobile app developer",
        "SVELTE": "You can be a great web developer",
        "PYTHON": "You can be a Data Scientist",
    }

    search_term = search_term.upper()
    return language_dict.get(search_term, "You can be whatever you want!")


print(switch_case(term_to_pass))

# --------  Second Example using Dictionaries --------
spoken_lang_dict = {
    "English": "You are from England",
    "Spanish": "You are from Nicaragua",
    "French": "You are from France",
    "Portuguese": "You are from Brazil",
}


def nationality(spoken_language: str) -> str:
    spoken_language = spoken_language.title()
    if spoken_language in spoken_lang_dict:
        return spoken_lang_dict[spoken_language]
    else:
        return "We don't know where you come from!"


spoken_language = "French"
print(nationality(spoken_language))


# -------- Example using While Loop --------
count = 0
while count < 5:
    print("Count is: ", count)
    count += 1

# -------- For Loops with Range --------
for num in range(1, 10, 3):
    print("Number is:", num)

favorite_fruits = [
    "apple",
    "banana",
    "cherry",
    "mango",
    "pear",
    "watermelon",
    "pineapple"
]

# Print favorite fruits using a for-each loop
print("My favorite fruits:")
for fruit in favorite_fruits:
    print(fruit)

# Print favorite fruits using an indexed loop
print("My favorite fruits (indexed):")
for index, fruit in enumerate(favorite_fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# Print favorite fruits with odd indices
print("Favorite fruits with odd indices:")
for fruit_index in range(1, len(favorite_fruits), 2):
    print(favorite_fruits[fruit_index])


# -------- For loop using strings --------
message = "Nicaragua"
# Loop through each character in the message
for char in message:
    print("Character:", char)

# -------- Nested for loops --------
# Nested loops to print the values of 'i' and 'j'
for i in range(1, 4):
    for j in range(1, 4):
        print("i is:", i, "j is:", j)

# -------- For loops with break --------

numbers = [1, 2, 3, 4, 5, 6]

# Example 1: Break out of the loop when a condition is met
for num in numbers:
    if num == 5:
        print("Finished loop on number", num)
        break
    print("Current number is:", num)
else:
    print("Loop completed without encountering a break statement.")

print()

# Example 2: Continue to the next iteration when a condition is met
for num2 in numbers:
    if num2 == 3:
        print("I just passed number", num2)
        continue
    print("Current number is:", num2)
else:
    print("Loop completed without encountering a continue statement.")


# -------- For loop with else --------
programmers = [
    "James Gosling",
    "Bjarne Stroustrup",
    "Brendan Eich",
    "Dan Abramov",
    "Guido van Rossum",
    "Yukihiro Matsumoto",
]
for programmer in programmers:
    print("Current Coder is:", programmer)
    # Additional code within the loop if needed
    if programmer == "Guido van Rossum":
        print(f"{programmer} is certainly the best!!")

# Executed after the loop completes
else:
    print("For loop completed without any break")


# For loop with Enumerate and using f-string to format print
countries = ["Nicaragua", "Argentina", "Colombia", "Costa Rica"]
for index, country in enumerate(countries):
    print(f"Index: {index}, Country: {country}")
