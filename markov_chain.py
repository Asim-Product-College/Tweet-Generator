from dictogram import Dictogram
from random import randint

class MarkovChain(dict):
    """Creates a var word_freq that's a Dictogram with all the words in my corpus and their frequencies."""
    def __init__(self, sentences):
        super(MarkovChain, self).__init__() # make itself a Markov Chain.
        self.START = "!+-2"
        self.END="$$$"
        for sentence in sentences:
            self.compile(sentence)

    # First Order
    def compile(self, sentence):
        """ Compile the sentence into a list of words . """
        words = [self.START] + sentence.split(' ') + [self.END] # Split the sentence into a list of words with START END tokens
        for i in range(len(words)-1): # For every word
            if words[i] not in self: # If the word is not in our Markov Chain.
                self[words[i]] = Dictogram() #  Set its key equal to a new Dictogram.
            self[words[i]].add_count(words[i+1]) # let's go grab the next word and add it to it's Dictogram value.

    def get_next_word(self, dictogram):
        '''Random sampling: Picks a random word from histogram containing words and weights
            Returning a random word based on the weights.
        '''
        words, weights = zip(*dictogram.items())
        
        # accumulator is the seperator between weights... #TODO: draw that out.
        accumulator, separators = 0, []
        for weight in weights:
            accumulator += weight
            separators.append(accumulator)

        rand = randint(0, accumulator)
        for index, separator in enumerate(separators):
            if rand <= separator:
                return words[index]

    def make_sentence(self, length=8):
        words = [self.get_next_word(self[self.START])]
        while words[-1] is not self.END:
            words.append(self.get_next_word(self[words[-1]]))
        return ' '.join(words[:-1])

# .....Visual.....
# one fish two fish red fish blue fish two shark
# {
#     one : {
#             fish: 1,
#           }
#     fish : {
#             two : 2,
#             red : 1,
#             blue : 1
#            }
#     two :
#     red :
#     blue :
#     shark :
# }

# START STOP TOKENS

