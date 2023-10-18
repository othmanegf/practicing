t1=[]
t=[]
s=0
n=int(input("Type the number of students :"))
for i in range (0,n) :
    m=int(input("Type the note:"))
    break
while m<0 or m>20 :
       m=int(input("Type a note between 0 and 20: "))
       t1.append(m)
       s=s+m
       e=s/n
       for i in range (0,n) :
        if t1[i]>e :
         t.append(t1[i])
print("Grades above averge are :",t)