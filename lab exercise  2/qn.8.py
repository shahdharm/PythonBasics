# Given a three-digit number. Find the sum of its digits.
num = int(input("enter the three digits number:"))
i = num%10
num1 = num//10
j = num%10
num2 = num//10
k = num%10
num3 = num//10
sum = i+j+k
print(sum)
