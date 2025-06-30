import random

score = 0

def get_range():
    print("Minimalna różnica to 10")
    min_range = int(input("Wpisz minimalny zakres do zgadywania: "))
    max_range = int(input("Wpisz maksymalny zakres do zgadywania: "))
    if max_range - min_range <= 10:
        print("Zły zakres")
        return get_range()
    else:
        return min_range, max_range

def get_random_number(min_range, max_range):
    return random.randint(min_range, max_range)

def guess_number(min_range, max_range, random_number):
    global score
    while True:
        user_guessed_number = int(input(f"Zgadnij liczbę między {min_range} a {max_range}: "))
        score += 1

        if random_number == user_guessed_number:
            print(f"Zgadłeś liczbę!, wynik: {score}")
            again = input('Jeśli chcesz rozpocząć ponownie grę kliknij "y": ').strip().lower()
            if again == "y":
                start_game()
            else:
                print("Dzięki za grę!")
            break
        elif user_guessed_number > random_number:
            print("Niżej")
        elif user_guessed_number < random_number:
            print("Wyżej")
        else:
            print("Error")

def start_game():
    global score
    score = 0
    min_range, max_range = get_range()
    random_number = get_random_number(min_range, max_range)
    guess_number(min_range, max_range, random_number)

start_game()
