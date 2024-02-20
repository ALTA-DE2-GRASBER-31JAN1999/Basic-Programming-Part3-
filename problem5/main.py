def pangkat(base, pangkat):
    hasil = 1
    for _ in range(pangkat):
        hasil *= base
    return hasil

if __name__ == '__main__':
    print(pangkat(2, 3))     # Output: 8
    print(pangkat(5, 3))     # Output: 125
    print(pangkat(10, 2))    # Output: 100
    print(pangkat(2, 5))     # Output: 32
    print(pangkat(7, 3))     # Output: 343