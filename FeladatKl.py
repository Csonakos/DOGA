kliensek=[]
with open("kliensek.txt","r",encoding="utf-8") as forras, \
    open("kliensek_api.txt","w",encoding="utf-8") as cel:
    cimsor=forras.readline()
    for sor in forras:
            adat=sor.strip().split(",")
            klien={"Eszköz" :adat[0], "Ipcím" :adat[1], "MacCím" :adat[2], "Csatlakozó" :adat[3]}
            kliensek.append(klien)
print(f"{kliensek}")