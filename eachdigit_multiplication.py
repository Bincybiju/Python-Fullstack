num=int(input("Enter a number : "))
a=num%10
b=num//10
c=b%10
d=b//10
print("Multiplication table of ",d)
for i in range(1, 11):
   print(d, 'x', i, '=', d*i)

print("Multiplication table of ",c)
for i in range(1, 11):
   print(c, 'x', i, '=', c*i)

print("Multiplication table of ",a)
for i in range(1, 11):
   print(a, 'x', i, '=', a*i)

