PROG02 _ Projektidee:

"Der Wishender"

*Inspired by:*
![wishender_inspiration](bilder/rachel-kong-wish-ender.jpg)


READ ME :)

Die Wishender - App ist eine Plattform auf welcher beliebig viele Wunschlisten erstellt werden können.
Dabei kann der Nutzer zuerst eine Wunschliste erstellen. Dafür gibt er zuerst einen Listennamen ein 
und fügt darunter seine Wünsche (zur Zeit max. 4) ein.
Bei erneutem Besuch der Startseite bietet sich die Option bestehende Listen einzusehen oder weitere zu erstellen.

Workflow (Dateneingabe, Datenverarbeitung/Speicherung, Datenausgabe)

Der Nutzer gibt Listennamen und nach Bedarfe 1 - 4 Wünsche ein. Diese Daten werden als Dict in Dict in einem .json -
File abgespeichert - leere Wünsche sind dabei als leerers String erfasst. Will der Nutzer die Listen abrufen, 
werden die Wünsche  als Ansammlung von Listen wiedergegeben, dabei werden die leeren Strings ignoriert.
Nach demselben Verfahren kann auf der Startseite auch eine einzelne Liste abgerufen werden. Die Wunschnummern
(1. Wunsch, 2. Wunsch, etc.) sind den Wünschen fix zugeordnet, weshalb es beim Auslassen eines Feldes zu 
Nummerierungsproblemen kommen kann.

 
-> ABLAUF im Flowchart (draw.io)