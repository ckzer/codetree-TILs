a=input()
a_list=list(a)
a_list[1]='a'
a_list[-2]='a'
for i in a_list:
    print(i, end='')