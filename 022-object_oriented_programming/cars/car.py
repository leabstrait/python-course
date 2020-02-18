from coord import Coord

class Car(object):
    """A car class"""
    def __init__(self, pos, brand, mileage, color, use_type, price):
        self.pos = pos
        self.brand = brand
        self.mileage = mileage
        self.color = color
        self.use_type = use_type
        self.price = price

    def get_info(self):
        """Information about the car object"""
        info_str = f"A {self.color} {self.use_type} {self.brand} with mileage {self.mileage} costing {self.price} is at position {self.get_position()}"
        return info_str

    __str__ = get_info

    def get_position(self):
        return (self.pos)

    def move_vert(self, distance, direction=1):
        if direction == 1:
            self.position.y += distance
        elif direction == 0:
            self.position.y -= distance

    def move_horz(self, distance, direction=1):
        if direction == 1:
            self.position.x += distance
        elif direction == 0:
            self.position.x -= distance

if __name__ == '__main__':
    amans_hyundai = Car(Coord(0,0), 'Hyundai', '17KmpL', 'blue', 'commuter', 5000000)

    print(amans_hyundai.get_info())

    print(amans_hyundai)

    # print(amans_hyundai.__doc__)
    # print(amans_hyundai.get_info.__doc__)
