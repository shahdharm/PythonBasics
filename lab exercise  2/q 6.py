# weight converter:
# input the weight of a person in either kg or lbs.if person provides his/her weight in kg then convert it into
# lbs else convert it to kg.


user_weight = float(input("please enter your weight:\n"))
user_choice = input("choose if u want to convertn it into kg or lbs\n")
if(user_choice == "kg"):
    print(f"the weight in lbs is {user_weight*2.20462262}")
elif(user_choice=="lbs"):
    print(f"the weight in kg is {user_weight*0.45359237}")
else:
    print("it is not recongized")