# lr0 tabla


class matrix:
    def __init__(self, s, o):
        self.sor=s
        self.oszlop=o
        i=0
        j=0
        self.sorok = []
        self.tabla = []
        for j in range(0,self.sor):
            self.sorok = []
            for i in range(0,self.oszlop):
                self.sorok.append("*")
            self.tabla.append(self.sorok)
            

    def ertek_kiir(self,sor,oszlop):
        print(self.tabla[sor][oszlop])
        return self.tabla[sor][oszlop]

    def tabla_kiir(self):

        for i in range(0,self.sor): 
            for j in range(0,self.oszlop): 
                print(self.tabla[i][j]," ", end=" ")
            print()    

    def legyen(self,sor,oszlop,ertek):
        self.tabla[sor][oszlop]=ertek

#****************************************************************************************************         
from pyvis.network import Network
import networkx as nx



f = open("c:\SZE-FordProg-2021-SLR-visualization\lr0_auto.txt", "r")
full_file=f.read()
#print(full_file)pip 
eol_pos=full_file.find('\n')
#print(eol_pos)
kapcsolatok=full_file[:eol_pos]
csomopontok=full_file[eol_pos+1:]

print(kapcsolatok)
kapcsolatok_lista=kapcsolatok.split(" ")
print(kapcsolatok_lista)
tbl=matrix(10,4)
print(csomopontok)
csomopontok_lista=csomopontok.split("\n")
print(csomopontok_lista)
sorok_szama=0
for cs in csomopontok_lista:
    if int(cs[0:cs.find(" ")])>sorok_szama:
        sorok_szama=int(cs[0:cs.find(" ")])
print(sorok_szama)
nemterminalisok=list()
terminalisok=list()
i=2
while i<len(kapcsolatok_lista):
    if kapcsolatok_lista[i]>="A" and kapcsolatok_lista[i]<="Z":
        if kapcsolatok_lista[i] not in nemterminalisok:
            nemterminalisok.append(kapcsolatok_lista[i])
    else:
        if kapcsolatok_lista[i] not in terminalisok:
            terminalisok.append(kapcsolatok_lista[i])
    i=i+3

terminalisok.sort()
nemterminalisok.sort()
print(terminalisok) 
print(nemterminalisok)  
oszlopok_szama=len(terminalisok)+len(nemterminalisok)
print(oszlopok_szama)
tbl=matrix(sorok_szama,oszlopok_szama)
tbl.tabla_kiir()

  





