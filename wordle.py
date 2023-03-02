import sys

file = open("words.csv", "r")
file_string = list(file)[0].replace("\n", "")
file.close()
word_list = list(file_string.split(","))

include_char = ""
include_char_2 = ""
include_char_3 = ""
include_char_4 = ""
include_char_5 = ""

if len(sys.argv) < 2:
    sys.exit("Please enter a starting input")
input = sys.argv[1]
if len(sys.argv) > 2:
    include_char = sys.argv[2]
if len(sys.argv) > 3:
    include_char_2 = sys.argv[3]
if len(sys.argv) > 4:
    include_char_3 = sys.argv[4]
if len(sys.argv) > 5:
    include_char_4 = sys.argv[5]
if len(sys.argv) > 6:
    include_char_5 = sys.argv[6]

if len(input) != 5:
    sys.exit("Invalid Input - must be exactly five (5) characters")
if len(include_char) > 1:
    sys.exist("Include Char #1 must be only one letter")
if len(include_char_2) > 1:
    sys.exist("Include Char #2 must be only one letter")
if len(include_char_3) > 1:
    sys.exist("Include Char #3 must be only one letter")
if len(include_char_4) > 1:
    sys.exist("Include Char #4 must be only one letter")
if len(include_char_5) > 1:
    sys.exist("Include Char #5 must be only one letter")


def filter_words(words, char, index):
    new_words = []
    for word in words:
        if word[index] is char:
            new_words.append(word)
    return new_words


def filter_include_char(words, include_char):
    new_words = []
    for word in words:
        if include_char in word:
            new_words.append(word)
    return new_words


for (idx, char) in enumerate(input):
    if char != "_":
        word_list = filter_words(word_list, char, idx)

if len(include_char) > 0:
    word_list = filter_include_char(word_list, include_char)
if len(include_char_2) > 0:
    word_list = filter_include_char(word_list, include_char_2)
if len(include_char_3) > 0:
    word_list = filter_include_char(word_list, include_char_3)
if len(include_char_4) > 0:
    word_list = filter_include_char(word_list, include_char_4)
if len(include_char_5) > 0:
    word_list = filter_include_char(word_list, include_char_5)

print(word_list)
