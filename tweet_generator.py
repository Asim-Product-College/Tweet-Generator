'''
    Tweet Generator.
    Created by: Asim Zaidi
    https://www.asimzaidi.tech
    https://www.github.com/awesomezaidi

    • This program can create a dictionary of words with their occurances from a text file.
    • Generates a random sentence based off of word frequencies.
'''

from file_methods import *
from random import randint
import sys, random
from markov_chain import MarkovChain

sentences = convert_textfile_to_list('corpus.txt')
generator = MarkovChain(sentences)

# for _ in range(10):
print(generator.make_sentence(12))


# def main():
#     """
#         Create a corpus by calling the convert_textfile_to_list method from the fil_methods module and pass in the source text.
#         Create a histogram with that corpus. (Dictionary with words and their occurances.)
#         Generate a random sentence using the first order Markov Chain.
#     """
    # with open("demofile.txt", "a") as out:
    #     out.write()

