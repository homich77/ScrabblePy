__author__ = 'user'
import redis

class StructInput(object):
    #letterPoint
    def __init__(self):
        f = open('Scores.txt', 'r')
        self.letterPoint = {}
        try:
            for line in f:
                self.letterPoint[line.split()[0]] = int(line.split()[1])
        finally:
            f.close()
        #print self.letterPoint

    result = {}
    def find_letter_score(self, letter):
        return [self.letterPoint[key] for key in self.letterPoint.keys() if letter in key][0]

    def give_letters(self):
        self.letters = raw_input("7 letters: ")
        if len(self.letters) != 7:
            print "Letters count must be equal 7"
            self.give_letters()

    def find_letter(self, letter):
        for l in self.lettersCopy:
            if l == letter:
                self.lettersCopy.remove(l)
                index = self.wordCopy.index(letter)
                return self.wordCopy.pop(index)

    def find_word(self, word):
        self.wordCopy = list(word)
        self.lettersCopy = list(self.letters)
        temp_word = map(self.find_letter, word)

        if len(self.wordCopy) == 0 and word == ''.join(temp_word):
            scores = map(self.find_letter_score, word)
            scores_sum = sum(scores)
            if not self.result or self.result[1] < scores_sum:
                self.result = [word, scores_sum]
                #self.result.append(word, sum)

    def input(self):
        wordsList = []
        for i in range(int(raw_input("Input: "))):
            wordsList.append(raw_input())

        self.give_letters()
        # Find matches
        map(self.find_word, wordsList)
        print self.result
