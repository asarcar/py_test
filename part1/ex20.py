#!/usr/bin/env python

from sys import argv
import ex19

def main():
    """ Main Function """
    scr = argv
    print "Running %s: no args; Calling fn" %scr
    done = help_func()
    print "Script run %s: Completed %r" %(scr, done)

def help_func():
    """ Helper Function just executes the mainline thread """
    print "Let's practice everything."
    print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

    poem = """
    \tThe lovely world
    \twith logic so firmly planted
    \tcannot discern the needs of love
    \tnor comprehend passion from intuition
    \tand requires an explantion
    \twhere there is none.
    """
    print "--------------"
    print poem
    print "--------------"
    
    five = 10 - 2 + 3 - 5
    print "This should be 6: %s" % five

    start_point = 10000
    beans, jars, crates = secret_formula(start_point)
    
    print "With a starting point of: %d" % start_point
    print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

    start_point = start_point / 10
    
    print "We can also do that this way:"
    print "New starting point of: %d" % start_point
    print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)
                                                                             
    
    sentence = "All good things come to those who weight."

    words = ex19.break_words(sentence)
    sorted_words = ex19.sort_words(words)
    
    print_first_word(words)
    print_last_word(words)
    print_first_word(sorted_words)
    print_last_word(sorted_words)
    sorted_words = ex19.sort_sentence(sentence)
    print sorted_words

    print_first_and_last(sentence)

    print_first_and_last_sorted(sentence)
    
    return True


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = ex19.break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = ex19.sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# Executes main function of the script if the file is directly executed 
if __name__ == "__main__":
    main()
