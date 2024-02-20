def palindrome(word):
    word = ''.join(e for e in word if e.isalnum())
    return word.lower() == word.lower()[::-1]

if __name__ == '__main__':
    print(palindrome("civic")) # True
    print(palindrome("katak")) # True
    print(palindrome("kasur rusak")) # True
    print(palindrome("kupu-kupu")) # False
    print(palindrome("lion")) # False