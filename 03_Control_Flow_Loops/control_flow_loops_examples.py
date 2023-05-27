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