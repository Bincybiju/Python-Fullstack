num=int(input("Enter the number : "))
units=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
ones=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
tens=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
if num<10:
    print(units[num])
elif num<20:
    print(ones[num%10])
elif num<100:
    print(tens[num // 10]  +" " + units[num % 10])
elif num<1000:
    if num%100<10:
        print(units[num//100] +" hundred " + units[num%10])
    elif num%10<20:
        print(units[num//100] + " hundred "+ ones[num%10])
    elif num%10<100:
        print(units[num//100]+ " hundred "+tens[(num//10)%10]+units[num%10])
    
    







