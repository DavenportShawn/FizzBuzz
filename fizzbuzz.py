for x in range(100):
    output = ''
    num = x + 1
    if num % 3 == 0:
        if num % 5 == 0:
            output = 'FizzBuzz'
        else:
            output = 'Fizz'
    elif num % 5 == 0:
        output = 'Buzz'
    else:
        output = num
    print(output)