from os import stat_result
from token import STAR
from tracemalloc import start

reader = open('problem.txt', 'r') # Next 2 lines of code read the "problem.txt" file line by line for each input
textLines = reader.readlines()

def parseWord(startLetters, word): #Recursive function that parses each line in a way where every possible letter combination is found, while only returning, by the end, the first and longest letterset
    index = 0
    temp = ""
    stored = startLetters
    for letter in word:
        index = index + 1
        if (startLetters == "" or startLetters[len(startLetters)-1] <= letter): 
            temp = parseWord(startLetters + letter, word[index:])
        if len(temp) > len(stored): # After the recursion in the loop is complete, the new temp variable will compare its length to the current length of the letters in the current combination
            stored = temp # The temp variable is stored if it is larger
    return stored # This loop occurs until no more letters in the word need be parsed, then the program understands to ultimately return the longest value to be compared, as it is now the temp variable

def strippedText(text): # Function removes any characters from the line of text that aren't letters and returns the new line after it has finished
    newWord = ""
    for letter in str(text):
        if letter.upper() != letter.lower():
            newWord += letter.lower()
    return newWord

for line in textLines: # Loop cycles for every line of input within the read text file
    word = parseWord("", strippedText(line.strip())) # Function ceases after the last recursion for the first loop of the line has completed. The first longest chronological word is then passed in "word"
    print(f"\nOriginal Word: {line.strip()}\nEarliest Largest Alphabetical Word: {word}\nLength: {len(word)}")