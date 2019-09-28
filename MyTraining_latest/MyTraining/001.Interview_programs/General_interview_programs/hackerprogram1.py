
Multiple_of_two = "FIZZ"
num1 = 2
Multipl_of_five = "BUZZ"
num2 = 5
number = raw_input()
for index in range(number):
    if index%num1 == 0 and index%num2 == 0:
        print Multiple_of_two,Multipl_of_five
    elif index%num1 == 0 == 0:
        print Multiple_of_two
    elif index%num2 == 0 == 0:
        print Multipl_of_five
    else:
        print index
    pass


