a=5.08
b=5.33
c=5.55
d=b-a
e=c-b
if c>d:
  print("c>d")
elif c<d:
  print("c<d")
else:
    print("c=d")


X=True
Y=False
W=X or Y
#Truth Table for W
#|X    |Y    |W=X or Y|
#|True |True |True    |
#|True |False|True    |
#|False|True |True    |
#|False|False|False   |
print(W)

