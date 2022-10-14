for val in range(1, 101):
    output = ''
    if val % 3 == 0:
        if val % 5 == 0:
            output = 'FizzBuzz'
        else:
            output = 'Fizz'
    elif val % 5 == 0:
        output = 'Buzz'
    else:
        output = val
    print(output)