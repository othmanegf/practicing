t1=[]
t2=[]
T=[]
n=int(input("Type size n of both tables:"))
for i in range (0,n) :
    m=int(input("Type the number for table 1:"))
    t1.append(m)
    for i in range (0,n) :
     p=int(input("Type the number for table 2:"))
     t2.append(p)
     for i in range (0,n) :
      s = t1[i] + t2[i]
      T.append(s)
print("The sum of tables T1 and T2",T)