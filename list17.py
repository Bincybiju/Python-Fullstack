t=int(input("Enter the temperature : "))
v=int(input("Enter the speed : "))
if 0<=v<=4:
    WCI=t
elif v>=45:
    WCI=1.6*t-45
else:
    WCI=91.4+(91.4-t)*(0.0203*v-0.304*(v)/2-0.474)
print("Wind chill index is " ,WCI)