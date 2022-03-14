#for number in [1,2,3,4]: #range(1,31):
 #   print(number)
a=int(input("What table do you want? :").strip())
b=int(input(" Upto what range? :").strip())
c=1
for c in range(1,b+1):
    d=a*c
    print(a ," * ", c , " = ",d)
