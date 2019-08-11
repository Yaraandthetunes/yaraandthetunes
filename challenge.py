num=float(input("Digit a number, please "))
string=[" "," " ," "]
nmb=(3,5,7)
ans=""
for i in range (len(string)):
    if num % nmb[i]==0 and i==0:
        string[i]="Pling"
    if num % nmb[i]==0 and i==1:
        string[i]="Plang"
    if num % nmb[i]==0 and i==2:
        string[i]="Plong"
for i in range (len(string)):
    if string[i]!= " ":
        ans = ans + string[i] 

if ans != "":
    print(ans)
else:
    print (num)



        

