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

for line in textLines:
    word = parseWord("", line.strip())
    print(f"\nOriginal Word: {line.strip()}\nLargest Special Word(s): {word}\nLength: {len(word)}")
