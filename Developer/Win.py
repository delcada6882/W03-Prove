class Win:    
    def check(self, lives, compare, fin_word): #this just returns how the game ends.
        if lives == 0:
            return 1
        elif fin_word == compare:
            return 2
        else:
            return 0

        