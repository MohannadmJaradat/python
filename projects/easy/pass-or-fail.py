maths = int(input("Please enter your score in maths course: "))
chemistry = int(input("Please enter your score in chemistry course: "))
physics = int(input("Please enter your score in physics course: "))
while maths!=-1:
    if maths >= 45 and chemistry >= 45 and physics >= 45:
        print("Pass")
    else:
        print("Fail")
    maths = int(input("Please enter your score in maths course: "))
    chemistry = int(input("Please enter your score in chemistry course: "))
    physics = int(input("Please enter your score in physics course: "))