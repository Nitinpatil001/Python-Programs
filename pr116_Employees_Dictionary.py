#Print Employees names Designation wise
dept=["computer","purchase","sales"]
design={"manager":1000,"clerk":8000,"peon":6000}
emp={"ram":"manager","sham":"clerk","seeta":"manager","geeta":"peon","anil":"clerk","sunil":"peon","jay":"clerk","vijay":"clerk"}
edept={"ram":"computer","sham":"computer","seeta":"sales","geeta":"sales","anil":"purchase","sunil":"purchase","jay":"computer","vijay":"sales"}
for i in design:
    print(i)
    for j in emp:
        if i==emp[j]:
            print("",j,edept[j])
            
