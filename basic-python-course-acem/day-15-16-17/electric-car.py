from coord import Coord
from car import Car


class ElectricCar(Car):
    
    def __init__(self, pos, brand, mileage, color, use_type, price, battery_cap):
        super().__init__(pos, brand, mileage, color, use_type, price)
        self.battery_cap = battery_cap
        self.charge = 100

    def get_info(self):
        """Information about the electric car object"""
        info_str = f"A {self.color} {self.use_type} {self.brand} with mileage {self.mileage} of battery capacity {self.battery_cap} costing {self.price} is at position {self.get_position()}"
        return info_str

    def get_charge(self):
        return str(self.charge) + '%'

    # def set_charge(self, charge):
    #     if charge >= 100:
    #         self.charge = 100
    #     elif charge < 0:
    #         self.charge = 0
    #     else:
    #         self.charge = charge

    __str__ = get_info

    def recharge(self):
        self.charge = 100

    def discharge(self, amount):
        self.charge -= amount

    def move_vert(self, dist, dir):
        super().move_vert(dist, dir)
        self.discharge(dist*0.001)


if __name__ == '__main__':
    gopals_tesla = ElectricCar(Coord(0,0), 'Tesla M S', '17KmpCH', 'black', 'commuter', 10000000, '4000AH')

    print(gopals_tesla)

    # print(gopals_tesla.get_position())

    # print(gopals_tesla.get_charge())
    # gopals_tesla.move_vert(10, 'up')
    # print(gopals_tesla.get_charge())
    
    # gopals_tesla.recharge()
    
    print(gopals_tesla.get_charge())
    print(gopals_tesla.charge)
    print(gopals_tesla.charge)
    print(gopals_tesla.get_charge())


    # print(gopals_tesla.get_position())



