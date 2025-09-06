def CaesarCode(Lösung):
    if Lösung == "Heute ist ein toller Tag":
        print("✔ Das ist korrekt.")
    elif Lösung == "heute ist ein toller tag":
        print("✔ Das ist korrekt.")
    elif Lösung == "HEUTE IST EIN TOLLER TAG":
        print("✔ Das ist korrekt.")
    else:
        import sys
        print("❗ Das ist leider nicht richtig. Überprüfe auf Rechtschreibfehler.", file=sys.stderr)