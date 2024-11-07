import math
################1. FELADAT


def bekeres():
    bekertszam = 0
    while not(bekertszam >= 200 and bekertszam <= 920):
        bekertszam = int(input("Kérlek adj meg egy egész számot 200 és 920 között: "))
    return bekertszam

def elsoIndex(bekertszam:str):
    bekertszam = str(bekertszam)
    print(f"{bekertszam[0]}")

################2. FELADAT


def bekeres2():
    ora = int(input("Kérlek adj meg egy egész óraszámot: "))
    return ora

def munkabirasi_ertek(ora):
    if ora < 1 or ora > 9:
        return "Ez már tényleg túlzás."
    
    if ora == 1:
        return "Még bírjuk (90%)."
    elif ora == 2 or ora == 3:
        return "Még bírjuk (60%)."
    elif ora == 4 or ora == 5 or ora == 6 or ora == 7:
        return "Még bírjuk (70%)."
    elif ora == 8 or ora == 9:
        return "Már kimerültünk (50%)."

def kiiras(munkabiras:str):
    print(munkabiras)


################4. FELADAT

def bekeres3():
    szam = 0
    while not(szam > 0):
        szam = int(input("Kérlek adj meg egy pozitív egész számot: "))
    return szam

def negyzetgyok_szamitas(szam:int):
    gyok = math.sqrt(szam)
    return szam, gyok

def kiiras2(szam:int, gyok:float):
    print(f"A {szam} négyzetgyöke: {gyok}")

################5. FELADAT

def bekeres4():
    a = int(input("Kérlek adj meg egy pozitív egész számot: "))
    b = int(input("Kérlek adj meg egy pozitív egész számot: "))
    return a,b

def teglalap_szamitas(a,b):       
    if a > 0 and b > 0:
        kerulet = 2 * (a + b)
        terulet = a * b
    else:
        bekeres4()
    return kerulet, terulet

def kiiras3(kerulet,terulet):
    print(f"A téglalap kerülete: {kerulet}, területe: {terulet}")


################9. FELADAT

def szorzotabla_kirajzolas():
    print("Szorzótábla:")
    for i in range(1, 11):
        for j in range(1, 11): 
            
            print(f"{i * j:5}", end=' ') 
        print() 




