def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds


book_words = get_words_in_book(
    "Exercises/14_list_algorithms/alice_in_wonderland.txt")
print("There are {0} words in the book, the first 100 are\n{1}".
           format(len(book_words), book_words[:100]))

def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

bigger_vocab = load_words_from_file("Exercises/14_list_algorithms/vocab.txt")


def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (i, v) in enumerate(xs):
       if v == target:
           return i
    return -1

def find_unknown_words(vocab, words):
    to_return = []
    for word in words:
        index = search_linear(vocab, word)
        if index == -1:
            to_return.append(word)
    return to_return

import time
t0 = time.clock()
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.clock()

print("There are {0} words not known in that book, the first 100 are\n{1}".
      format(len(missing_words), missing_words[:100]))
print("That took {0:.4f} seconds.".format(t1-t0))
