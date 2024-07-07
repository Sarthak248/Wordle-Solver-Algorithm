# 5 Letter WORDLE
# Can also suggest random word (automatic play)
# Word/Letter Frequency calculator: https://www.mtholyoke.edu/courses/quenell/s2003/ma139/js/count.html
# Python Online Compiler: https://www.programiz.com/python-programming/online-compiler/
# Wordle Unlimited link: https://wordleunlimited.org/

# To change code to be website dependent and not file dependent, use following code:
# word_url = "https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt"
# response = urllib.request.urlopen(word_url)
# long_txt = response.read().decode()


# File dependent code:
# file = open("all_words.txt", "r")
# text = file.read()
# words =        text.splitlines()

def play_game(words):
    new_words = list(words)
    # possible_words = len(new_words)
    all_words = new_words.copy()
    i = 0
    while i < 6 and len(new_words) > 1:

        # poss = 0 initially
        ctr = 0
        word_input = list(input("Enter:"))
        # print(word_input)
        if word_input != 5:
            if word_input == ['r', 'e', 's', 't', 'a', 'r', 't']:
                print("New game started")
                play_game()
            elif word_input == ['q', 'u', 'i', 't']:
                # user_quit = True
                # print("i came here")
                return True

        spot_input = list(input())
        # all_words = new_words.copy()
        # iterates through each word in possible words and removes words that do not comply with the rules
        j = 0
        while j < 5:
            tmp1 = word_input[j]
            tmp2 = int(spot_input[j])
            if list(word_input).count(tmp1) == 1:
                if tmp2 == 0:
                    # print("letter not in word")
                    for k in all_words:
                        if tmp1 in k:
                            new_words.remove(k)
                elif tmp2 == 1:
                    # print("letter in wrong spot, but in word")
                    # k = 0
                    for k in all_words:
                        if tmp1 not in k or k[j] == tmp1:
                            new_words.remove(k)
                else:
                    # print("correct spot")
                    for k in all_words:
                        if k[j] != tmp1:
                            new_words.remove(k)
            else:
                rep_letter = tmp1
                if tmp2 == 0:
                    # print("letter not in word")
                    for k in all_words:
                        if k[j] == tmp1:
                            new_words.remove(k)
                    ctr = ctr + 1
                elif tmp2 == 1:
                    # print("letter in wrong spot, but in word")
                    # k = 0
                    for k in all_words:
                        if tmp1 not in k or k[j] == tmp1:
                            new_words.remove(k)
                else:
                    # print("correct spot")
                    for k in all_words:
                        if k[j] != tmp1:
                            new_words.remove(k)
            # after all removals are done, list is updated
            all_words = new_words.copy()
            j = j + 1
        if len(new_words) <= 50:
            print(new_words)
        elif len(new_words) == 1:
            return False

        i = i + 1
    return False