def _sum_of_square_digits(n: int) -> int:
    total = 0
    while n:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total


def checkmap(n: int) -> bool:
    slow = n
    fast = _sum_of_square_digits(n)

    while fast != 1 and slow != fast:
        slow = _sum_of_square_digits(slow)
        fast = _sum_of_square_digits(_sum_of_square_digits(fast))

    return fast == 1

