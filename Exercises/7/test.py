import sys

def test(value, gold):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if value == gold:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED, got {1}, expected {2}.".format(linenum, value, gold))
    print(msg)