class ComplexNum():

    def __init__(self, real, img):
        self.real  = real
        self.img = img

    def __str__(self):
        if self.img < 0:
            return f"{self.real} - {-self.img}i"
        elif self.img >= 0:
            return f"{self.real} + {self.img}i"

    def __add__(self, other):
        out_real = self.real + other.real
        out_img = self.img + other.img
        # return f"{out_real} + {out_img}i"
        return ComplexNum(out_real, out_img)

    def __sub__(self, other):
        out_real = self.real - other.real
        out_img = self.img - other.img
        return ComplexNum(out_real, out_img)

    def __mul__(self, other):
        out_real = self.real*other.real - self.img*other.img
        out_img = self.img*other.real + self.real*other.img
        return ComplexNum(out_real, out_img)

    def __eq__(self, other):
        return self.real == other.real and self.img == other.img

c1 = ComplexNum(4,5)
c2 = ComplexNum(-7, 3)


c3 = c1 + c2

c4 = c3 + c1

print(c4)

c6 = c1 * c2

print(c6)


c5 = ComplexNum(4,5)

print(c1 == c5)
print(c2 == c5)