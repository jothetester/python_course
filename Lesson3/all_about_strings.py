string1 = 'hello World'
string2 = "1234"
print("string 1 is :", string1)
print("string 1 is :", string2)
length = len(string1)
print("Length of string 1 is :", length)
print("Length of string 2 is :", len(string2))

##Delimiters
string3 = "we're #1!"
string4 = 'I said, "put it over by the llama"'
print("string 3 is :", string3)
print("string 4 is :", string4)

string5 = "This multiline string is \
           is displayed as one line"
print("string 5 is :", string5)

paragraph = "This planet has - or rather had - a problem, which was \
this: most of the people living on it were unhappy for pretty much "

print("The paragraph is", paragraph)

paragraph2 = """
This planet has—or rather had—a problem, which was
this: most of the people living on it were unhappy for
pretty much of the time. Many solutions were suggested
for this problem, but most of these were largely concerned
with the movements of small green pieces of
paper, which is odd because on the whole it wasn’t the
small green pieces of paper that were unhappy. """

print("The paragraph2 is", paragraph2)

preserving_white_space = """An example of a
                                     string that spans across multiple lines
                                                        that also preserves whitespace."""
print("string with white space : ", preserving_white_space)

# String Concatenation
string1 = "abra"
string2 = "cadabra"
magic_string = string1 + string2
print("concatenated string is : ", magic_string)

# String Indexing
flavour = "strawberry milkshake"
letter = flavour[5]
print("letter is ", letter)

#slicing
letters = flavour[0:3]
print("sliced letters :", letters)
new_word = flavour[11:20]
print("a sliced word :", new_word)

#string functions
flavour = flavour.upper()
print("The flavour is:",flavour)


