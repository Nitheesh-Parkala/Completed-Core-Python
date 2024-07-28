a={10,20,30,40}
frozen=frozenset([10,20,30,40])
print(frozen) #immutable

frozen.add(21)    #error
frozen.remove(26) #error