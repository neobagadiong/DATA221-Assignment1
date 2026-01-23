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
    
print(circleAreaCoverage(0,4))