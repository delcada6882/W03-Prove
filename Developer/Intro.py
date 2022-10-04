import random
here = []
here.__len__()
class Intro:
    def __init__(self):
        self.word = ["wordfeas","worfeads","worfeafefeds","wofeaferds","wordsfeawefe","wfeafeords"]
        self.parachute = [" ___", "/___\ ", "\   /", " \ / "]
        self.person = ["  O  "," /|\ ", " / \ ", "\n^^^^^"]
    def grabbing_word(self):
        num = random.randint(2,3)
        word_selection = self.word[num]
        final_word = list(word_selection)
        compare = []
        for w in final_word:
            compare.append("_")
        
        return final_word, compare
        
    def render(self, lives, compare):
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