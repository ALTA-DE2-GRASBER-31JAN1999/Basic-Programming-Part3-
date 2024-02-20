def full_prima(N):
    if N < 2:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True
def prima(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def full_prima(N):
    if not prima(N):
        return False
    digits = str(N)
    for digit in digits:
        if not prima(int(digit)):
            return False
    return True

if __name__ == '__main__':
    print(full_prima(2))     # Output: True
    print(full_prima(3))     # Output: True
    print(full_prima(11))    # Output: False
    print(full_prima(13))    # Output: False
    print(full_prima(23))    # Output: True
    print(full_prima(29))    # Output: False
    print(full_prima(37))    # Output: True
    print(full_prima(41))    # Output: False
    print(full_prima(43))    # Output: False
    print(full_prima(53))    # Output: True