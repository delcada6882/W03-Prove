class Win:    
    def check(self, lives, compare, fin_word):
        if lives == 0:
            return 1
        elif fin_word == compare:
            return 2
        else:
            return 0

        