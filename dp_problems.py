# set of common problems of dynamic programming

from timeit import timeit


def fib_memo(n, memo={}):
    """
    Fibonacci: memoization approach for nonnegative
    number n limited by the recursion depth.
    """
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:  # base case
        return 1
    memo[n] = fib_memo(n-2, memo) + fib_memo(n-1, memo)
    return memo[n]


def fib_bottom_up1(n):
    """
    Fibonacci: bottom-up approach.
    """
    if n == 0 or n == 1:  # base case
        return 1
    a = 1  # n-2
    b = 1  # n-1
    for i in range(2, n+1):
        n = a+b
        a, b = b, n
    return n


def fib_bottom_up2(n):
    """
    Fibonacci: bottom-up approach using list.
    """
    fib = [None]*(n+1)
    fib[0], fib[1] = 1, 1
    for i in range(2, n+1):
        fib[i] = fib[i-2] + fib[i-1]
    return fib[n]


def path_search_memo(m, n, memo={}):
    """
    Path traveller problem.
    """
    if m == 1 and n == 1:  # base case 1
        return 1
    if m == 0 or n == 0:  # base case 2
        return 0
    key = str(m) + ',' + str(n)

    if key in memo:
        return memo[key]

    memo[key] = path_search_memo(m-1, n, memo) +\
        path_search_memo(m, n-1, memo)
    return memo[key]


def can_sum(target_sum, numbers, memo={}):
    """
    This function returns True when the numbers
    of an array add up the target_sum.
    """
    if target_sum == 0:  # base case
        return True
    if target_sum < 0:
        return False
    if target_sum in memo:
        return memo[target_sum]
    for n in numbers:
        if can_sum(target_sum - n, numbers, memo):
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False


def how_sum(target_sum, numbers, memo={}):
    """
    This function returns any combination of the numbers
    of an array that add up the target sum.
    """
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum > 0:
        for n in numbers:
            result = how_sum(target_sum - n, numbers, memo)
            if result is not None:
                return [n]+result
    memo[target_sum] = None


def best_sum(target_sum, numbers, memo={}):
    """
    This function returns any of the shortest combinations
    of the numbers of an array that add up the target sum.
    """
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return

    shortest = None
    for n in numbers:
        S = best_sum(target_sum - n, numbers, memo)
        if S is not None:
            S = [n]+S
            if shortest and len(S) < len(shortest):
                shortest = S
            elif not shortest:
                shortest = S
    memo[target_sum] = shortest
    return shortest


if __name__ == '__main__':
    # print(fib_bottom_up1(30))  # 7
    # print(path_search_memo(32, 32))
    # print(can_sum(777, [2, 3, 5]))
    # print(how_sum(7, [5, 3, 4, 7]))
    # print(how_sum(8, [2, 3, 5]))
    # print(how_sum(8, [3, 5]))
    # print(how_sum(300, [7, 14]))
    # print(best_sum(7, [5, 3, 4, 7]))
    # print(best_sum(100, [1, 2, 5, 25]))
    # print(best_sum(300, [7, 14]))
    pass
