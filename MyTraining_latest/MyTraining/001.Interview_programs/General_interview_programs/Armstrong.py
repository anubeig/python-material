#Armstrong number
num = int(input("Enter a number: "))

# Changed num variable to string,
# and calculated the length (number of digits)
order = len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   print(digit)
   sum += digit ** order
   print(sum)
   temp = temp // 10
   print(temp)

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")