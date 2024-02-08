item=input("Enter the item : ")
price=float(input("Enter the price in dollars: "))
over=int(input("Overnight shipping is wanted (Enter 1 if yes and 0 if no)? "))
if price<10 and over==0:
    shipping=2
elif price<10 and over==1:
    shipping=7
elif price>10 and over==0:
    shipping=3
else:
    shipping=8
print(item,price)
print("shipping",shipping)
print("Total  ",price+shipping)
