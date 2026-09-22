#Task 3.1

number = int(input("Enter de number: "))

if number % 2 == 0:
    print("even")
else:
    print("odd")

#Task 3.2
number = 123456789
digit_sum = sum(int(digit) for digit in str(number))

print(digit_sum)

number = 112233445566778899
digit_sum = sum(int(digit) for digit in str(number))

print(digit_sum)

number = 123456789 * 987654321
digit_sum = sum(int(digit) for digit in str(number))

print(digit_sum)

#Task 3.3
number1 = 12.24 
number2 = 424242.8412

prin(int(number1))
print(int(number2))

#Task 3.4
number1 = 12.24
number2 = 424242.8412

print(number1 - int(number1))
print(number2 - int(number2))
