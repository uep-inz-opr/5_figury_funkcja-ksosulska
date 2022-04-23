import math
pi=math.pi
sq=math.sqrt 

def oblicz_pole(a):
    if len(a)==1:
        p =pi*a[0]**2
    elif len(a)==2:
        p = a[0]*a[1]
    elif len(a)==3:
        b = ((a[0]+a[1]+a[2])/2)
        p = sq(b*(b-a[0])*(b-a[1])*(b-a[2]))
    else:
        return "Błąd: można podać maksymalnie 3 liczby"
    return round(p,2)

pole=0
liczba_figur = int(input())
for i in range(liczba_figur):
    figura = input().split()
    for j in range(len(figura)):
        figura[j]=float(figura[j])

    p_funkcji = oblicz_pole(figura)
    if type(p_funkcji) is not float:
        pole=p_funkcji
        break
    p_funkcji = oblicz_pole(figura)
    pole = pole+p_funkcji
    pole = round(pole, 2)
print(pole)