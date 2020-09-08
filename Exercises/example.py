# f_out = open("print_to_this.txt", "w")
# f_out.write("Write this\n")
# f_out.write("and this\n")
# f_out.close()

# cout << "this is a test" << endl

def arrow_arrow(handle, to_write):
    open(handle, "a")
    handle.write(to_write)
    handle.close()
    return handle



arrow_arrow( arrow_arrow("print_to_this.txt", "Write this now\n"), "And this again\n" )
