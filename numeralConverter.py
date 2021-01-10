def dec2bin(d):
    n, b = 1, 0
    while(d > 0):
        b += (d % 2) * n
        d //= 2
        n *= 10
    return b
# dec2bin


def bin2dec(b):
    b_sep = list(str(b))
    for digit in b_sep:
        if digit not in '01':
            return None
    d, i = 0, 0
    while(b > 0):
        d += (b % 10) * 2**i
        i += 1
        b //= 10
    return d
# bin2dec


def test():
    while True:
        try:
            program = int(input('Decimal to Binary (1)\nBinary to Decimal (2)\n: '))
            if str(program) not in '12':
                raise Exception
            d = int(input('Enter your number: '))
            break
        except Exception:
            print('Enter a valid number.')

    if program == 1:
        print(dec2bin(d))
    elif bin2dec(d) is None:
        print(d, 'is not a binary number.')
    else:
        print(bin2dec(d))


if __name__ == '__main__':
    test()