from Intro import Intro
from Win import Win
from Mechanics import Mechanics #calling all of the separate files

class Director:
    def __init__(self): #init values
        self.win = Win()
        self.end_con = 0

    def start_game(self): #This is the main gameplay loop
        lives = 4 #init the lives value
        intro = Intro()
        fin_word, compare = intro.grabbing_word() #getting the main word
        while self.end_con == 0: #starting the actual loop
            intro.render(lives, compare) #doing the render

            mechanic = Mechanics()
            lives, compare = mechanic.user_inputs(fin_word, compare, lives) #getting the input

            self.end_con = self.win.check(lives, compare, fin_word) #checking if you lost or won.
            #then again and again

        intro.render(lives, compare) #one last render to see your defeat or victory

        if self.end_con == 1: #based on how you ended the game you either get a good job message or a message saying what the word was
            fin_str = ""
            for x in fin_word:
                fin_str += x
            print(f'\nThe word was "{fin_str}"')
        elif self.end_con == 2:
            print("\nExcellent job. Thanks for playing my game.")

director = Director() #init the director 
director.start_game() #and starting the game.