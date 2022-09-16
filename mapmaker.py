import pandas as pd

# mapdata(800, 600)
mapsize=(800,600)
x=[]
y=[]
blocktype=[]

print(mapsize[0],mapsize[1])

for rx in range(mapsize[0]):
    for ry in range(mapsize[1]):
        x.append(rx+1)
        y.append(ry+1)
        blocktype.append(0)

mapdata={
        "x":x,
        "y":y,
        "blocktype":blocktype
        }

df = pd.DataFrame(mapdata)
df = df.set_index('x')

#原始map.csv作成
df.to_csv("map.csv", encoding="utf-8")

#0 空気
#1　泥
#2　芝生