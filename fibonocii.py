#code for fibonacci numbers
n1=0
n2=1
count = 0
nterms=int(input("Enter how many terms :"))
if nterms<=0:
    print("Enter a positive interger :")
else:
    while(count<nterms):
       print(n1)
       nth=n1+n2
       n1=n2
       n2=nth
       count+=1
    
    
