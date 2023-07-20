def sum_digits(digits):
    result = 0

    while digits:
        digit = digits % 10
        result += digit ** 2
        digits //= 10

    return result

    
def is_happy_number(n):
    slow = n
    fast = n
    while True:
        slow = sum_digits(slow)
        fast = sum_digits(sum_digits(fast))
        if fast == slow:
            if fast == 1:
                return True
            else:
                return False