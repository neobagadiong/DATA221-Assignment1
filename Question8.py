'''
Question 8: Pandas DataFrame with Computed 

Install the pandas package and import it using the alias pd. Then:
    • Create a DataFrame using the provided column data.
    • Add a new column derived from existing columns.
    • Print the final DataFrame.
'''

# Starter code
import pandas as pd

data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

# Start of written code
dataframeFromDictionary = pd.DataFrame(data)
dataframeFromDictionary["C*(B^A)"] = dataframeFromDictionary["C"] * (dataframeFromDictionary["B"] ** dataframeFromDictionary["A"])

print(dataframeFromDictionary)