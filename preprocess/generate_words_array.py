import subprocess
from preprocess.tool_utility import getToken


def getAllWords():
    subprocess.check_output([ "perl", "./word_count.pl", "Data.txt"])
    all_words_array = getToken("words.txt")

    words_array = []
    length = len(all_words_array)

    #get every third element of an array
    i = 0
    c = 1
    while i < length:

        if (c%3)==0:
            words_array.append(all_words_array[i])

        i += 1
        c += 1

    return words_array


#array = getAllWords()
#write_into_file(array,'words2.txt')