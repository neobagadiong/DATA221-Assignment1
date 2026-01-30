'''
Question 3: Safe Function Application

Define a function that computes x^y. Then, given a list of pairs (x, y):
    • Use a for loop with argument unpacking to call the function.
    • Skip any pair where the exponent y is negative.
    • Store the valid results in a list and print the list.
'''
# Example input list given
pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]

# Start of written code
def exponentCalcWithoutNegativeExponent(listOfPairs):
    listOfValidResults = []

    for pair in listOfPairs:
        if pair[1] >= 0: listOfValidResults.append(pair[0]**pair[1])  

    return listOfValidResults

# Printout of what function outputs when given the example input.
print(exponentCalcWithoutNegativeExponent(pairs))