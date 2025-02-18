l=input()
m=input()

l=l.lower()
m=m.lower()

m=list(m)
l=list(l)

for x in m:
    if x == ' ': m.remove(x)
for u in l:
    if u == ' ': l.remove(u)

l.sort()
m.sort()

if m == l: print("Is an anagram.")
else: print('Is not an anagram.')
