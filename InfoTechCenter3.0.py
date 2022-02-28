# Code Name - Hornet
#Print to one line w/ time delay between prints
from time import sleep
import colorama
from colorama import Fore, Back, Style
colorama.init(strip=False, autoreset=True)
import random

# Welcome Branch

print(Fore.RED + "Welcome to Hornets InfoTechCenter\n")
sleep(1.0)

print(Fore.RED +"Hornet's Operating System Booting Up\n")
sleep(1.0)

# Gas Branch

# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

gasLevelIndicator = gasLevelGauge()

# Create If-ELIF-ELSE statements the Comparative Operator == Equal To in order to display gas level messages
def gasLevelAlert():
    gasStations = ["Shell","BP","Citgo","Circle K","Mobil","Speedway","Marathon","Love's","Meijer","Costco","Sunoco"]
    miles = round(random.uniform(1, 25), 2)
    if gasLevelIndicator == "Empty":
        print("   WARNING YOU ARE ON EMPTY\n Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("      WARNING\n Your gas tank is low on gas\n The closest gasoline station is " + random.choice(gasStations) + " which is " + str(miles) + " miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print("     You have a quarter tank of gas left\n The closest gasoline station is " + random.choice(gasStations) + " which is " + str(miles) + " miles away")

    elif gasLevelIndicator == "Half Tank":
        print("     You have a Half tank of gas left\n You have 126 miles to empty")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("     You have Three quarter tank of gas left\n You have 210 miles to empty")
    else:
     print("     You be FULL of Gas \n You have 310 miles to empty")



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

# Call Functions Here
gasLevelAlert()
sleep(1)
vehicleResponseSystem()

