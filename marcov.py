from konlpy.tag import Twitter
import random


class Marcov:
    def __init__(self):
        self.root = {'START': set()}
        self.twitter = Twitter()

    def split(self, sentence):
        return self.twitter.pos(sentence)

    def train(self, sentence):
        words = self.split(sentence)
        cword = words[0]
        self.root['START'].add(cword)
        for word in words[1:]:
            next_word_list = self.root.setdefault(cword, set())
            next_word_list.add(word)
            cword = word
        else:
            end_word_list = self.root.setdefault('END', set())
            end_word_list.add(cword)

    def get_random(self, word_list):
        cword = random.sample(word_list, 1)
        return cword[0]

    def make_sentence(self):
        sentence = ""
        cword = self.get_random(self.root['START'])
        sentence += cword[0]
        while cword not in self.root['END']:
            cword = self.get_random(self.root[cword])
            word, punc = cword
            if punc != "Josa" and punc != "Eomi":
                sentence += " "
            sentence += word
        return sentence