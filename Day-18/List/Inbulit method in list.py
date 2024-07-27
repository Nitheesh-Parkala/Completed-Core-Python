a=[10,20,30,40]
print(a)

a.insert(2,25)
print(a)

a.append(60)
a.append(70)
a.append(80)
print(a)

# a.append(90,100,110) # It will throw error because append can expect only one value.
b=[90,100,110]
a.extend(b)
print(a)

#extend method
a.extend([120,130,140])
print(a)
