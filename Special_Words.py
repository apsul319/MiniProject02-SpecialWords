from os import stat_result
from token import STAR
from tracemalloc import start

reader = open('problem.txt', 'r')
textLines = reader.readlines()

def parseWord(startLetters, word):
    index = 0
    temp = ""
    stored = startLetters
    for letter in word:
        index = index + 1
        if (startLetters == "" or startLetters[len(startLetters)-1] <= letter): 
            temp = parseWord(startLetters + letter, word[index:])
        if len(temp) > len(stored):
            stored = temp
    return stored

def strippedText(text):
    newWord = ""
    for letter in str(text):
        if letter.upper() != letter.lower():
            newWord += letter
    return newWord

for line in textLines:
    word = parseWord("", strippedText(line.strip().lower()))
    print(f"\nOriginal Word: {line.strip()}\nEarliest Largest Alphabetical Word: {word}\nLength: {len(word)}")