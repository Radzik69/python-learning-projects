import random
import string

password_characters_questions = [
    "Wpisz 1 by dodać małe litery, wpisz coś innego by pominąć: ",
    "Wpisz 1 by dodać duże litery, wpisz coś innego by pominąć: ",
    "Wpisz 1 by dodać liczby, wpisz coś innego by pominąć: ",
    "Wpisz 1 by dodać znaki specjalne, wpisz coś innego by pominąć: ",
]

characters_listed_types = []
password_length = 0
def get_required_info():
    for number in range(len(password_characters_questions)):
        chosen_character = input(password_characters_questions[number])
        if chosen_character == "1":
            match number:
                case 0:
                    characters_listed_types.append("małe")
                case 1:
                    characters_listed_types.append("duże")
                case 2:
                    characters_listed_types.append("liczby")
                case 3:
                    characters_listed_types.append("znaki")
                case _:
                    print("Error")
        else:
            continue
        number = number + 1
    try:
        global password_length
        password_length = int(input("Wpisz długość hasła: "))
    except Exception as e:
        print(f"Error: {e}")

def get_desired_characters():
    all_characters = ""
    if "małe" in characters_listed_types:
        all_characters += string.ascii_lowercase
    if "duże" in characters_listed_types:
        all_characters += string.ascii_uppercase
    if "liczby" in characters_listed_types:
        all_characters += string.digits
    if "znaki" in characters_listed_types:
        all_characters += string.punctuation
    create_password(all_characters)

def create_password(all_characters):
    password = ""
    for number in range(password_length):
        password += random.choice(all_characters)
    print(password)

get_required_info()
get_desired_characters()
