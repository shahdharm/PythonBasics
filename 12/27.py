def mul (num):
    if num==1:
        return 3
    else:
        return 3+mul(num-1)
for i in range(1,11):
    print(mul(i))