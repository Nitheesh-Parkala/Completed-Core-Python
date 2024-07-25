from itertools import zip_longest


name=["kohli","Rohit","ABD","Gayle"]

runs=[2400,1800,12000,1500]

country=["IND","IND","SA","WI"]

ipl_t=["RCB","MI","RCB","RCB"]


ipl_t=["RCB","MI",]  #output->[('kohli', 2400, 'IND', 'RCB'), ('Rohit', 1800, 'IND', 'MI')]

print([(name[0],runs[0],country[0],ipl_t[0]),
       (name[1],runs[1],country[1],ipl_t[1]),
       (name[2],runs[2],country[2],ipl_t[2]),
       (name[3],runs[3],country[3],ipl_t[3])
      ])

#2 approach using zip().
# k=list(zip(name,runs,country,ipl_t))
# print(k)


#3 approach using zip_longest()
# we have to import from itertools import zip_longest
res=list(zip_longest(name,runs,country,ipl_t))
print(res) #[('kohli', 2400, 'IND', 'RCB'), ('Rohit', 1800, 'IND', 'MI'), ('ABD', 12000, 'SA', None), ('Gayle', 1500, 'WI', None)]

res=list(zip_longest(name,runs,country,ipl_t,fillvalue="#"))
print(res) #[('kohli', 2400, 'IND', 'RCB'), ('Rohit', 1800, 'IND', 'MI'), ('ABD', 12000, 'SA', '#'), ('Gayle', 1500, 'WI', '#')]