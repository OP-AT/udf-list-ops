#for print list
def ls():
    for i in range(0,a):
        x= int(input("enter number here: "))
        l.append(x)
    return l 
l=[] 
a= int(input("how many elements you want to enter: "))
print("your enterd is: ", ls())


# sum
def sum():
    s=0 
    for b in l:
        s= s+b
    return s
#insert
def inst():
    c= int(input("neter the element  you want to insert: "))
    print("at which index do you want to enter ", c, ": ", end= " ")
    d= int(input(" "))
    l.insert(d,c)
    return l
#delete an elemnt
def dlt():
    e= int(input("enter the item you want to delete: "))
    l.remove(e)
    return l

#increase by some amount
def ins():
    f= int(input("by how much do you want to increase: "))
    for g in range(0,a):
        l[g] += f
    return l


print(" to print the sum of all elements press 1")
print(" to add an element at a certain index press 2")
print(" to remove an element press 3")
print(" to increase every element by some amount press 4 ")
print(" बाहर निकलने के लिए 5 दबाएं")
while 2>1:
    h= int(input("enter choice here: "))
    if h == 1:
        print(sum())
    elif h == 2:
        print(inst())
    elif h == 3:
        print(dlt())
    elif h == 4:
        print(ins())
    elif h == 5:
        print("good decision *_* ")
        break 