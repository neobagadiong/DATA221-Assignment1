listOfStrings = ['data','science']

def stringListToStringDictionary(inputListOfStrings):
    dictionaryOfProcessedStrings = {}
    for word in inputListOfStrings:
        dictionaryOfProcessedStrings[word] = {'length':len(word),'parity':'odd' if len(word) % 2 != 0 else 'even'}
    return dictionaryOfProcessedStrings
    
print(stringListToStringDictionary(listOfStrings))