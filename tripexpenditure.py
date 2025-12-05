def prc():
    print("Choose your destination: Los Angeles, Tampa, Washington DC, or New York")
    destination=input("Enter your destination: ")
    if destination == "Los Angeles":
        airfare= 280
        return airfare
    elif destination== "Tampa":
        airfare= 250
        return airfare
    elif destination == "Washington DC":
        airfare= 300
        return airfare
    else:
        airfare= 350
        return airfare

def hc():
    nights=int(input("Enter the number of nights you wish to stay: "))
    cost=40*nights
    return cost

def cr():
    days=int(input("Enter the number of days for which you would like to rent a car: "))
    cost1=30*days
    return cost1

def tc():
    
    return prc()+hc()+cr()

print("The total cost of the whole trip is " , tc())

