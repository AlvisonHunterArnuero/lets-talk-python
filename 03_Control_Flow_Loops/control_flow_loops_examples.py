# --------  Conditional if with several cases --------
num = 1
if num > 3:
    print("Numero Mayor que 3")
elif num == 3:
    print("Numero igual a 3")
else:
    print("Numero menor que 3")

# -------- Ternary Operator Example --------
gender = "B"
print("Masculine" if gender == "M" else "Femenine")

# Switch case Example (Simulation since this only exist on ver 3.10)

term_to_pass = "python"


def switch_case(search_term: str) -> str:
    search_term = search_term.upper()
    if (search_term == "JAVASCRIPT"):
        return ("You can be a web developer")
    elif (search_term == "JAVA"):
        return ("You can be a mobile app developer")
    elif (search_term == "SVELTE"):
        return ("You can be a great web developer")
    elif (search_term == "PYTHON"):
        return ("You can be a Data Scientist")
    else:
        return ("You can be what you want!")


print(switch_case(term_to_pass))

# --------  Second Example using Dictionaries --------
spoken_lang_dict = {"English": "You are from England", "Spanish": "You are from Nicaragua",
                    "French": "You are from France", "Portuguese": "You are from Brazil"}


def nationality(spoken_language: str) -> str:
    spoken_language = spoken_language.title()
    if spoken_language in spoken_lang_dict:
        return (spoken_lang_dict[spoken_language])
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
    print("Number is: ", num)

favorite_fruits = ["apple", "banana", "cherry", "mango", "pear", "watermelon", "pineapple"]
for fruit in favorite_fruits:
    print(fruit)

for fruit_index in range(1, len(favorite_fruits), 2):
    print(favorite_fruits[fruit_index])

# -------- For loop using strings --------
message = "Nicaragua"
for char in message:
    print("Character: ", char)

# -------- Nested for loops --------
for i in range(1, 4):
    for j in range(1, 4):
        print("is is: ", i, "j is: ", j)

# -------- For loops with break --------
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num == 5:
        print("Finished loop on number ", num)
        break
    print("Current number is: ", num)

for num2 in numbers:
    if num2 == 3:
        print("I just passed number ", num2)
        continue
    print("Current number is: ", num2)

# -------- For loop with else --------
for n in numbers:
    print("Current number is : ", n)
else:
    print("For loop completed")

# -------- For loop with enumerate --------
countries = ["Nicaragua", "Argentina", "Colombia", "Costa Rica"]
for index, country in enumerate(countries):
    print("Index: ", index, "Country: ", country)
