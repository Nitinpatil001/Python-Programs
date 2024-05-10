#Print Employees names Dept wise
dept=["computer","purchase","sales"]
design={"manager":1000,"clerk":8000,"peon":6000}
emp={"ram":"manager","sham":"clerk","seeta":"manager","geeta":"peon","anil":"clerk","sunil":"peon","jay":"clerk","vijay":"clerk"}
edept={"ram":"computer","sham":"computer","seeta":"sales","geeta":"sales","anil":"purchase","sunil":"purchase","jay":"computer","vijay":"sales"}
for i in dept:
    print(i)
    for j in edept:
        if i==edept[j]:
            print("",j)
            
