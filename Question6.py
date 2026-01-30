'''
Question 6: Distribution Analysis

Define a function that receives a list of numbers and returns a dictionary where:
    • Each key is a unique value from the list.
    • Each value is the percentage of elements in the list that are less than or equal to that key.

The resulting dictionary should be sorted by key before being returned
'''

# Example input provided
numbers = [3, 1, 2, 3, 4, 2]

# Start of written code
def distributionAnalysisOfNumberList(listOfNumbers):

    listOfNumbers.sort()
    distributionAnalysisDictionary = {}

    for i in range(len(listOfNumbers)):
        distributionAnalysisDictionary[listOfNumbers[i]] = f"{round((i+1)/len(listOfNumbers)*100,2)}%"

    return distributionAnalysisDictionary

print(distributionAnalysisOfNumberList(numbers))
