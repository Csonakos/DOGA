halozatok=[]
with open("hálózat.txt","r",encoding="utf-8") as forras, \
    open("halozatok_api.txt","w",encoding="utf-8") as cel:
    cimsor=forras.readline()
    for sor in forras:
            adat=sor.strip().split(",")
            halo={"Eszköz" :adat[0], "Csatlakozó" :adat[1], "Ipcím" :adat[2]}
            halozatok.append(halo)
print(f"{halozatok}")