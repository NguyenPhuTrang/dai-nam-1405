import math
a= int(input("Nhap a :"))
def songuyento(a):
    b=0
    for i in range(1,a+1):
        if a%i==0:
            b=b+1
    if b==2:
        return("a la so nguyen to")
        return("a khong la so nguyen to")
print(songuyento(a))