from encodings import utf_8
import os 
import pyautogui as pg
import time
import pyautogui as pag

def q(mass):    
    for i in range(len(mass)):
        print(range(len(mass)))
        if mass[i][1]=='steam' or mass[i][1] =='Steam':
            print(mass[i][1])            
            file= open('File.bat','w+')
            fuck_text= f'`@echo off \ntaskkill /f /im steam.exe \n@echo off \nStart {mass[i][2]} -login {mass[i][3]} {mass[i][4]} \nexit`'
            file.write(fuck_text)             
            file.close()
        ##########я остановился на том как поместить переменную по середине строки , и как изменить мне txt файл на bat файл , ...
        ##############################################
        ########################################################################
        ##############################################################################################################################
            os.startfile('File.bat')
    for i in range(len(mass)):
        if mass[i][1]=='Battlenet' or mass[i][1] =='Battlnet' or mass[i][1] =='battlnet' or mass[i][1] =='battlenet' or mass[i][1] =='батлнет' or mass[i][1] =='batlnet' or mass[i][1] =='Batlnet':
            pg.hotkey('win','d')
            time.sleep(1)
            os.startfile(mass[i][2]) 
            time.sleep(20)
            pg.leftClick(1082, 469)
            time.sleep(1)
            pg.leftClick(992,828)
            time.sleep(15)
                ## сворачивание всех экранов 
            pg.hotkey('win','d')
            time.sleep(5)
    for i in range(len(mass)):
        if mass[i][1]=='origin' or mass[i][1] =='Origin' or mass[i][1] =='orign' or mass[i][1] =='Orign' or mass[i][1] =='ориджн' or mass[i][1] =='орижн' :
            time.sleep(7)
            os.startfile(mass[i][2])
            time.sleep(25)
            #pg.leftClick(843, 443)
            pg.leftClick(1132, 440)
            pg.leftClick(1132, 440)
            pg.leftClick(1132, 440)
            time.sleep(1)
            pg.typewrite(mass[i][3], 0.02)
            time.sleep(1) 
            pg.leftClick(835, 485)
            time.sleep(1)
            pg.typewrite(mass[i][4],  0.02) 
            pg.leftClick(950, 641)
            pg.doubleClick(950,641)
            time.sleep(8) 
    for i in range(len(mass)):
        if mass[i][1]=='Wargaming' or mass[i][1] =='Wargaming.net' or mass[i][1] =='танки' or mass[i][1] =='Танки' or mass[i][1] =='wargamin' or mass[i][1] =='wargamin.net' :
            pg.hotkey('win','d')
            time.sleep(4)
            os.startfile(mass[i][2])
    for i in range(len(mass)):
        if mass[i][1]=='GameCenter' or mass[i][1] =='gamecenter' or mass[i][1] =='Warface' or mass[i][1] =='warface' or mass[i][1] =='варфейс' or mass[i][1] =='Варфейс' or mass[i][1] =='gameCenter' :
            pg.hotkey('win','d')
            time.sleep(4)
            os.startfile(mass[i][2])
            time.sleep(4)
    for i in range(len(mass)):
        if mass[i][1]=='EpicGamesLauncher' or mass[i][1] =='EpicGames' or mass[i][1] =='epicgameslauncher' or mass[i][1] =='epicgames' or mass[i][1] =='fortnite' or mass[i][1] =='Fortnite' or mass[i][1] =='фортнайт' :
            time.sleep(8)
            pg.hotkey('win','d')
            os.startfile(mass[i][2]) 
            time.sleep(11)
            pag.press("tab")
            pag.press("tab")
            pag.press("tab")
            pag.press("tab")
            pag.press("tab")
            pag.press("tab")
            pag.press("tab")
            pag.press("tab")
            pag.press("tab")
            pag.press("tab")
            pag.press("tab")
            pag.press("tab")
            pag.press("tab")
            pag.press("enter")
            time.sleep(8)
    for i in range(len(mass)):
        if mass[i][1]=='RiotClientServices.exe' or mass[i][1] =='RiotClientServices' or mass[i][1] =='RiotClient' or mass[i][1] =='Riot' or mass[i][1] =='riot' :
            time.sleep(5)
            pg.hotkey('win','d')
            os.startfile(mass[i][2]) 
            time.sleep(16)
            pg.leftClick(318, 375)
            pg.doubleClick(318,375)
            pg.typewrite(mass[i][3],  0.02)
            time.sleep(2)
            pg.leftClick(318, 433)
            pg.typewrite(mass[i][4],  0.02)
            time.sleep(2)
            pag.press("enter")
            
            time.sleep(8)
    return mass
    

#`@echo off
#taskkill /f /im steam.exe
#@echo off
#Start Start C:\"Program Files (x86)"\Steam\steam.exe -login nahimovskypubg1 Balesny1986=-
#exit`
#
#