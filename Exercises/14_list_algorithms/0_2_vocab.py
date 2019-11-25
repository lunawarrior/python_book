#Here is a more realistic problem.

# As children learn to read, there are expectations that their vocabulary will grow. 
# So a child of age 14 is expected to know more words than a child of age 8. 
# When prescribing reading books for a grade, an important question might be 
#   "which words in this book are not in the expected vocabulary at this level?”
#
# Let us assume we can read a vocabulary of words into our program, and read the text of a book, 
# and split it into words. Let us write some tests for what we need to do next. 
# 
# Test data can usually be very small, even if we intend to finally use our program for larger cases:

# Try pulling your search_linear function in from the last problem.


vocab = ["apple", "boy", "dog", "down",
                          "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()




from test import test
test(find_unknown_words(vocab, book_words) == ["from", "to"])
test(find_unknown_words([], book_words) == book_words)
test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])