print ("caluculate fuel consumption")
distance = int(input("Enter travel distance(kilometers): "))
#distance is already integer, because of int in the first line
FuelUsage = int(input("Enter fuel usage(liters): "))
#FuelUsage is already integer
Consumption = distance / FuelUsage
print ("Fuel consumption is", Consumption, "l per 100 kilometers")