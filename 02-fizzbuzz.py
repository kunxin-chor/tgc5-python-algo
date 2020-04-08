"""
FIZZBUZZ

1. Print out the numbers 1 to 50
2. If the number is divisible by 3, print "Fizz" instead
3. If the number is divisible by 5, print "Buzz" instead
4. If the number is divisble by both 3 and 5, print "FizzBuzz" instead

OUTPUT : 1 to 20
1
2
Fizz
3
4
Buzz
6
Fizz
7
8
Fizz
10
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
"""
for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)