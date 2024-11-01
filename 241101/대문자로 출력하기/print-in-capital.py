a=input()
a_alpha=[]

for i in range(len(a)):
    if a[i].isalpha():
        a_alpha.append(a[i])

for i in a_alpha:
    print(i.upper(), end='')