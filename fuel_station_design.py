class FuelStation:
    def __init__(self, diesel: int, petrol: int, electric: int):
        self.spots = {
            "diesel": diesel,
            "petrol": petrol,
            "electric": electric
        }
        self.occupied = {
            "diesel": 0,
            "petrol": 0,
            "electric": 0
        }

    def fuel_vehicle(self, fuel_type: str):
        if self.occupied[fuel_type] < self.spots[fuel_type]:
            self.occupied[fuel_type] += 1
            return True, f"{self.spots[fuel_type] - self.occupied[fuel_type]} slots now open"
        return False, f"{self.spots[fuel_type] - self.occupied[fuel_type]} slots now open"

    def open_fuel_slot(self, fuel_type: str) -> bool:
        if self.occupied[fuel_type] > 0:
            self.occupied[fuel_type] -= 1
            return True, f"{self.spots[fuel_type] - self.occupied[fuel_type]} slots now open"
        return False, f"Only {self.spots[fuel_type] - self.occupied[fuel_type]} slot available at fuel station" if fuel_type == 'electric' else f"0 slots available for {fuel_type}"

# Test the implementation
fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.fuel_vehicle("petrol"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.fuel_vehicle("electric"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.open_fuel_slot("diesel"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.open_fuel_slot("electric"))
print(fuel_station.open_fuel_slot("electric"))
