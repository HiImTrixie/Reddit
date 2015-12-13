def three(number):
    while number != 1:
        if number % 3 == 0:
            print number, 0
        elif number % 3 == 1:
            print number, -1
            number -= 1
        elif number % 3 == 2:
            print number, 1
            number += 1
        number /= 3
    else:
        print number

three(31337357)