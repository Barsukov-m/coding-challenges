def evaluate(n1, n2, s):
    if s == '+':
        return int(n1) + int(n2)
    elif s == '-':
        return int(n1) - int(n2)
    elif s == '*':
        return int(n1) * int(n2)
    elif s == '/':
        return int(n1) / int(n2)

def solve():
    s = input()    
    # First result is formed by adding 0 to the first operand
    operand_1, operand_2 = '0', ''
    operator = '+'
    negative = 0 # Negative number state
    
    # Reading the entry data
    i = 0
    while s: # Entry data is not empty
        while True:
            if s[i].isdigit() or s[i] in ' +-*/':
                if s[i] == '+':
                    continue
                elif s[i] == '-':
                    # Inverse the negative number state
                    negative = not negative
                elif s[i].isdigit():
                    operand_2 += s[i]
                    i += 1
                    break
            i += 1
        
        while True:
            if i >= len(s):
                if negative:
                    operand_2 = '-' + operand_2
                operand_1 = evaluate(operand_1, operand_2, operator)
                print(operand_1)
                return
            if s[i].isdigit() or s[i] in ' +-*/':
                if s[i].isdigit():
                    operand_2 += s[i]
                elif s[i] in '+-*/':
                    if negative and s[i] != '-':
                        operand_2 = '-' + operand_2
                    operand_1 = evaluate(operand_1, operand_2, operator)
                    operator = s[i]
                    negative = 0
                    operand_2 = ''
                    i += 1
                    break
            i += 1
        if i >= len(s):
            print(operand_1)
            return

    print(operand_1)
    

def main():
    solve()


if __name__ == '__main__':
    main()