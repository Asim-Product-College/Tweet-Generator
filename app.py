import os, sys, random
from random import randint
from flask import Flask, render_template, jsonify
from file_methods import *
from markov_chain import MarkovChain

app = Flask(__name__)
sentences = convert_textfile_to_list('corpus.txt')
generator = MarkovChain(sentences)

@app.route('/')
def hello_world():
    sentence = generator.make_sentence()
    return render_template("index.html", tweet="Welcome to my random tweet generator! Hit refresh to see random tweets!")

@app.route('/tweet')
def tweet():
        sentences = convert_textfile_to_list('corpus.txt')
        generator = MarkovChain(sentences)
        tweet = generator.make_sentence()
        return jsonify({'tweet': tweet})


if __name__ == '__main__':
    app.run(debug=True)