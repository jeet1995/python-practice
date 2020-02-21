if __name__ == '__main__':
    print(str(7 / 5))  # returns the string version of the input

    dict_one = {'Abhijeet': 24, 'Hishimoto': 44}

    # formatted string literals
    # there will be a minimum of 10 spaces after k and after v
    for k, v in dict_one.items():
        print(f'{k:10}->{v:10}')

