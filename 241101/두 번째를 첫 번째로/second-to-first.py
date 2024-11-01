a=input()
a_list=list(a)
first=a_list[0]
second=a_list[1]
for i in range(len(a_list)):
    if a_list[i]==second:
        a_list[i]=first
for i in a_list:
    print(i, end='')