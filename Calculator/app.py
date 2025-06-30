possibleSigns = [
    "+",
    "-",
    "*",
    "/",
    "(",
    ")",
    "=",
    "b",
]

calculation = []

def choose_action():
    check_sign()
    print(calculation)
    print(f"Możliwe znaki: {possibleSigns}")
    choice_of_action = input("Wpisz 1 jeśli chcesz dodać liczbę, Wpisz 2 jeśli chcesz dodać znak: ")
    checkAction(choice_of_action)

def checkAction(choice_of_action):
    if choice_of_action == "1":
       add_number()
    elif choice_of_action == "2":
        add_sign()
    else:
        choose_action()

def add_number():
    try:
        number = float(input("Wpisz liczbę: "))
        calculation.append(number)
        choose_action()
    except Exception as e:
        print(f"Error: {e}")

def add_sign():
    try:
        sign = str(input("Wpisz znak z listy: "))
        if sign in possibleSigns:
            calculation.append(sign)
            choose_action()
        else:
            print("Brak znaku w liście")
            add_sign()
    except Exception as e:
        print(f"Error: {e}")

def check_sign():
    if len(calculation) == 0:
        return
    if calculation[-1] == "=":
        end_calculation()
    elif calculation[-1] == "b":
        calculation.pop(len(calculation)-1)
        calculation.pop(len(calculation)-2)

def end_calculation():
    if calculation[-1] == "=":
        calculation.pop()

    expression = " ".join(map(str, calculation))

    try:
        result = eval(expression)
        print(f"Wyrażenie: {expression}")
        print(f"Wynik: {result}")
    except Exception as e:
        print(f"Error: {e}")

    calculation.clear()


choose_action()