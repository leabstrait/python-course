from coord import Coordinate

class Car(object):
    
    car_type = ('offroad', 'race', 'normal')

    def __init__(self, owner, brand, position, car_type):
        self.owner = owner
        self.brand = brand
        self.position = position
        self.car_type = Car.car_type.index(car_type)

    def get_position(self):
        return self.position.x, self.position.y

    def move(self, distance, direction=1):
        if direction == 1:
            self.position.y += distance
        elif direction == 0:
            self.position.y -= distance

    def move_side(self, distance, direction=1):
        if direction == 1:
            self.position.x += distance
        elif direction == 0:
            self.position.x -= distance

    def __str__(self):
        info_string = f"{self.owner}'s {self.brand} is a\
            {Car.car_type[self.car_type]} car.\
                \nIt is located at ({self.position.x}, {self.position.y})\
                in the world coordinate"
        return(info_string)

class ElectricCar(Car):
    
    def __init__(self, owner, brand, position, car_type, battery_capacity):
        super().__init__(owner, brand, position, car_type)
        self.battery_capacity = battery_capacity

    def move(self, distance, direction=1):
        self.discharge(0.1)
        return super().move(distance, direction=direction)

    # # charge
    def discharge(self, amount):
        self.battery_capacity -= amount

    def __str__(self):
        parent_info = super().__str__()
        elecro_info = self.battery_capacity
        return parent_info + f"\nIt has {elecro_info} battery right now"

class FuelCar(Car):
    # fuel_capacity 

    # refuel
    # consume_fuel
    pass

arun_ko_hyundai = ElectricCar('Arun', 'Hyundai', Coordinate(0,0), 'normal', 45)
arun_ko_hyundai.move(1)

print(arun_ko_hyundai)