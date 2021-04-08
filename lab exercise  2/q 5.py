# if name is less than 3 characters long-name is must be at least 3 characters otherwise if it's more than 50
# characters - name must be maximum of 50 characters otherwise - name looks good.


name = int(input("enter your user name:"))
if name < 3:
    print("the name must be 3 character:")
elif name > 50:
    print("the name must be 50 characters:")
else:
    print("the name looks good")
