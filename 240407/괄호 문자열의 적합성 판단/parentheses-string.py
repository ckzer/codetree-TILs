li=[]
answer='Yes'
n=input()
for i in n:
    if i=='(':
        li.append(i)
    else:
        if not li:
            answer='No'
            break
        else:
            li.pop()
if li:
    answer='No'
print(answer)