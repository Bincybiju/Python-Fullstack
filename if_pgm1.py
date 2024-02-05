w=int(input("Enter the number of working days : "))
ab=int(input("Enter the number of absent days : "))
per=(w-ab/w)*100
if per>75:
    print("student will be able to sit in exam")
else:
     print("student will not be able to sit in exam")