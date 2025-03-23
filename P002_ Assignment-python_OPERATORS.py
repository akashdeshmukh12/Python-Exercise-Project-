

###   -- >>  Practice || Exercise :_P02 -->>
#                             Exercise "Use of Operators in Python for different Operations"

#=======================================================================================================================


print("EXERCISE NO- 001: "
      "Take any two numbers and do different operations and find out results. \n")

number_01 = int(input("take any number you like for number_01 - "))
number_02 = int(input("take any number you like for number_02 - "))
#         - Input Function -used to take any two numbers...[two_digit number]

sum = (number_01 + number_02)
#         - Arithmatic Operator [addition- '+'] -used to addition of given two numbers, by user.
print(f"\n  total of given two numbers = {sum}")
#          - Print Function -used to print/display outputs of operation.

Divide= round((number_01 / number_02),2)
#           -  Arithmatic Operator[Division- '/' ] -used to division of given two numbers, by user.
print(f"  Division of given two numbers = {Divide} \n\n")
#          - Print Function -used to print/display outputs of operation.


#=======================================================================================================================

        ### Exercise 002  - to add digits of 'total' number [after addition of given two numbers].

print("EXERCISE NO- 002:  "
      "find total sum- by doing addition of digits on number you got, after adding two numbers you take from user. \n")

number_1 = int(input("take any number you like for number_01 - "))
number_2 = int(input("take any number you like for number_02 - "))
#    sum = total of given two numbers by user.

sum1 = (number_1 + number_2)

#   method 1- by applying while loop, inside if condition:

if sum1>1000:
    digit_sum = 0
    while sum1 > 0:
        digit_sum = digit_sum + sum1 % 10
        sum1 = sum1 // 10

    print(f"\n total addition of digits for Given two numbers are {digit_sum}")

#   method 2- by simply using if-else condition:

elif sum1>100:
    sum2=str(sum1)
    first_digit = sum2[0]
    second_digit = sum2[1]
    third_digit = sum2[2]

    Digit_sum2 = ((int(first_digit)) + (int(second_digit)) + (int(third_digit)))
    print(f"\n total addition of digits for Given two numbers are {Digit_sum2} ")

else:
    sum3=str (sum1)
    first_digit3 = sum3[0]
    second_digit3 = sum3[1]

    Digit_sum3 = ((int(first_digit3)) + (int(second_digit3)))
    print(f"\n total addition of digits for Given two numbers are {Digit_sum3}")


exit()