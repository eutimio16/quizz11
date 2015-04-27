__author__ = 'Eutimio'
f=open("bananas.txt")
cont=0
for line in f:
    index=line.find("banana")
    if(index!=-1):
        print("found a banana on line", index)
        cont= cont +1

print("found", cont, "bananas")