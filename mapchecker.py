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


#（mapdata用）listの作り
xylist = pd.read_csv("map.csv").values.tolist()

xylist2 = []

xlength2=int(xlength/10)
ywidth2=int(ywidth/10)
for ix in range(1,xlength2+1):
    for iy in range(1,ywidth2+1):
        ik=xylist[(((ix*10)-1)*ywidth)+(iy*10)][2]
        
        
        xylist2.append([ix*10,iy*10,ik])



imgmud=pg.image.load('game2\lawn.png')
imgmud=pg.transform.scale(imgmud, (10, 10))
for i in range(0,len(xylist2)):
    if xylist2[i][2]==1:
        mudrect = pg.Rect(xylist2[i][0]-9,xylist2[i][1]-9,1,1)
        screen.blit(imgmud, mudrect)

#この下をずっとループする
while True:
    for kx in xylist:
        if kx[2]==1:
            pg.draw.rect(screen, pg.Color("red"), (kx[0], kx[1], 1, 1))

                
    # 6.画面を表示する
    pg.display.update()
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
