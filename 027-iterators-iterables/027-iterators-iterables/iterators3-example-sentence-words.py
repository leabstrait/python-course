# Using a class
class Sentence(object):

    def __init__(self, sentence):
        self.sentence = sentence

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.sentence) == 0:
            raise StopIteration

        word_end_idx = self.sentence.find(' ')
        if word_end_idx != -1:
            word = self.sentence[:word_end_idx]
            self.sentence = self.sentence[word_end_idx + 1:]
        else:
            word = self.sentence
            self.sentence = ''
        return word

my_sentence = Sentence('This is a test')

for word in my_sentence:
    print(word)

# Using a generator function

def wordcount(sentence):
    while not len(sentence) == 0:
        word_end_idx = sentence.find(' ')
        if word_end_idx != -1:
            word = sentence[:word_end_idx]
            sentence = sentence[word_end_idx + 1:]
        else:
            word = sentence
            sentence = ''
        yield word    

my_sentence = wordcount('This is a test')

for word in my_sentence:
    print(word)

# itertools provides some useful methods for iterations and stuff
