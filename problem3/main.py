def prime_number(number):
    if number < 2:
        return "Not Prime"
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return "Not Prime"
    return "Prime"

if __name__ == '__main__':
    print(prime_number(11)) 
    print(prime_number(13)) 
    print(prime_number(17))  
    print(prime_number(20)) 
    print(prime_number(35))   