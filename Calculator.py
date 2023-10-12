print("*" * 10, "Calculator v1.0", "*" * 10)
while True:
    print("Press q to exit")
    s = input("Mark (+, -, *, /): ")
    if s == 'q': break
    if s in ('+', '-', '*', '/'):
        x = float(input('x = '))
        y = float(input('y = '))
        if s == '+':
            print('%.2f' % (x + y))
        elif s == '-':
            print('%.2f' % (x - y))
        elif s == '*':
            print('%.2f' % (x * y))
        elif s == '/':
            if y != 0:
                print('%.2f' % (x / y))
            else:
                print('Division by zero!')
    else:
        print('Wrong mark!')

