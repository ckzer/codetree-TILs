a=input()
order=input()

for i in order:
    if i=='L':
        a=a[1:]+a[0]
    else:
        a=a[-1]+a[:-1]
print(a)