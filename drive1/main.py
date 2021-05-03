num=[]
x=[]
d1={}
d={"name":"Clark",
    "age":19,
    }



a=input("enter the key")


if a=="cart":
            for i in range(4):
                g=input("enter the input for cart")
                h=int(input("enter the value"))
                d1[g]=h

            d["cart"]=d1
            print(d)
else:
        b = input("enter the values")



p=d["age"]
if int(p)  < 20:
    a = d["cart"]["Book"]
    b = d["cart"]["Sports Item"]
    d["cart"]["Book"] = a - a * 0.25
    d["cart"]["Sports Item"] = b - b * 0.25
c = d["cart"]["Electronics"]
d["cart"]["Electronics"] = c - c * 0.1
y = d["age"]

if  y is 20> y <40:
    x=d["cart"]["Home Suplies"]
    d["cart"]["Home Suplies"]=x-x*0.25
z=d["cart"]
num=[]
for i,j in z.items():
    num.append(j)
tc=sum(num)
print(tc)









