#frozenset is an immutable version of a set.
x = frozenset({"apple", "banana"})
print(type(x)) #<class 'frozenset'>

fs = frozenset({1, 2, 3})
cp = fs.copy()
print(fs) #frozenset({1, 2, 3})
print(cp) #frozenset({1, 2, 3})

a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.difference(b)) #frozenset({1, 2})
print(a - b) #frozenset({1, 2})

a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.intersection(b))  #frozenset({3, 4})
print(a & b) #frozenset({3, 4}) 

a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(a.symmetric_difference(b))#frozenset({1, 2, 4, 5})
print(a ^ b)#frozenset({1, 2, 4, 5})

a = frozenset({1, 2})
b = frozenset({2, 3})
print(a.union(b))#frozenset({1, 2, 3})
print(a | b) #frozenset({1, 2, 3})

#Returns whether two frozensets have an intersection
a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))#True
print(a.isdisjoint(c)) #False

#Returns True if this frozenset is a (proper) subset of another
a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)#True
print(a < b)#True

#Returns True if this frozenset is a (proper) superset of another
a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b))#True
print(a >= b)#True
print(a > b)#True
