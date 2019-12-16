import time
x = 0
sum=0
print(time.strftime('%H:%M:%S'))
while x<500000000:
    x+=1
    sum+=x
print(time.strftime('%H:%M:%S'))
print(sum)
