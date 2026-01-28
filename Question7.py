def convertSecondsToTime(seconds):
    if type(seconds) is int:
        if seconds < 86400:
            return (f"{int(seconds/3600)%12} {int((seconds/60)%60)} {seconds%60:.0f} {'AM' if int(seconds/3600) < 12 else 'PM'}")
    return "Invalid input. Please input a valid integer that is less than 86400 seconds (a full day)."

print(convertSecondsToTime(56730))
print(convertSecondsToTime(567300))
print(convertSecondsToTime('56730'))