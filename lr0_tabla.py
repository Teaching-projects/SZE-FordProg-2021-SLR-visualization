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
                self.sorok.append(i+j)
            self.tabla.append(self.sorok)
        print(self.tabla)    

    def ertek(self,sor,oszlop):
        print(self.tabla[sor][oszlop])
        return self.tabla[sor][oszlop]

    def kiir(self):

        for i in range(0,self.sor): 
            for j in range(0,self.oszlop): 
                print(i,j,":",self.tabla[i][j]," ", end=" ")
            print()    

#****************************************************************************************************         
# Beolvassuk a lr0 adatait tartalmazó file-t
f = open("c:\SZE-FordProg-2021-SLR-visualization\lr0_auto.txt", "r")
full_file=f.read()
print(full_file)
eol_pos=full_file.find('\n')
print(eol_pos)
connections=full_file[:eol_pos]
nodes=full_file[eol_pos:]

print(connections)
print("+++++++++++++++++++++")
print(nodes)
tbl=matrix(10,4)
print(tbl)
print(tbl.kiir())         
print(tbl.ertek(8,2))
