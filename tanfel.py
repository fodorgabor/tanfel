# tantargyFelosztas=[]

# with open ("./beosztas.txt","r",encoding="UTF-8") as fin:
#     for sor in fin:
#         tantargyFelosztas.append(sor.strip())

#ver1
# for elem in tantargyFelosztas:
#     print(f"{elem},")       

#print(f"A listának {int(len(tantargyFelosztas)/4)} eleme van.")

#ver2
tanarok=[]
tantargyak=[]
osztalyok=[]
oraszamok=[]

rekord=[]

with open ("./beosztas.txt","r",encoding="UTF-8") as fin:
    for sor in fin:
        rekord.append(sor.strip())
        if len(rekord)==4:
            tanarok.append(rekord[0])
            tantargyak.append(rekord[1])
            osztalyok.append(rekord[2])
            oraszamok.append(int(rekord[3]))
            rekord=[]
            
for i in range(len(tanarok)):
    print(f"{tanarok[i]}, {tantargyak[i]}, {osztalyok[i]}, {oraszamok[i]}")

print("2. feladat:")
print(f"A fájlban {len(tanarok)} bejegyzés van.")

print("3. feladat")
print(f"Az iskolában a heti összóraszám: {sum(oraszamok)}")

def osszegzes(be_tanar,tanarok,oraszamok):
    osszOraszam=0
    for i in range(len(tanarok)):
        if tanarok[i]==be_tanar or "Albatrosz Aladin":
            osszOraszam+=oraszamok[i]
    return osszOraszam

print("4. feladat")
be_tanar=input("Egy tanár neve= ")
print(f"A tanár heti óraszáma: {osszegzes(be_tanar,tanarok,oraszamok)}")

def eldontes(beOsztaly,beTantargy,tantargyak,osztalyok):
    i=0
    while (i<len(tantargyak) and not (beTantargy==tantargyak[i] and beOsztaly.split(".")[0]==osztalyok[i].split(".")[0] and "x" in osztalyok[i])):
        i+=1
        
    return i<len(tantargyak)


print("6. feladat")
beOsztaly=input("Osztály= ") or "10.b"
beTantargy=input("Tantárgy= ") or "kemia"
if eldontes(beOsztaly,beTantargy,tantargyak,osztalyok):
    print("Csoportbontásban tanulják.")
else:
    print("Nem csoportbontásban tanulják.")

def megszamolas(tanarok):
    lista=[]
    for elem in tanarok:
        if elem in lista:
            None
        else:
            lista.append(elem)
    return len(lista)

print("7. feladat")
print(f"Az iskolában {megszamolas(tanarok)} tanár tanít.")