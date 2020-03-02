from coord import Coord

class Car():
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

    def move_vert(self, dist, dir):
        if dir == 'up':
            self.pos.y += dist
        elif dir == 'down':
            self.pos.y -= dist

    def move_horz(self, dist, dir):
        if dir == 'right':
            self.pos.x += dist
        elif dir == 'left':
            self.pos.x -= dist


if __name__ == '__main__':
    amans_hyundai = Car(Coord(0,0), 'Hyundai', '17KmpL', 'blue', 'commuter', 5000000)

    # print(amans_hyundai.get_info())

    print(amans_hyundai)

    # print(amans_hyundai.__doc__)
    # print(amans_hyundai.get_info.__doc__)

    print(amans_hyundai.get_position())
    print(amans_hyundai.pos.y)
    amans_hyundai.move_vert(10, 'up')
    print(amans_hyundai.pos.y)
    print(amans_hyundai.get_position())



