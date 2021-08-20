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

def fizz_buzz(max):
    result = []
    for i in range(max):
        if(i != 0):
            if(i % 4 == 0 or i % 6 == 0):
                if(i % 4 == 0 and i % 6 == 0):
                    continue   
                result.append(i)
    print(result)    

def average_of_three(num1, num2, num3):
    print((num1+num2+num3)//3)    

def goodbye(name):
    print("Good bye "+name)     


print('palindrome method here:')
is_palindrome("mummum")
print("\n")
print("doubler method here:")
list1 = [1, 2, 3, 4, 5]
doubler(list1)
print("\n")
print('fizz_buzz method here:')
fizz_buzz(20)
print("\n")
print("average_of_3 method here:")
average_of_three(13,14,15)
print("\n")
print('goodbye method here:')
goodbye('Nonny Mahao')