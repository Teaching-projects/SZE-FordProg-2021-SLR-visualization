# SZE-FordProg-2021-SLR-visualization

Teszt nyelvtan:

S -> S - E .
S -> S + E .
S -> E .
E -> E * n .
E -> E / n .
E -> n .

A fenti nyelvtan LR tárolási formátuma (ez a program bemenete): 

0 3 n 0 1 S 0 2 E 1 4 - 1 5 + 4 3 n 4 8 E 5 3 n 5 9 E 8 7 / 8 6 * 9 7 / 9 6 * 2 7 / 2 6 * 7 11 n 6 10 n
0 ¤S
0 S»¤S-E
0 S»¤S+E
0 S»¤E
0 E»¤E*n
0 E»¤E/n
0 E»¤n
1 S¤
1 S»S¤-E
1 S»S¤+E
2 S»E¤
2 E»E¤*n
2 E»E¤/n
3 E»n¤
4 S»S-¤E
4 E»¤E*n
4 E»¤E/n
4 E»¤n
5 S»S+¤E
5 E»¤E*n
5 E»¤E/n
5 E»¤n
6 E»E*¤n
7 E»E/¤n
8 S»S-E¤
8 E»E¤*n
8 E»E¤/n
9 S»S+E¤
9 E»E¤*n
9 E»E¤/n
10 E»E*n¤
11 E»E/n¤

Az első sor tartalmazza a kapcsolatokat pl: 0 3 n jelentése nullás állapitból a hármas állapotba az átmenet n-nel
A további sorok az item set-ek. az elején a sorszám, és utána a szabály. A » karakter jelenti a "nyilat" és a ¤ karakter jelenti a "pöttyöt"

A kimenet a lr_to_html.htm file-ba képződik, valamint vicces formában vizualizálja a nyelvtan automatáját a pyvis modul segítségével.

