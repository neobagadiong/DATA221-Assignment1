pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
def exponentCalcWithoutNegativeExponent(listOfPairs):
    listOfValidResults = []

    for pair in listOfPairs:
        if pair[1] >= 0: listOfValidResults.append(pair[0]**pair[1])  

    return listOfValidResults


print(exponentCalcWithoutNegativeExponent(pairs))