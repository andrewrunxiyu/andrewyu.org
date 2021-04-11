#!/usr/bin/env/python3
import os
ls = os.listdir(".")
ls.remove("gen.py")
ls.remove("index.def.gmi")
ls.remove("index.gmi")
ls.reverse()
print(ls)
links = []
for f in ls:
    desc = f.replace(".gmi", "")
    desc = desc.replace("_", " ")
    desc = desc.split(" ")
    print(desc)
    desc = ' '.join(desc)
    links.append(f"=> {f} {desc}")
yay = '\n'.join(links)
print(yay)

with open("index.def.gmi", "r") as template:
    tplt = template.read()
    wr = tplt.replace("[ POSTS ]", yay)

with open("index.gmi", "w") as writer:
    writer.write(wr)
    writer.close()
