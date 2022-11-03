import pyautogui as py
import time
import webbrowser

while (True):
    # Ouvrir la webapp FUT
    webbrowser.open("https://www.ea.com/fifa/ultimate-team/web-app/")

    time.sleep(10)

    py.leftClick(1278, 637) #Position onglet transfert

    time.sleep(25)
    

    py.leftClick(48, 439) #Position onglet transfert

    time.sleep(10)


    py.leftClick(790, 734) #Position onglet list transfert

    time.sleep(15)


    py.leftClick(1191, 304) #Position clear sold

    time.sleep(17)

    py.leftClick(1196, 514) #Position relist all

    time.sleep(10)

    py.leftClick(931, 645) #Confirmer relisting

    time.sleep(10)

    py.leftClick(1903, 47) #Fermer le browser

    time.sleep(3600)