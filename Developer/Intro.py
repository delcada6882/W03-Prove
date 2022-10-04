import random
here = []
here.__len__()
class Intro:
    def __init__(self):
        self.word = ["python", "hang man", "easy", "difficult", "answer",  "xylophone"] #these are the words that the hangman can go for
        self.parachute = [" ___", "/___\ ", "\   /", " \ / "] #this is the parachute
        self.person = ["  O  "," /|\ ", " / \ ", "\n^^^^^"] #this is the human
    def grabbing_word(self): #this grabs a random word and then turns it into an array of _ to use for render
        num = random.randint(0, 5)
        word_selection = self.word[num]
        final_word = list(word_selection)
        compare = []
        for w in final_word:
            compare.append("_")
        
        return final_word, compare
        
    def render(self, lives, compare): #This displays all of the visual aspects of the game. Things like the parachute and man, also the underscores before you guess.
        string_compare = ""
        for x in compare:
            string_compare += f"{x} "
        print(string_compare)
        print()
        self.parachute.__len__()
        i = self.parachute.__len__() - lives
        while i != self.parachute.__len__():
            print(self.parachute[i])
            i += 1
        
        if lives == 0:
            self.person[0] = "  X  "

        i = 0
        for i in self.person:
            print(i)