<br>
READ ME

<h1>Der Wish-Ender</h1>

*Inspired by Destiny 2:*
![wishender_inspiration](wishender/bilder/rachel-kong-wish-ender.jpg) 

<h3>Herzlich willkommen beim Wish-Ender</h3>
Die WishEnder-App ist eine Plattform auf welcher beliebig viele Wunschlisten erstellt werden können.
Dafür gibt der Nutzer zuerst einen Listennamen ein und fügt darunter seine Wünsche *(zur Zeit max. 4)* ein.
Bei erneutem Besuch der Startseite bietet sich die Option bestehende Listen einzusehen oder weitere zu erstellen.
Auf der Seite der Listenübersicht, welche über den Button "Zu allen Listen" zu erreichen ist,
werden alle Listen angezeigt und es besteht die Möglichkeit erfüllte Wünsche dauerhaft abzuhaken.

<h3>Workflow *(Dateneingabe, Datenverarbeitung/Speicherung, Datenausgabe)*</h3>

Der Nutzer gibt auf der Startseite einen Listennamen und nach Bedarf 1 - 4 Wünsche ein. 
Diese Daten werden daraufhin als Dict in Dict in einem .json - File abgespeichert, leere Wünsche sind dabei 
als leerer String erfasst. Will der Nutzer alle bestehenden Listen abrufen, 
werden die Wünsche als Ansammlung von Listen wiedergegeben, dabei werden die leeren Strings ignoriert.
Nach demselben Verfahren kann auf der Startseite auch eine einzelne Liste durch Auswahl im Dropdown abgerufen werden. 
Die Wunschnummern (1. Wunsch, 2. Wunsch, etc.) sind den Wünschen fix zugeordnet, weshalb es beim Auslassen eines 
Wunsch-Feldes zu Nummerierungsproblemen kommt. 

Der genaue Ablauf ist auch im Flowchart (draw.io) ersichtlich.


Auf der Wunschlistenübersicht besteht die Option, erfüllte Wünsche via Checkbox dauerhaft abzuhaken. Die abgehakten 
Wünsche werden dabei bei jedem Absenden des Formulars (Also mit Klick auf den "Speichern"-Button) als dict in einem 
Separaten .json-File abgespeichert. Dies ermöglicht auch das dauerhafte Speichern, da bei jedem neuen Aufruf der Seite 
das File nach Wünschen durchsucht wird. Da bei jedem Speichervorgang die bestehende Liste überschrieben wird, können 
auch Wünsche wieder abgewählt werden, da nur Wünsche mit aktiver (checked) Checkbox übermittelt werden.

Auf der Startseite kann, sobald eine erste Liste erstellt wurde, via Dropdown-Menü eine einzelne Liste angezeigt werden
um nicht auf die ganze Übersicht wechseln zu müssen.


<h3>Zukunft</h3>

Für zukünftige Updates ist das Ziel eine unbeschränkte Anzahl an Wünschen hinzufügen zu können.
Ausserdem müsste bei dieser Erweiterung die Nummerierung zu einem späteren Zeitpunkt erfolgen 
(z.B. mit "enumerate") damit auch bei Auslassen eines Eingabefeldes eine fortlaufende Nummerierung garantiert
ist.

Zudem wäre die Option einer Preisangabe pro Wunsch noch wertvoll.

