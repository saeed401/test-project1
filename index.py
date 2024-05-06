vurudi=int(input(':'))
list1=[]
s=''
for i in range (vurudi):
    str=input(':')
    list1.append(str)

for str in  (list1):
    
    for d in range (len(str)):
        s=s+'*'
    print(s)
    s=''