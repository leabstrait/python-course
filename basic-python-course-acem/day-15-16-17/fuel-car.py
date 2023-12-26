from coord import Coord
from car import Car


class FuelCar(Car):
    
    def __init__(self, pos, brand, mileage, color, use_type, price, fuel_tank):
        super().__init__(pos, brand, mileage, color, use_type, price)
        self.fuel_tank = fuel_tank

    def get_info(self):
        """Information about the fuel car object"""
        info_str = f"A {self.color} {self.use_type} {self.brand} with mileage {self.mileage} of fuel tank capacity {self.fuel_tank} costing {self.price} is at position {self.get_position()}"
        return info_str

    __str__ = get_info

    def refuel(self):
        self.charge = 100

    def consume_fuel(self, amount):
        self.charge -= amount


if __name__ == '__main__':
    darshans_rollsroyce = FuelCar(Coord(0,0), 'Rolls Royce', '17KmpL', 'matte black', 'racing', 100000000, '40L')

    print(darshans_rollsroyce)

