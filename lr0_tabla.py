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
                self.sorok.append("")
            self.tabla.append(self.sorok)
            

    def ertek_kiir(self,sor,oszlop):
        print(self.tabla[sor][oszlop])
        return self.tabla[sor][oszlop]

    def tabla_kiir(self):

        for i in range(0,self.sor): 
            for j in range(0,self.oszlop): 
                print(self.tabla[i][j]," ", end=" ")
            print()   

    def lr_tabla_kiir(self):
        s=5
        print("      # ",end="")
        for i in terminalisok:
            print(i.rjust(9+s, ' '),end="",sep="")
        for i in nemterminalisok:
            print(i.rjust(9+s, ' '),end="")    
        print("")
        print("-"*(11+s)*(len(terminalisok)+len(nemterminalisok)))
        print("")
       

        for i in range(0,self.sor): 
            print(str(i).rjust(3+s, ' '),". ",end=" ",sep="")
            for j in range(0,self.oszlop): 
                print((self.tabla[i][j]).rjust(7+s, ' ')," ", end=" ",sep="")
                if j==len(terminalisok)-1:
                    print("|",end="",sep="")
            print()   
            print()  

        print("-"*(11+s)*(len(terminalisok)+len(nemterminalisok)))

    def lr_tabla_to_html(self):
        t=chr(9)
        htm="<!DOCTYPE html>\n<html>\n"
        htm=htm+"<head>\n<style>\ntable, th, td {\n"+t+"border: 1px solid black;\n}\n</style>\n</head>"
        
        
        
        
        htm=htm+"<body>\n\n<h2>LR(0) HTML Table</h2>\n<table style="+chr(34)+"width:90%"+chr(34)+">\n"
        htm=htm+t+"<tr>\n"
        htm=htm+t+t+"<td> # </td>\n"
        for i in terminalisok:
            htm=htm+t+t+"<td>"+i+"</td>\n"
        htm=htm+t+t+"<td>*</td>\n"
        for i in nemterminalisok:
            htm=htm+t+t+"<td>"+i+"</td>\n"    
        htm=htm+t+"</tr>\n"

        for i in range(0,self.sor): 
            htm=htm+t+"<tr>\n"
            htm=htm+t+t+"<td>"+str(i)+"</td>\n"
            for j in range(0,self.oszlop): 
                htm=htm+t+t+"<td>"+self.tabla[i][j]+"</td>\n"
                if j==len(terminalisok)-1:
                    htm=htm+t+t+"<td>*</td>\n"
            htm=htm+t+"</tr>\n"
            
        htm=htm+t+"</tr>\n</table>\n</body>\n</html>\n"
        return(htm)



    def legyen(self,sor,oszlop,ertek):
        self.tabla[sor][oszlop]=ertek

    def legyen_add(self,sor,oszlop,ertek):
        self.tabla[sor][oszlop]=self.tabla[sor][oszlop]+ertek

def terminalise(s):  # true = terminális, false = nemterminális
    if s>="A" and s<="Z":
        return False
    return True    




#****************************************************************************************************         
from pyvis.network import Network
import networkx as nx
import base64
import webbrowser

f = open("c:\SZE-FordProg-2021-SLR-visualization\lr0_auto.txt", "r")
full_file=f.read()
eol_pos=full_file.find('\n')
kapcsolatok=full_file[:eol_pos]
szabalyok=full_file[eol_pos+1:]
kapcsolatok_lista=kapcsolatok.split(" ")
szabalyok_lista=szabalyok.split("\n")
sorok_szama=0
for cs in szabalyok_lista:
    if int(cs[0:cs.find(" ")])>sorok_szama:
        sorok_szama=int(cs[0:cs.find(" ")])
sorok_szama+=1        
print("Sorok:",sorok_szama)
nemterminalisok=list()
terminalisok=list()
i=2
while i<len(kapcsolatok_lista):
    if terminalise(kapcsolatok_lista[i]):
        if kapcsolatok_lista[i] not in terminalisok:
            terminalisok.append(kapcsolatok_lista[i])
    else:
        if kapcsolatok_lista[i] not in nemterminalisok:
           nemterminalisok.append(kapcsolatok_lista[i])    
    i=i+3

terminalisok.sort()
nemterminalisok.sort()
print("Terminalisok:",terminalisok) 
print("Nemterminalisok:",nemterminalisok)  
oszlopok_szama=len(terminalisok)+len(nemterminalisok)
tbl=matrix(sorok_szama,oszlopok_szama)

# tábla kitöltése  
i=0
while i<len(kapcsolatok_lista):
    if terminalise(kapcsolatok_lista[i+2]):
        tbl.legyen(int(kapcsolatok_lista[i]) , terminalisok.index(kapcsolatok_lista[i+2]) , "s"+kapcsolatok_lista[i+1] )
    else:
        tbl.legyen(int(kapcsolatok_lista[i]) , nemterminalisok.index(kapcsolatok_lista[i+2])+len(terminalisok) , "T"+kapcsolatok_lista[i+1] )
    i=i+3

t=0
t_karakter=""
for i in range(0,len(szabalyok_lista)):
    pos=szabalyok_lista[i].index(" ")+1
    if szabalyok_lista[i][pos:pos+1]=="¤":
        t=i
        t_karakter=szabalyok_lista[i][-1:]
for i in range(0,len(szabalyok_lista)):
    if szabalyok_lista[i][-2:]==t_karakter+"¤":
        t=i

acc_sor=int(szabalyok_lista[t][0:szabalyok_lista[i].index(" ")])

for i in range(0,len(terminalisok)):
    tbl.legyen_add(acc_sor,i," acc")

for i in range(0,len(szabalyok_lista)):
    if szabalyok_lista[i].count("»")==1 and szabalyok_lista[i][-1:]=="¤":
        sor=int(szabalyok_lista[i][0:szabalyok_lista[i].index(" ")])

        ertek=szabalyok_lista[i][     szabalyok_lista[i].index("»")-1  : szabalyok_lista[i].index("¤") ]

        for j in range(0,len(terminalisok)):
            tbl.legyen_add(sor,j," "+ertek)



tbl.lr_tabla_kiir()
html_tbl=tbl.lr_tabla_to_html()
wf = open("lr_to_html.htm", "w")
wf.write(html_tbl)
wf.close()
webbrowser.open_new_tab("lr_to_html.htm")


n=Network("1000px","1000px",directed=True)
for i in range (0,sorok_szama):
    lbl=str(i)+"\n\n"
    for j in range(0,len(szabalyok_lista)):
        
        sor=int(szabalyok_lista[j][0:szabalyok_lista[j].index(" ")])
        if i==sor:
           lbl=lbl+" "+szabalyok_lista[j][szabalyok_lista[j].index(" "):]+" \n"

    n.add_node(i,shape="box",label=lbl)
i=0
while i<len(kapcsolatok_lista):
    n.add_edge( int(kapcsolatok_lista[i]) ,int(kapcsolatok_lista[i+1]),label=kapcsolatok_lista[i+2] ,size=100)     
    i=i+3
n.repulsion(node_distance=120, central_gravity=0, spring_length=200, spring_strength=0, damping=0.09)
n.show("lr.html")