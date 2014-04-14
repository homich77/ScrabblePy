__author__ = 'user'
import redis

class StructInput(object):
    result = {}

    def __init__(self):
        f = open('Scores.txt', 'r')
        self.letterPoint = {}
        try:
            for line in f:
                self.letterPoint[line.split()[0]] = int(line.split()[1])
        finally:
            f.close()

    def find_letter_score(self, letter):
        return [self.letterPoint[key] for key in self.letterPoint.keys() if letter in key][0]

    def give_letters(self):
        self.letters = sorted(raw_input("7 letters: ").strip().lower())
        if len(self.letters) != 7:
            print "Letters count must be equal 7"
            self.give_letters()

    def find_word(self, word):
        wordCopy = list(word)
        lettersCopy = list(self.letters)
        for letter in sorted(word):
            for l in lettersCopy:
                if l == letter:
                    lettersCopy.remove(l)
                    index = wordCopy.index(letter)
                    wordCopy.pop(index)
                    break
                elif l > letter:
                    return

        if len(wordCopy) == 0:
            scores_sum = sum(map(self.find_letter_score, word))
            if not self.result or self.result[1] < scores_sum:
                self.result = [word, scores_sum]

    def input(self):
        wordsList = []
        for i in range(int(raw_input("Input: "))):
            wordsList.append(raw_input().lower())

        self.give_letters()
        # Find matches
        map(self.find_word, wordsList)
        print self.result[0]
