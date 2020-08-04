# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
from os.path import dirname, join, realpath
filename = join(dirname(realpath(__file__)), 'ciphertext.txt')

def find_frequency(file):
    tally = {}

    for character in file:
        if character >= 'A' and character <= 'Z':
            if character not in tally:
                tally[character] = 1
            else:
                tally[character] += 1

    tally_list = list(tally.items())
    tally_list.sort(key=lambda x: x[1], reverse=True)

    return tally_list

def decode(file, tally):

