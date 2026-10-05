
print ("1 for Volume " "\n" "2 for ractangle" "\n" "3 for triangle" "\n" "4 for trapezoid")
choice =int(input("Inter your choice: "))

    
if (choice==1):
    r=float(input("Inter a  radius: "))
    h=float(input("Inter  height: "))

    def volu(r,h):
        pi=22/7
        vol= pi*r**h
        return vol
    choice_1=volu(r,h)
    print(choice_1)    
    exit()   


elif (choice==2):
    
    l=float(input("Inter a  length: "))
    w=float(input("Inter  width: "))

    def size_ractangle(l,w):
        ractangle= l*w
        return ractangle
    choice_2= size_ractangle(l,w)
    print(choice_2)    
    exit()  

elif (choice==3):
    
    b=float(input("Inter a  base: "))
    h=float(input("Inter  height: "))

    def area_triagle(b,h):
        triagle= (b*h)/2
        return triagle
    choice_3= area_triagle(b,h)
    print(choice_3)    
    exit()  
    
elif (choice==4):
    
    b=float(input("Inter a  base: "))
    h=float(input("Inter  height: "))

    def area_trapezoid(b,h):
        trapezoid=1/2*(b+b)*h
        return trapezoid
    choice_4= area_trapezoid(b,h)
    print(choice_4)    
    exit()  
    
else:
    print("out of choice")

