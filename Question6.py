numbers = [3, 1, 2, 3, 4, 2]
def distributionAnalysisOfNumberList(listOfNumbers):
    listOfNumbers.sort()
    distributionAnalysisDictionary = {}
    for i in range(len(listOfNumbers)):
        distributionAnalysisDictionary[listOfNumbers[i]] = f"{round((i+1)/len(listOfNumbers)*100,2)}%"
    return distributionAnalysisDictionary

print(distributionAnalysisOfNumberList(numbers))
