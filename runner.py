import algo

def print_menu():
    print("This program helps you solve wordle by using your input and only displaying the words that are possible")
    print("To start, enter a word on the wordle website, and then enter the same word in the program")
    print("Based on the feedback, enter the numbers")
    print("0 means the letter is not in the word")
    print("1 means the letter is in the word, but in the wrong spot")
    print("2 means the letter is in the word, and in the correct spot\n")
    print("Sample input:\nmouse\n00100")

def run_game():
    # Running Menu and Algo.py
    file = open("allwords.txt", "r")
    text = file.read()
    words = text.splitlines()
    print_menu()
    user_quit = algo.play_game(words)


    while not user_quit:
        ans = input("Do you want to continue")
        if ans != 'n':
            print("New game started")
            user_quit = algo.play_game(words)
        else:
            break

run_game()
    