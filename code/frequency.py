def frequency(text):
    # Ein leeres Dictionary erstellen
    haeufigkeit = {}
    # Über jeden Buchstaben im Text iterieren
    for buchstabe in text:
        # Wenn der Buchstabe schon im Dictionary ist, seinen Zähler um eins erhöhen
        if buchstabe in haeufigkeit:
            haeufigkeit[buchstabe] += 1
        # Sonst den Buchstaben mit dem Zähler eins ins Dictionary einfügen
        else:
            haeufigkeit[buchstabe] = 1
    # Die Funktion aufrufen und das Ergebnis ausgeben
    print("Das ist die Häufigkeitsverteilung für deinen Text:")
    for k, v in haeufigkeit.items():
        print(f'"{k}"  :  {v}')






    


