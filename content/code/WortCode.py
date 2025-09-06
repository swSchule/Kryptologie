def WortCode(Lösung):
    if Lösung == "Stern":
        print("✔ Super! Das ist korrekt.")
    elif Lösung == "stern":
        print("✔ Super! Das ist korrekt.")
    elif Lösung == "STERN":
        print("✔ Super! Das ist korrekt.")
    else:
        import sys
        print("❗ Das ist leider nicht richtig. Überprüfe auf Rechtschreibfehler.", file=sys.stderr)