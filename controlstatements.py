

x = 8

# if-elif control statements

if x == 5:
    print(x)
elif x > 5:
    print(7)
else:
    print(9)

a = ['Apple', 'Ball', 'Camera']

for word in a:
    print('Word', word, len(word))

for i in range(5):
    print('Range :', i)

def function_with_default(b, a = 5):
    return a + b


if __name__ == "__main__":
    print('Result of function : ', function_with_default(7))
