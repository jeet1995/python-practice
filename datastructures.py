from collections import deque

def print_dictionaries():
    # dictionary
    dict_one = {'Abhijeet': 24, 'Subrata': 55}
    print(len(dict_one))
    print('Abhijeet age :', dict_one['Abhijeet'])
    print('Subrata age :', dict_one['Subrata'])

    # dictionary comprehension
    dict_comprehension = {x : x ** 2 for x in range(20)}
    print(dict_comprehension)

    for k, v in dict_comprehension.items():
        print('Pair : ', (k, v))


def print_sets():
    # set
    set_one = {'Ab', 'Ab', 'Cd'}
    print(set_one)
    print(len(set_one))

    set_two = set({'A', 'A', 'B'})
    print(set_two)

def print_matrices():
    # matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j])

def print_queues():
    # queue
    queue = deque(["Ab", "Cd", "De"])
    queue.append("Fe")
    b = queue.pop()
    print(b)

def print_lists():
    # basic list
    a = [1, 2, 5, 1, 4]
    a[len(a):] = [7]
    a[3] = 9
    print(a)

    # no side effects
    squares = [x ** 2 for x in range(10)]
    print(squares)

    # no side effects - lambda expressions
    squares_lambda = list(map(lambda x: x ** 2, range(10)))
    print(squares_lambda)

    squares_comprehension = list(map(lambda x: x ** 2, [1, 2, 5]))
    print(squares_comprehension)

    # enumeration
    for i, v in enumerate(squares_comprehension):
        print('Index, Val : ', (i, v))


def print_tuples():
    # creating list of tuples
    pairs = []
    for x in [1, 2, 3]:
        for y in [2, 4, 6]:
            pairs.append((x, y))
    print(pairs)



if __name__ == "__main__":
    print_dictionaries()
    print_lists()
    print_matrices()
    print_queues()
    print_sets()
    print_tuples()











