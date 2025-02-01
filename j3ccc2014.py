ant=100
dvd=100

n=int(input())

for i in range(0,n):
    j=input()
    k=j.split(" ")
    a=int(k[0])
    d=int(k[1])

    if a > d: dvd = dvd - a
    if a < d: ant = ant - d

print(ant)
print(dvd)
