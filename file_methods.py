import re

def convert_textfile_to_list(textfile):
    ''' Opens a textfile to read and splits words into a big list of sentences and formats the words.'''
    with open(textfile) as f:
        sentences = f.read()
        sentences = sentences.replace("\n","")
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', sentences.lower())
    return sentences