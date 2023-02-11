import math
m,n,a= input().split()
x=math.ceil(int(m)/int(a))
y=math.ceil(int(n)/int(a))
num= x * y
print(num)