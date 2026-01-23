from random import random
values = [random() for i in range(20)]
x = random()
indicesOfValuesEqualOrGreaterThanX = []

values.sort()

for i in range(len(values)):
    if values[i] >= x: indicesOfValuesEqualOrGreaterThanX.append(i)

print(values, '\nx: ',x,indicesOfValuesEqualOrGreaterThanX[0])