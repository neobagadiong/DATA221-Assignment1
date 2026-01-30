'''
Question 5: Circle Area Comparison with Validation

Write a function that takes the radii of two circles and performs the following:
    • Validates that both radii are positive integers.
    • Computes the area of each circle.
    • Returns the percentage of the larger circle’s area that can be covered by the smaller circle.
If invalid input is provided, return a meaningful message instead of performing the calculation.
'''
# Start of written code using example function signature
import math
def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    if int(radiusOfCircle1) >= 0 and int(radiusOfCircle2) >= 0:
        if radiusOfCircle1 <= radiusOfCircle2:
            circleCoveragePercent = ((2*math.pi*radiusOfCircle1)/(2*math.pi*radiusOfCircle2))*100 
        else:
            circleCoveragePercent = ((2*math.pi*radiusOfCircle2)/(2*math.pi*radiusOfCircle1))*100

        return f"The smaller circle covers {round(circleCoveragePercent)}% of the larger circle"
        
    else: 
        return "Please input positive integers only."

# Printout     
print(circleAreaCoverage(3,7))