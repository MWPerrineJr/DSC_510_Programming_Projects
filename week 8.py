#DSC 510
# Week 8
# Programming Assignment
# Author Michael Perrine
# 10/17/2024
import string

# Run the read file and create a dictionary
getty = open("gettysburg.txt", "r")
read = getty.readlines()



# add word to the dictionary

def add_word(words_add, dict: read):
    if words_add in read:
        dict [words_add] += 1
    else:
        dict [words_add] = 1

# reformat text file to remove punctuation and separate each word into a string

def process_line(line, dict: read):
    line = line.translate(str.maketrans(',', string.punctuation))
    line_process = line.lower()
    words = line_process.split()

# adds words to the dictionary

    for words in words:
        add_word(words, dict)

def pretty_print(dict: read):
    new_read = list()
    for key,  value in list(dict.items()):
        new_read.append((value, key))
        new_read.sort(reverse = True)

print(f"\n length of dict:{len(read)}")

print(f"\n Word count: ")

# sort words in decreasing order
for word ,count in sorted(dict.items(), key = lambda item: item[1], reverse=True ):
      print(f"{word: < 12} {count}")
def main():
    dict = {}

    try:
        with open("gettysburg.txt", "r") as gba_file:
            for line in gba_file:
                process_line(line , dict)

        pretty_print(dict)

    except:
        print("File gettysburg not found")


if"_name_" == "_main_":
    main()
































