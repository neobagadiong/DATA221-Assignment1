'''
Question 7: Time Conversion Function

Write a function that converts a given number of seconds since midnight into:
    • Hours
    • Minutes
    • Seconds
    • AM or PM
The function should return a formatted string. If the input is invalid, return an appropriate
message.
'''
def convertSecondsToTime(seconds):
    if type(seconds) is int:
        if seconds < 86400:
            return (f"{int(seconds/3600)%12} {int((seconds/60)%60)} {seconds%60} {'AM' if int(seconds/3600) < 12 else 'PM'}")
    return "Invalid input. Please input a valid integer that is less than 86400 seconds (a full day)."

print(convertSecondsToTime(36730))
print(convertSecondsToTime(567300))
print(convertSecondsToTime('56730'))