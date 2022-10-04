from Intro import Intro
from Win import Win
from Mechanics import Mechanics #calling all of the separate files

class Director:
    def __init__(self):
        self.win = Win()
        self.end_con = 0
        self.lives = 4

    def start_game(self):
        self.end_con = 0
        lives = 4
        intro = Intro()
        fin_word, compare = intro.grabbing_word()
        while self.end_con == 0:
            intro.render(lives, compare)

            mechanic = Mechanics()
            lives, compare = mechanic.user_inputs(fin_word, compare, lives)

            self.end_con = self.win.check(lives, compare, fin_word)

        intro.render(lives, compare)

        if self.end_con == 1:
            fin_str = ""
            for x in fin_word:
                fin_str += x
            print(f'\nThe word was "{fin_str}"')
        elif self.end_con == 2:
            print("\nExcellent job. Thanks for playing my game.")

director = Director()
director.start_game()