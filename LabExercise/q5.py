# A school decide to replace the desk in three classrooms.each desk sits two student.
# Give the number of the student in each class ,print the smallest possible number of desk that can be purchased.
#the program should read three integer the number of student in each of the three class a,b and c respectively

#in the first test three are three group. the first group has 20 students and thus needs 10 desk.the second group
#has 21 student so ,they can get by with no then 11 desks are else enough


no_student_class1=int(input("enter the number of student  in first class:"))
no_student_class2=int(input("enter the number of student in second class:"))
no_student_class3=int(input("neter the number of student in third class:"))
desk_class1=(no_student_class1//2)
print(f"the required number of desk for first class is {desk_class1}")
desk_class2=(no_student_class2//2)
print(f"the required number of desk required in second class is {desk_class2}")
desk_class3=(no_student_class3//2)
print(f"the required the number of desk required in third class is {desk_class3}")