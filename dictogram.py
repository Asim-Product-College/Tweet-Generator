#!python
from __future__ import division, print_function  # Python 2 and 3 compatibility

class Dictogram(dict):
    """Dictogram is just a histogram as a dictionary where key value pairs are the words with their frequencies."""
    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__() # Initialize this as a new dict
        
        self.types = 0  # Count of distinct word types
        self.tokens = 0  # Total count of all word tokens
        
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)
    
    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # Increase word frequency by count
        if word in self:
            self[word] += count
        else:
            self[word] = count
            self.types += 1
        
        self.tokens+= count
    
    def frequency(self, word):
        """Increase word frequency by count."""
        return 0 if word not in self else self[word]
    
def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    
def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                        ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())

if __name__ == '__main__':
    main()


# one : fish
# fish : two, blue
# two : fish
# red : fish
# blue : fish