class AgeAdder:

    def __init__(self, age):
        self.age = age

    def __add__(self, other):
        return self.age + other.age


if __name__ == '__main__':
    # operator overloading
    print(1 + 2)
    print('a' + 'b')
    print([1, 2, 3] + [4, 5, 6])
    print('Added age :', AgeAdder(7) + AgeAdder(9))
