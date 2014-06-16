#!/usr/bin/env python

# Exercise 37: KEYWORD REVIEW #

#######################
###### Keywords #######
# 1. Generators/Yield # Y
# 2. as               # Y
# 3. Try, Finally     # Y
# 4. Exec             # Y
# 5. assert           # Y
# 6. pass             # Y
# 7. class            # Y
# 8. del, global, lam # Y
# 9. raise, except    # Y
#10. with             # Y
#######################

import ex19 as senop
import ex20 as wordop
import sys as argman

gCount = 10

def main():
    """ Tests a bunch of new python keywords """
    # Test Exec #
    exec("""for i in [1,2,3,4,5]: print (i + 5),""")
    
    # Test Global Variables
    global gCount
    gCount += 5
    assert gCount == 15
    print "\nGlobal Count = {}".format(gCount) 

    try:
        scr, fip, fop = argman.argv
        fobj = FileObj(fip) 

        print "File Obj %r created: ip fname %s: op fname %s" %(fobj, fip, fop)

        # Print state of words
        fobj.printsen()
        fobj.printwords()
        fobj.printswords()

        # Generate Words: Use lambda
        with open(fop, "w") as f:
            f.write("Word List from Iterator: \n")
            for word in fobj.genwords():
                f_w = lambda w: " <" + w + "> "
                f.write(f_w(word))

            f.write("\n----\nSorted Word List from Iterators:\n")
            for word in fobj.gensortwords():
                fs_w = lambda w: " *" + w + "* "
                f.write(fs_w(word))
            f.write("\n----\n")

### Exception Handlers
    except ValueError as e:
        """ Value Error Exception Handler """
        print "Value Error: {}".format(e)
    except FileException as e:
        """ File Exception Handler """
        print "File Exception Raise ({}): {}".format(FileException, e.value)

    finally:
        print "Exiting Function"
        return None

class FileException(Exception): 
    """ Used to raise exceptions on File operatiosn """
    def __init__(self, string):
        self.value = string

    def __str__(self):
        """ converts the exception to a string equivalent """
        return repr(self.value)

class FileObj:
    """ Accepts a text file with sentences, breaks the sentences into words, and sorts the words """ 

    def __init__(self, filename):
        """ Parses the text file and stores list of words in unsorted and sorted order """ 
        try:
            self.f = open(filename, 'r')
            self.txt = self.f.read()
            #            print "Txt \"{}\"".format(self.txt)
            self.words = senop.break_words(self.txt)
            self.swords = senop.sort_words(self.words)
        except IOError as e:
            self.f = None
            str = "Bad file \"{}\" read error".format(filename)
            raise FileException(str)
        finally:
            pass

    def __del__(self):
        """ Free file description """ 
        if (self.f == None):
            return None
        
        self.f.close()
    
    def printsen(self):
        """ Displays the full sentence parsed into words """
        print "Sentence: \"{}\"".format(self.txt)
        return None

    def printwords(self):
        """ Displays the first & last word parsed """
        print "Words: \"{}\"".format(str(self.words))
        wordop.print_first_word(self.words)
        wordop.print_last_word(self.words)
        return None
        
    def printswords(self):
        print "Sorted Words: \"{}\"".format(str(self.swords))
        wordop.print_first_word(self.swords)
        wordop.print_last_word(self.swords)
        return None

    def genwords(self):
        """ Generates the list of words in the file """
        for w in self.words:
            yield w

    def gensortwords(self):
        """ Generates list of words in sorted order in the file """
        for w in self.swords:
            yield w

if __name__ == "__main__":
    main()
