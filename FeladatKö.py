konyvtar=[]
with open("konyvtar.txt","r",encoding="utf-8") as forras, \
    open("konyvtar_api.txt","w",encoding="utf-8") as cel:
    cimsor=forras.readline()
    for sor in forras:
            adat=sor.strip().split(",")
            konyv={"Szerzõ" :adat[0], "Cím" :adat[1], "KiadásÉve" :adat[2], "ISBN" :adat[3], "Állapot" :adat[4]}
            konyvtar.append(konyv)
print(f"{konyvtar}")