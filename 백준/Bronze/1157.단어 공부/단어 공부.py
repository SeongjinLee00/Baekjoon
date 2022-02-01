s=input()
s=s.lower()

list1=[]
for i in range(97,123):
    list1.append(s.count(chr(i)))

count=0
for k in range(len(list1)):
    if list1[k]==max(list1):
        count=count+1

if count>=2:
    print('?')

else:
    for j in range(len(list1)):
        if list1[j]==max(list1):
            print(chr(j+97).upper())
            break