class Mechanics:
    def __init__(self):
        self.losing_guess = False
    def user_inputs(self, fin_word, compare, lives): #This gets the input and then see's if its correct.
        use_inp = input("Guess a letter [a-z]: ")
        use_inp = use_inp.lower()
        i = 0
        while i != fin_word.__len__():
            if use_inp == fin_word[i]:
                compare[i] = use_inp
                self.losing_guess = True
            i += 1

                
        if self.losing_guess == False:
            lives -= 1
        
        return lives, compare
