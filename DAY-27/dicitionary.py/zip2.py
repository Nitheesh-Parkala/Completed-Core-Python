eid=[101,102,103,104]
ename=["rama","sita","krishna","Bheema"]
esal=[9000,6000,70000,8000]
edesg=["SE","QA","FE","BA"]

emp_info=list(zip(ename,esal,edesg))

info1=dict(zip(eid,emp_info))
print(info1)