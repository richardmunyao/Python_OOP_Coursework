class FooBar:
    def __init__(self, a=1, b=1) -> None:
        self.a = a
        self.b = b        

    def calculate(self):
        print(self.a * self.b)

if __name__ == '__main__':
    obj1 = FooBar(3,9)
    obj1.calculate()

# obj1 = FooBar(3,9)
# obj1.calculate()
