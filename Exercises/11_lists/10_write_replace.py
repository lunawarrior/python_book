# Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:
import test







test(replace("Mississippi", "i", "I"), "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"

test(replace(s, "om", "am"), "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(s, "o", "a"), "I lave spam! Spam is my favarite faad. Spam, spam, yum!")