"""
This program demonstrates how to direct a user to a location based on their input
"""
print("Hello there!what is your name?")
name = input()
print(f"{name} where are you headed to, abakpa or emene?")
location = input()

if location.lower() == "abakpa":
    print(f"Alright{name}, once you step out from Aptech, you cross the road and flag down any keke going to holyghost. " \
    "when you get to holy ghost, you walk up to the loading point and enter any bus going to abakpa.")
else:
    if location.lower() == "emene":
        print(f"Alright {name}, once you come out from Aptech, you cross the road carefully and flag down any keke going to holyghost." \
        "when you get there, you walk up to the loading point and enter any bus going to emene.")
    else:
        print(f"Sorry {name}, your location is not recognized by the google map, kindly choose between abakpa and emene.")    