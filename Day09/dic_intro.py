programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",

}

print(programming_dictionary)

# print(programming_dictionary["Bug"])

# Adding data to Dictionary
programming_dictionary["Loop"] = "The action of doing something again and again."

print(programming_dictionary)

# create an empty dictionary
empty_dic = {}

# Wipe a dictionary
# programming_dictionary = {}
# print(programming_dictionary)
programming_dictionary["Bug"] = "A moth in your computer"

print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key, ":", programming_dictionary[key])
    # print(programming_dictionary[key])
