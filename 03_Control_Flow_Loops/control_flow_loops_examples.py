num = 1
if num > 3:
    print("Numero Mayor que 3")
elif num == 3:
    print("Numero igual a 3")
else:
    print("Numero menor que 3")

# Ternary Operator Example
gender = "B"
print("Masculine" if gender=="M" else "Femenine")

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

# Second Example using Dictionaries
spoken_lang_dict = {"English": "You are from England", "Spanish": "You are from Nicaragua",
                    "French": "You are from France", "Portuguese": "You are from Brazil"}

def nationality(spoken_language: str)-> str:
    spoken_language = spoken_language.title()
    if spoken_language in spoken_lang_dict:
        return(spoken_lang_dict[spoken_language])
    else:
        return "We don't know where you come from!"

spoken_language = "French"
print(nationality(spoken_language))

