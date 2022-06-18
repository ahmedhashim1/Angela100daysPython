def format_name(fname, lname):
    if fname == "" or lname == "":
        return "Incomplete information is entered"
    else:
        result = fname.title() + " " + lname.title()
        return f"{result}"


print(format_name("ahmed", "hashim"))
