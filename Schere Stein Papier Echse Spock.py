import random
import time

#Einleitung
uprint("Schere|Stein|Papier|Echse|Spock");time.sleep(0.5)
print("Regeln: Stein schlägt Schere");time.sleep(1)
print("Regeln: Papier schlägt Stein");time.sleep(1)
print("Regeln: Echse schlägt Papier");time.sleep(1)
print("Regeln: Spock schlägt Echse");time.sleep(1)
print("Regeln: Schere schlägt Spock");time.sleep(1)

#Variablen
figuren = ("Schere", "Stein", "Papier", "Echse", "Spock")
spielen = True

while spielen:

    #Spielfigur auswählen
    spielerauswahl = 0
    while spielerauswahl not in (1,2,3,4,5):
        spielerauswahl = int(input("[1]Schere [2]Stein [3]Papier [4]Echse [5]Spock\n"))
    spielfigur = figuren[spielerauswahl - 1]
                            
    #Computerfigur auswählen
    computerfigur = figuren[random.randint(0,4)]
                           
    #Sieger ermitteln
    if spielfigur == computerfigur:
       print("Unentschieden Computer wählte", computerfigur)
    else:
                                              
       if spielfigur == "Schere":
        if computerfigur == "Stein":
            print("Verloren Computer wählte", computerfigur)
        else:
            print("Gewonnen Computer wählte", computerfigur)
            
       if spielfigur == "Stein":
        if computerfigur == "Papier":
            print("Verloren Computer wählte", computerfigur)
        else:
            print("Gewonnen Computer wählte", computerfigur)

       if spielfigur == "Papier":
        if computerfigur == "Echse":
            print("Verloren Computer wählte", computerfigur)
        else:
            print("Gewonnen Computer wählte", computerfigur)
            
       if spielfigur == "Echse":
        if computerfigur == "Spock":
            print("Verloren Computer wählte", computerfigur)
        else:
            print("Gewonnen Computer wählte", computerfigur)

       if spielfigur == "Spock":
        if computerfigur == "Schere":
            print("Verloren Computer wählte", computerfigur)
        else:
            print("Gewonnen Computer wählte", computerfigur)
            
   
    #Restart?
    time.sleep(1)
    entscheidung = ""
    while entscheidung not in("y", "n"):
       entscheidung = input("\nNochmal spielen? [y]Ja [n]Nein")
       
    if(entscheidung == "n"):
       spielen = False                    
