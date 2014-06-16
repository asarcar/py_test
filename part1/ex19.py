#!/usr/bin/env python

from sys import argv

def break_words(str_sen):
    """Breaks words for us given a string sentence"""
    return str_sen.split( )

def sort_words(word_list):
    """Sort every word in word_list"""
    return sorted(word_list)

def first_word(word_list):
    """Pops and gives first word in the word_list"""
    word = word_list[0]
    del word_list[0]
    return word

def last_word(word_list):
    """Pops and gives first word in the word_list"""
    return word_list.pop(-1)

def sort_sentence(str_sen):
    """Sorts the words in a sentence and returns sorted word list"""
    return sort_words(break_words(str_sen))

def first_n_last_word(str_sen):
    """Returns first and last words of sentence"""
    words = break_words(str_sen)
    return (first_word(words), last_word(words))

def first_n_last_sort_word(str_sen):
    """Returns first and last words of sentence when words are sorted"""
    swords = sort_words(break_words(str_sen))
    return (first_word(swords), last_word(swords))

def main():
    scr, sen = argv

    words = break_words(sen)
    print "Sentence: \"%s\"; " %sen + "List: %s; " % str(break_words(sen))
    
    swords = sort_words(words)
    print "Sorted Words: %s" % str(swords)

    fword = first_word(words)
    lword = last_word(words)
    print "Updated List: %s; " % str(words) + "First Word: %s; Last Word: %s." %(fword, lword)
    
    print "Sentence %s; " %sen, "First Word: %s; Last Word: %s" %first_n_last_word(sen)

    print "Sentence %s; " %sen, "First Sorted Word: %s; Last Sorted Word: %s" %first_n_last_sort_word(sen)

    
if __name__ == "__main__":
    main()

