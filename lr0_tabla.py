# lr0 tabla



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
