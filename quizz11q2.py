__author__ = 'Eutimio'
def check_banana(x):
    f=open("banana.txt")
    cont=0
    for i in f:
     a=i.lower() #convert the capital letters to minus
     b=a.find("banana")
     while(b!= -1):
          cont=cont+1
           b=low.fin("banana",( b+1))
    return cont
feb=check_banana(x)
print(feb)