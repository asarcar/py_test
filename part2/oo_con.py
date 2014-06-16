#!/usr/bin/env python

"""This script is to just play around with words used in python OO programming"""
import sys
import urllib
import random

def main():
    """ Plays around with a list of class names """
    num_args = len(sys.argv)

    # Argument Parsing Logic: script language url
    ph_first = num_args >= 2 and sys.argv[1] == "english"
    word_url = "http://learncodethehardway.org/words.txt"
    if (num_args >= 3):
        word_url = sys.argv[2]

    words = get_words(word_url)

    qna(words)

    return

def qna(words):
    """ Generates an endless list of question and answer tuples """
    try:
        while True:
            question_n_answer(words)
            print "Next Loop"
    
    except EOFError:
        print "EOFError: ending loop"
    finally:
        print "\nBye\n"
        return
    
def question_n_answer(words):
    """ Given a random order of phrases and snippets: we create a QnA """
    phrases = {
        "class %%%(%%%):":
            "Make a class names %%% that is-a %%%.",
        "class %%%(object):\n\tdef ___init___(self, ***)":
            "class %%% has-a ___init___ that takes self and *** parameters.",
        "class %%%(object):\n\tdef ***(self, @@@)":
            "class %%% has-a function name *** that takes self and @@@ parameters.",
        "*** = %%%()":
            "Set *** to an instance of class %%%.",
        "***.***(@@@)":
            "From *** get the *** function, and call it with parameters self, @@@.",
        "***.*** = '***'":
            "From *** get the *** attribtue and set it to '***'."
        }
    snips = phrases.keys()
    random.shuffle(snips)
    
    for snip in snips:
        phrase = phrases[snip]
        
        q, a = convert(words, snip, phrase)

        print q
        raw_input("> ")
        print "ANSWER: {}\n\n".format(a)

    return

def convert(words, snippet, phrase):
    """ Gathers OO language based associative description """

    class_names = [w.capitalize() for w in random.sample(words, snippet.count("%%%"))]
    other_names = random.sample(words, snippet.count("***"))

    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(", ".join(random.sample(words, param_count)))

    for sentence in snippet, phrase:
        for word in class_names:
            sentence = sentence.replace("%%%", word, 1)
        for word in other_names:
            sentence = sentence.replace("***", word, 1)
        for word in param_names:
            sentence = sentence.replace("@@@", word, 1)
        results.append(sentence)

    return results

def get_words(word_url):
    """ Fetches all words available in the URL """
    url = "http://learncodethehardway.org/words.txt"
    words = []

    for word in urllib.urlopen(word_url).readlines():
        words.append(word.strip())
        
    print "URL {} words: \"{}\"".format(word_url, ", ".join(words))
        
    return words

if __name__ == "__main__":
    main()
