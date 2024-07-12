# base vehicle class
class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.__class__.__name__}({self.registration_number}, {self.make}, {self.model})"

# classes(car, truck, & motocycle)
class Car(Vehicle):
    def __init__(self, registration_number, make, model):
        super().__init__(registration_number, make, model) 

    def __str__(self):
        return f"Car({self.registration_number}, {self.make}, {self.model})"

class Truck(Vehicle):
    def __init__(self, registration_number, make, model):
        super().__init__(registration_number, make, model)       

    def __str__(self):
        return f"Truck({self.registration_number}, {self.make}, {self.model})"

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model):
        super().__init__(registration_number, make, model)        

    def __str__(self):
        return f"Motorcycle({self.registration_number}, {self.make}, {self.model})"

#fleet class
class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):     # add function
        self.vehicles.append(vehicle)

    def display_vehicles(self):         # disaplay function
        if not self.vehicles:
            print("No vehicles in the fleet.")
        else:
            for vehicle in self.vehicles:
                print(vehicle)

    def search_vehicle_by_registration(self, registration_number):      # search function
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                return vehicle
        return None

# using an instance of fleet to demonstrate functionalities
if __name__ == "__main__":
    # Create a fleet
    my_fleet = Fleet()

    # Add vehicles to the fleet
    car = Car("AFC133", "Tesla", "Model S")
    truck = Truck("AFF454", "Ford", "F-150")
    motorcycle = Motorcycle("GXT769", "Nduthi", "Boxer")

    my_fleet.add_vehicle(car)
    my_fleet.add_vehicle(truck)
    my_fleet.add_vehicle(motorcycle)

    # Display all vehicles
    print("All vehicles in the fleet:")
    my_fleet.display_vehicles()

    # Search for a vehicle by registration number
    reg_number = "AFF454"
    found_vehicle = my_fleet.search_vehicle_by_registration(reg_number)
    if found_vehicle:
        print(f"\nVehicle found: {found_vehicle}")
    else:
        print(f"\nNo vehicle found with registration number {reg_number}")
