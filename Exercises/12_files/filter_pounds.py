def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    while True:
        text = infile.readline()
        if len(text) == 0:
           break
        if text[0] == "#":
           continue
        if text[-2] == '/':
            continue

        # Put any more processing logic here
        outfile.write(text)

    infile.close()
    outfile.close()

filter('test.txt', 'test_filtered.txt')
