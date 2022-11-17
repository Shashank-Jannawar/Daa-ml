item=[10,20,30]
profit=[60,100,120]

c=120

arr=[]
for i in range(0,len(item)):
    it=item[i]
    pt=profit[i]
    pkg=pt/it
    arr.append([it,pt,pkg])

arr.sort(key=lambda x:x[2])
arr=arr[::-1]

i=0
profit=0
while(c>0):
    if arr[i][0]<=c:
        c=c-arr[i][0] #positive
        profit+=arr[i][1]
    else:
        profit+=c*arr[i][2]
        c=0
    i+=1

print(profit)
