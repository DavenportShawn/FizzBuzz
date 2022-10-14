for x in range(1, 101):
    output = ''
    if x % 3 == 0:
        if x % 5 == 0:
            output = 'FizzBuzz'
        else:
            output = 'Fizz'
    elif x % 5 == 0:
        output = 'Buzz'
    else:
        output = x
    print(output)