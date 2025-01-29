avl= int(input()) # total amount of minutes that someone has to do chores
chn= int(input()) # total number of chores to choose from
chrlst=[]
for x in range(0,chn):
    chrlst.append(int(input()))
chrlst.sort()

ttl=0 # total amount of minutes added

for i in range(0,len(chrlst)):
    if (ttl + chrlst[i]) > avl:
        print(i)
        break
    ttl=ttl+chrlst[i]

# This works. Solved on 01/21/2025
