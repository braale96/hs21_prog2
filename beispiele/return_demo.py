def gruppen_preis(gruppen_groesse):
    if gruppen_groesse > 100:
        return "Gruppe zu gross"
    if gruppen_groesse > 50:
        preis = 100
    else:
        preis = 200
    return preis


gruppe = 101

ergebnis = gruppen_preis(gruppe)
print(ergebnis)
