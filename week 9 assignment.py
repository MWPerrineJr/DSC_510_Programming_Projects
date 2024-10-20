#DSC 510
# Week 9
# Programming Assignment
# Author Michael Perrine
# 10/27/2024



#import string library
import string

def process_line(line, word_count_dict):
# process file to lower case
    line = line.strip()
    word_list = line.split()
    for word in word_list:
# remove all punctuation and '--' in file
        if word != '--':
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            add_word(word, word_count_dict)

def add_word(word, word_count_dict):
# update word frequency, word is the key, frequency is the value
    if word in word_count_dict:
        word_count_dict[word] +=1
    else:
        word_count_dict[word] = 1


def pretty_print(word_count_dict):
# print frequency in sorted reverse order
    value_key_list = []
    for key, val in word_count_dict.items():
        value_key_list.append((val, key))
    value_key_list.sort(reverse = True)
    print(f"{'Word':<15} {'Count':<15}")
    print(' '*21)
    for val, key in value_key_list:
        print(f"{key:<15} {val:<15}")


def process_file(word_count_dict, filename):
# write word frequency to a file
    with open(filename, 'a') as file:
        file.write(f"{'Word':<15} {'Count':<15}")
        file.write('-' * 22 + '\n')
#sort word count in decending order
        for word, count in sorted(word_count_dict.items(), key= lambda item: item[1], reverse=True):
            file.write(f"{'Word':<15} {'Count':<15}\n")



def main():
    word_count_dict = {}
    try:
        with open("gettysburg.txt", 'r') as fileHandle:
            for line in fileHandle:
                process_line(line, word_count_dict)
            data =  fileHandle.read()
    except FileNotFoundError as e:
        print(e)
    print('Length of the dictionary:', len(word_count_dict))
    pretty_print(word_count_dict)

if __name__=="__main__":
    main()

