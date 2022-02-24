import random

# Weather Branch

def weather():
    weatherForecast = ["Icy","Snowy","Raining","Windy","Foggy","Sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

# Calling weather Function to determine weather
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "Icy":
        print("\nVRS Has Changed Your Alarm Based On The NWS",weatherAlert)
        print("\nVRS Will Only Allow Your Car To Go 30MPH")
    elif weatherAlert ==  "Snowy":
        print("\nVRS Has Changed Your Alarm Based On The NWS",weatherAlert)
        print("\nVRS Will Only Allow Your Car To Go 50MPH")
    elif weatherAlert == "Raining":
        print("\nVRS Has Changed Your Alarm Based On The NWS", weatherAlert)
        print("\nVRS Will Only Allow Your Car To Go 50MPH")
    elif weatherAlert == "Windy":
        print("\nVRS Has Changed Your Alarm Based On The NWS", weatherAlert)
        print("\nVRS Will Only Allow Your Car To Go 60MPH")
    elif weatherAlert == "Foggy":
        print("\nVRS Has Changed Your Alarm Based On The NWS", weatherAlert)
        print("\nVRS Will Only Allow Your Car To Go 50MPH")
    else:
        print("\n Your Vehicle May Go Max Speed")


vehicleResponseSystem()