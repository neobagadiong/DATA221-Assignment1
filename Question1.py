threshold = 1000
currentNumber = 1
product = 1

while product < threshold:
    currentNumber += 1
    product = product * currentNumber

print (product, ' with ', currentNumber, ' as last multiplication')