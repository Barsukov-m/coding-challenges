# 0 - 997000

def decToRoman(d):
    if d <= 0:
        return ""
    roman = ""
    if d >= 1000:
        return alpha[-1][1] + decToRoman(d-1000)
    i = 0
    while True:
        if alpha[i][0] <= d < alpha[i+1][0]:
            roman = alpha[i][1] + decToRoman(d-alpha[i][0])
            break
        i += 1
    return roman
alpha = [[0, ""], [1, "I"], [4, "IV"], [5, "V"], [9, "IX"],
         [10, "X"], [40, "XL"], [50, "L"], [90, "XC"],
         [100, "C"], [400, "CD"], [500, "D"], [900, "CM"],
         [1000, "M"]]


def test():
    while True:
        try:
            print(decToRoman(int(input())))
            break
        except TypeError:
            print('Enter a valid number.')


if __name__ == '__main__':
    test()  