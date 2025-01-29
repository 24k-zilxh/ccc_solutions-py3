adj=int(input())
nou=int(input())
adjs=[]
nns=[]
for i in range(0,adj): # enter adjectives
    adjs.append(input())
for i in range(0,nou):
    nns.append(input())

for x in range (0,len(adjs)):
    for y in nns:
        print(f'{adjs[x]} as {y}')

# This works. Solved on 01/20/2025