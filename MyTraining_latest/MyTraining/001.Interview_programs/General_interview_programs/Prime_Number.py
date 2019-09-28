# Prime Number

# change the values of lower and upper for a different result
lower = 1
upper = 10

# uncomment the following lines to take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)


"""
sh-4.3$ python main.py
('Prime numbers between', 1, 'and', 10, 'are:')
2
3
5
7    
"""