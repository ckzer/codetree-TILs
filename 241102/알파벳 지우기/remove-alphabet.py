a=input()
b=input()

a_num=[]
b_num=[]
a_num_=0
b_num_=0

for i in a:
    if '0'<=i<='9':
        a_num.append(int(i))
for i in b:
    if '0'<=i<='9':
        b_num.append(int(i))

cnt=len(a_num)-1
for i in a_num:
    a_num_+=i*(10**cnt)
    cnt-=1

cnt=len(b_num)-1
for i in b_num:
    b_num_+=i*(10**cnt)
    cnt-=1

print(a_num_+b_num_)