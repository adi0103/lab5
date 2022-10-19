a=input().split()
p=a[-1]
for i in range(len(a)-2, -1, -1):
    a[i+1]=a[i]
a[0]=p
print(' '.join(a))
