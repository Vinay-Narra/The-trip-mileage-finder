print("welcome to the Trip Mileage Finder!")
print("Lets calculate your trip mileage")
print("------------------------------------------------------")

distance = float(input("Enter the distance travelled (in kilometers):"))
fuel_used = float(input("Enter the fuel used (in litres):"))
fuel_price = float(input("Enter the price of the fuel (per litre): "))

mileage = distance / fuel_used
total_cost = fuel_used * fuel_price
cost_per_km = total_cost / distance

print("/ntrip Summary:")
print("-----------------------------------------------------")
print("Distance Travelled:" , distance, "km")
print("Fuel Used:" , fuel_used, "litres")
print("Mileage:" , mileage, "km per litre")
print("Total Fuel Cost: ₹" , total_cost)
print("Average Cost per km: ₹" , cost_per_km)
print("-----------------------------------------------------")
print("Thank you for using the Trip Mileage Finder!")
