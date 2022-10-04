With the hangman like game, I plan on using encapsulation by separating my game into special files with one purpose. In order to make the intro to the hangman game work, we'll need a function for grabbing a word, turning it into an array and we'll need a render function that shows and saves the players remaining lives. After that we'll need user-input function that will take the user's guess then compare it with the word that our grabbing-word function returns. From there we can calculate remaining lives and then run the render function again. We'll also need a winning-condition function that checks if the winning-condition has been met so that the game can be finished.

Class Director:
    win = Win()
    loss_c = win.loss_check
    win_c = win.win_check
    lives = 3
    def start_game(self):
        while win_c = false or loss_c = false:
            intro = Intro()
            fin_word, compare = intro.grabbing_word(self)
            intro.render(self, lives, fin_word, compare)

            mechanic = Mechanics()
            lives = mechanic.user_inputs(self, fin_word, compare, lives)

            lost_c, win_c = win.check(self, lives, compare, fin_word)


import random
Class Intro:
    word = ["words","words","words","words","words","words"]
    parachute = [" ___", "/___\", "\   /", " \ / "]
    person = ["  O  "," /|\", " / \"]
    def grabbing_word(self):
        num = random.randint(2,3)
        word_selection = word[num]
        final_word = list(word_selection)
        compare = []
        for x in final_word:
            compare[x] = "_"
        
        return final_word, compare
        
    def render(self, lives=3, fin_wor, compare):
        for x in compare:
            print(x)

        i = parachute.length - lives
        while i != parachute.length:
            print(parachute[i])
            i += 1
        
        for x in person:
            print(person[x])

Class Mechanics:
    def user_inputs(self, fin_word, compare, lives):
        losing_guess = false
        use_inp = input("Guess a letter [a-z]: ")
        use_inp = use_inp.toLowerCase()
        for x in fin_word:
            if use_inp == x:
                compare[x] == use_inp
                losing_false = true
        if losing_guess = false:
            lives -= 1
        
        return lives

Class Win:
    def __init__(self):
        self.win_check = false
        self.loss_check = false
    
    def check(self, lives, compare, fin_word):
        if lives = 0:
            return true, false
        elif fin_word = compare:
            return false, true


        