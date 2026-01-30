'''
Question 2: Nested Dictionary from Strings

Define a function that receives a list of strings and returns a dictionary with the following struc-
ture:
    • Each key is a string from the list.
    • Each value is another dictionary containing:
        – The length of the string
        – Whether the length is even or odd
'''


# Declare list of inputs to match example expected output
listOfInputStrings = ['data','science']

# Start of written code
def stringListToStringDictionary(inputListOfStrings):
    dictionaryOfProcessedStrings = {}

    for word in inputListOfStrings:
        dictionaryOfProcessedStrings[word] = {'length':len(word), 'parity':'odd' if len(word) % 2 != 0 else 'even'}
        
    return dictionaryOfProcessedStrings

#Printout of results 
print(stringListToStringDictionary(listOfInputStrings))