class Car:

    # constructor
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def describe(self):
        print('The car is a', self.name)

    def move(self, direction):
        print('The class', self.__class__.__name__, 'is moving towards the', direction)


if __name__ == '__main__':
    car = Car('Jaguar', 2020)
    car.describe()
    car.move('left')
