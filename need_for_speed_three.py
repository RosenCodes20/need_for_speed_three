number_of_cars = int(input())
cars_dict = {}
for cars in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    mileage, fuel = int(mileage), int(fuel)
    if car not in cars_dict:
        cars_dict[car] = {"Mileage": mileage, "Fuel": fuel}

command = input()

while command != "Stop":
    current_command = command.split(" : ")
    if current_command[0] == "Drive":
        car, distance, fuel = current_command[1], int(current_command[2]), int(current_command[3])
        if fuel > cars_dict[car]["Fuel"]:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car]["Mileage"] += distance
            cars_dict[car]["Fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars_dict[car]["Mileage"] >= 100_000:
            cars_dict.pop(car)
            print(f"Time to sell the {car}!")
    elif current_command[0] == "Refuel":
        max_fuel = 75
        car, fuel = current_command[1], int(current_command[2])
        fuel_to_add = max_fuel - cars_dict[car]["Fuel"]
        min_fuel = min(fuel, fuel_to_add)
        cars_dict[car]["Fuel"] += min_fuel
        print(f"{car} refueled with {min_fuel} liters")

    elif current_command[0] == "Revert":
        car, kilometers = current_command[1], int(current_command[2])
        cars_dict[car]["Mileage"] -= kilometers
        if cars_dict[car]["Mileage"] < 10_000:
            cars_dict[car]["Mileage"] = 10_000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input()

for car, mileage_fuel in cars_dict.items():
    print(f"{car} -> Mileage: {mileage_fuel['Mileage']} kms, Fuel in the tank: {mileage_fuel['Fuel']} lt.")
