from turtle import clear
from numpy import block
import pandas as pd
import pygame as pg, sys

#裏側のmapの読み込み
mapdataold = pd.read_csv('map.csv')
print(mapdataold)

pg.init()
xlength=mapdataold["x"].max()
ywidth=mapdataold["y"].max()
screen = pg.display.set_mode((xlength, ywidth))
screen.fill(pg.Color("lightblue"))


#（変更用とmapdata用）listの作り
xylist = pd.read_csv("map.csv").values.tolist()

listx=[]
listy=[]

#この下をずっとループする
while True:

    mouse_state = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()

    if mouse_state[0]:
        #clickで障害物の位置を指定する
        print(mx, my)

        pg.draw.rect(screen, pg.Color("red"), (mx-5, my-5,10,10))


        #clickで指定された障害物の位置のdataをlistに導入する
        for a in range(10):
            for b in range(10):
                listx.append(mx+a)
                listy.append(my+b)

        for kx in listx:
            for ky in listy:
                xylist[((kx-1)*ywidth)+ky][2]=1
        
        listx.clear()
        listy.clear()
                

    #画面を表示する
    pg.display.update()


    #閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            
            #元のmapdataを変更する
            x=[]
            y=[]
            blocktype=[]

            for xyb in xylist:
                x.append(xyb[0])
                y.append(xyb[1])
                blocktype.append(xyb[2])
                
            mapdata={
                "x":x,
                "y":y,
                "blocktype":blocktype
                }
        
            df = pd.DataFrame(mapdata)
            df = df.set_index('x')
            df.to_csv("map.csv", encoding="utf-8")

            pg.quit()
            sys.exit()

#111111
