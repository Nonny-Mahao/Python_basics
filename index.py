def is_palindrome(word):
    rev = word[::-1]
    if(word  == rev):
        print(True)
    else:
        print(False)

def doubler(numbers):
    multiply = []
    for i in range(len(numbers)):
        multiply.append(numbers[i]*2)
    print(multiply)