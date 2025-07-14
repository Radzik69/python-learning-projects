import random

random_move = ""
move = ""
score = 0
games = 0
lost = 0
draws = 0
total_wins_to_victory = 0

def generate_random_move():
    global random_move
    avaliable_moves = ['rock', 'paper', 'scissors']
    random_move = random.choice(avaliable_moves)

def user_move():
    global move
    move_number = input('\nEnter 1 to select rock,\nEnter 2 to select paper,\nEnter 3 to select scissors:\n')
    match move_number:
        case '1':
            move = 'rock'
        case '2':
            move = 'paper'
        case '3':
            move = 'scissors'
        case _:
            print('Invalid input')
            user_move()

def check_winner():
    global games
    global score
    global lost
    global draws
    games += 1
    print(f'Your move: {move}\nEnemy move: {random_move}')
    if move == 'rock' and random_move == 'scissors':
        print('You won')
        score+=1
    elif move == 'paper' and random_move == 'rock':
        print('You won')
        score+=1
    elif move == 'scissors' and random_move == 'paper':
        print('You won')
        score+=1
    elif move == 'rock' and random_move == 'paper':
        print('You lost')
        lost+=1
    elif move == 'paper' and random_move == 'scissors':
        print('You lost')
        lost+=1
    elif move == 'scissors' and random_move == 'rock':
        print('You lost')
        lost+=1
    elif move == 'rock' and random_move == 'rock':
        print('Draw')
        draws+=1
    elif move == 'paper' and random_move == 'paper':
        print('Draw')
        draws+=1
    elif move == 'scissors' and random_move == 'scissors':
        print('Draw')
        draws+=1

def check_if_game_over():
    global games
    global score
    global lost
    global draws
    global total_wins_to_victory

    if total_wins_to_victory == score:
        print('The game has ended by your victory!')
        print(f'Stats: your wins: {score}, your losses: {lost}, your draws: {draws}')
    elif total_wins_to_victory == lost:
        print('The game has ended by your loss :(')
        print(f'Stats: your wins: {score}, your losses: {lost}, your draws: {draws}')
    else:
        generate_game_turn()

def get_game_settings():
    global total_wins_to_victory
    try:
        total_wins_to_victory = int(input("\nHow many wins to end game?\n"))
    except Exception as e:
        print(f"Error: {e}")

def generate_game_turn():
    generate_random_move()
    user_move()
    check_winner()
    check_if_game_over()

get_game_settings()
generate_game_turn()