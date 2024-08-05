d={
    1:11,
    2:22,
    3:44,
    4:55
}

print(d)
print(type(d))

d1=d
d2=d.copy()

print(d[2])

d[2]=222
print(d[2])
print(d1[2])
print(d2[2])

del d[2]

print(d)
print(d1)
print(d2)