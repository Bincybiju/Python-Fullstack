# using range

# for i in range(10):
#     print('hello world')
# for i in range(1):
#     print(i)

# for i in range(1,12,2): # generate the sequence -> 1,3,5,7,9,11
#     print(i)

a = "hello_worlds"
# length = len(a)
# for i in range(length):
#     print(a[i])

# for char in a:
#     print(char)




# a = "Hello_world"
# for i in a:
#     print(i)


# break
# for i in range(10):
#     if i == 5:
#         break
#     print("Have a great day times :",i)

# continue
# for i in range(10):
#     if i == 5:
#         continue
#     print("Have a wonderfull day times :", i)

# Else not working
# for i in range(10):
#     if i == 5 :
#         break
# else:
#     print("This for loop was succesfull")

# Else working
# for i in range(10):
#     if i == 5 :
#         print("It was 5")
# else:
#     print("This for loop was succesfull")


# Pass
# for i in range(10):
#     pass



# Patterns 
# *
# **
# ***
# ****
# *****

# a = "Hello"
# for i in a:
#     print(i, end="")

# for i in range(5):
#     for j in range(i):
#         print("*", end="")
#     print()


for i in range(1,5):
    for j in range(i):
        print("*", end=" ")
    print()