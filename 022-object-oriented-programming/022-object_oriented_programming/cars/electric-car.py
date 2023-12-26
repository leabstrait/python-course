from coord import Coord
from car import Car


class ElectricCar(Car):
    
    def __init__(self, pos, brand, mileage, color, use_type, price, battery_cap, charge):
        super().__init__(pos, brand, mileage, color, use_type, price)
        self.battery_cap = battery_cap
        self.charge = charge

    def get_info(self):
        """Information about the electric car object"""
        info_str = f"A {self.color} {self.use_type} {self.brand} with mileage {self.mileage} of battery capacity {self.battery_cap} costing {self.price} is at position {self.get_position()}"
        return info_str

    __str__ = get_info

    def recharge(self):
        self.charge = 100

    def discharge(self, amount):
        self.charge -= amount


if __name__ == '__main__':
    gopals_tesla = ElectricCar(Coord(0,0), 'Tesla M S', '17KmpCH', 'black', 'commuter', 10000000, '4000AH', 100)

    print(gopals_tesla)

