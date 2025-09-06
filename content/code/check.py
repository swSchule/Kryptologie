# --- Funktionsübersicht ---

# Caesar-Verschlüsselung
# encrypt_letter(letter, n): Verschlüsselt einen Buchstaben mit dem Caesar-Verfahren und Schlüssel n.
# decrypt_letter(letter, n): Entschlüsselt einen Buchstaben mit dem Caesar-Verfahren und Schlüssel n.
# encrypt_text(text, n): Verschlüsselt einen Text mit dem Caesar-Verfahren und Schlüssel n.
# decrypt_text(text, n): Entschlüsselt einen Text mit dem Caesar-Verfahren und Schlüssel n.
# calc(m, e): Berechnet m hoch e (Potenz).

# Überprüfungslösungen
# caesar_code(loesung): Prüft die Lösung für einen Caesar-verschlüsselten Text.
# wort_code(loesung): Prüft die Lösung für einen Wort-Code.
# caesar_test(encr_letter, encr_text, decrt_letter, decr_text): Testet die Caesar-Funktionen auf Korrektheit und gibt Rückmeldung.
# vigenere_code(lösung): Prüft die Lösung für die Vigenère-Verschlüsselung von 'GEHEIMNIS' mit Schlüsselwort 'CODE'.

# Analyse und Mathematik
# frequency(text): Gibt die Häufigkeitsverteilung der Zeichen im Text aus.
# ggt(a, b): Berechnet den größten gemeinsamen Teiler (ggT) von a und b.
# is_prime(n): Prüft, ob n eine Primzahl ist.
# prime_factors(n): Gibt die Primfaktorzerlegung von n als Liste zurück.
# phi(n): Berechnet die Euler'sche Phi-Funktion von n.
# modinv(a, m): Berechnet das multiplikative Inverse von a modulo m.
# extended_gcd(a, b): Erweiterter euklidischer Algorithmus für ggT und Inverse.

# RSA-Verschlüsselung
# encrypt_rsa(m, e, n): RSA-Verschlüsselung: Verschlüsselt m mit Schlüssel (e, n).
# decrypt_rsa(c, d, n): RSA-Entschlüsselung: Entschlüsselt c mit Schlüssel (d, n).
# chiphre_text(c, m, e, n): Prüft, ob der Geheimtext c korrekt aus m, e, n berechnet wurde.
# d_berechnen(e, phi_n): Berechnet den privaten Schlüssel d aus e und phi(n).

# Sonstiges
# day(n): Gibt den Wochentag zu einer Zahl n zurück.
# sport(): Platzhalterfunktion: Gibt einen Sport-Spruch aus.
# topf(): Platzhalterfunktion: Gibt einen Topf-Spruch aus.
# zbggt(a, b): Gibt den ggT von a und b aus.

# Interaktive Widgets (nur für Jupyter)
# caesar_wheel_widget(): Interaktives Widget für das Caesar-Rad (Jupyter).
# vigenere_quadrat_widget(): Interaktives Widget für das Vigenère-Quadrat (Jupyter).
# vigenere_quadrat_interaktiv(): Interaktive HTML-Tabelle für das Vigenère-Quadrat (Jupyter).

# Aufgabenüberprüfung
# PrimzahlErkennen(Zahl_6, Zahl_11, Zahl_23, Zahl_31, Zahl_42, Zahl_63): Prüft, ob die Antworten zu den Zahlen 6, 11, 23, 31, 42, 63 korrekt als Primzahl/Nicht-Primzahl angegeben wurden.
# correctprime(p, q): Prüft, ob p und q verschieden und Primzahlen sind.
# product(p, q, N): Prüft, ob N das Produkt aus p und q ist.



import math
import sys



# Caesar-Verschlüsselung 
def encrypt_letter(letter, n):
    """Verschlüsselt einen Buchstaben mit dem Caesar-Verfahren und Schlüssel n."""
    number = ord(letter.upper()) - ord('A')
    cipher = (number + n) % 26
    return chr(cipher + ord('A'))

def decrypt_letter(letter, n):
    """Entschlüsselt einen Buchstaben mit dem Caesar-Verfahren und Schlüssel n."""
    number = ord(letter.upper()) - ord('A')
    plain = (number - n) % 26
    return chr(plain + ord('A'))

def encrypt_text(text, n):
    """Verschlüsselt einen Text mit dem Caesar-Verfahren und Schlüssel n."""
    cipher_text = ""
    for letter in text.upper():
        if 'A' <= letter <= 'Z':
            cipher_text += encrypt_letter(letter, n)
        else:
            cipher_text += letter
    return cipher_text

def decrypt_text(text, n):
    """Entschlüsselt einen Text mit dem Caesar-Verfahren und Schlüssel n."""
    plain_text = ""
    for letter in text.upper():
        if 'A' <= letter <= 'Z':
            plain_text += decrypt_letter(letter, n)
        else:
            plain_text += letter
    return plain_text

def calc(m, e):
    """Berechnet m hoch e (Potenz)."""
    return pow(m, e)

# Caesar-Code Überprüfung
def caesar_code(loesung):
    """Prüft die Lösung für einen Caesar-verschlüsselten Text."""
    if loesung == "Heute ist ein toller Tag":
        print("✔ Das ist korrekt.")
    elif loesung == "heute ist ein toller tag":
        print("✔ Das ist korrekt.")
    elif loesung == "HEUTE IST EIN TOLLER TAG":
        print("✔ Das ist korrekt.")
    else:
        print("❗ Das ist leider nicht richtig. Überprüfe auf Rechtschreibfehler.", file=sys.stderr)

# WortCode Überprüfung
def wort_code(loesung):
    """Prüft die Lösung für einen Wort-Code."""
    if loesung in ["Stern", "stern", "STERN"]:
        print("✔ Super! Das ist korrekt.")
    else:
        print("❗ Das ist leider nicht richtig. Überprüfe auf Rechtschreibfehler.", file=sys.stderr)


#Caeser-Verschlüsseung prüfen der erstellten Programme
def caesar_test(encr_letter, encr_text, decrt_letter, decr_text):
    """Testet die Caesar-Funktionen auf Korrektheit und gibt Rückmeldung."""
    meldungen = []

    # Einzelbuchstaben-Tests
    test_cases = [
        ("A", 3, "D"),
        ("Z", 1, "A"),
    ]

    # encrypt_letter
    korrekt = True
    for letter, key, expected in test_cases:
        result = encr_letter(letter, key)
        if result != expected:
            meldungen.append(f"encrypt_letter: Fehler bei '{letter}', {key}: '{result}' statt '{expected}'")
            korrekt = False
    if korrekt:
        meldungen.append("encrypt_letter: korrekt")

    # decrypt_letter
    korrekt = True
    for letter, key, expected in test_cases:
        result = encr_letter(letter, key)
        decrypted = decrt_letter(result, key)
        if decrypted != letter:
            meldungen.append(f"decrypt_letter: Fehler bei '{result}', {key}: '{decrypted}' statt '{letter}'")
            korrekt = False
    if korrekt:
        meldungen.append("decrypt_letter: korrekt")

    # encrypt_text
    text = "HEUTE IST EIN ToLLER TAG"
    key = 15
    cipher_text = encrypt_text(text, key)
    if cipher_text == encr_text(text, key):
        meldungen.append("encrypt_text: korrekt")
    else:
        meldungen.append(f"encrypt_text: Fehler bei '{text}', {key}: '{encr_text(text,key)}' statt '{cipher_text}'")
    
    # decrypt_text
        
    decrypted_text = decr_text(cipher_text, key)
    if decrypted_text == text.upper():
        meldungen.append("decrypt_text: korrekt")
    else:
        meldungen.append(f"decrypt_text: Fehler bei '{cipher_text}', {key}: '{decrypted_text}' statt '{text.upper()}'")

    return "\n".join(meldungen)





def vigenere_code(lösung):
    """Prüft die Lösung für die Vigenère-Verschlüsselung von 'GEHEIMNIS' mit Schlüsselwort 'CODE'."""
    
    # Erwarteter Geheimtext (Achtung: Großbuchstaben, keine Leerzeichen)
    expected = "ISKIKAQMU"
    # Eingabe vereinheitlichen
    user = lösung.replace(" ", "").upper()
    if user == expected:
        print("✅ Richtig! Deine Verschlüsselung stimmt.")
    else:
        print("❌ Leider falsch. Überprüfe deine Verschlüsselung noch einmal.")

def vigenere_decode(lösung):
    """
    Prüft die Lösung für die Vigenère-Verschlüsselung von 'GEHEIMNIS' mit Schlüsselwort 'CODE'.
    """
    # Erwarteter Klartext" (Achtung: Großbuchstaben, keine Leerzeichen)
    expected = "KLARTEXT"
    # Eingabe vereinheitlichen
    user = lösung.replace(" ", "").upper()
    if user == expected:
        print("✅ Richtig! Deine Entschlüsselung stimmt.")
    else:
        print("❌ Leider falsch. Überprüfe deine Verschlüsselung noch einmal.")

# Häufigkeitsanalyse
def frequency(text):
    """Gibt die Häufigkeitsverteilung der Zeichen im Text aus."""
    haeufigkeit = {}
    for buchstabe in text:
        if buchstabe in haeufigkeit:
            haeufigkeit[buchstabe] += 1
        else:
            haeufigkeit[buchstabe] = 1
    print("Das ist die Häufigkeitsverteilung für deinen Text:")
    for k, v in haeufigkeit.items():
        print(f'"{k}"  :  {v}')

# ggT (größter gemeinsamer Teiler)
def ggt(a, b):
    """Berechnet den größten gemeinsamen Teiler (ggT) von a und b."""
    while b:
        a, b = b, a % b
    return a

# Primzahltest (einfach)
def is_prime(n):
    """Prüft, ob n eine Primzahl ist."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Primfaktorzerlegung
def prime_factors(n):
    """Gibt die Primfaktorzerlegung von n als Liste zurück."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

# Euler'sche Phi-Funktion
def phi(n):
    """Berechnet die Euler'sche Phi-Funktion von n."""
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

# Modulo-Inverse (erweiteter euklidischer Algorithmus)
def modinv(a, m):
    """Berechnet das multiplikative Inverse von a modulo m."""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Kein Inverses vorhanden')
    else:
        return x % m

def extended_gcd(a, b):
    """Erweiterter euklidischer Algorithmus für ggT und Inverse."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

# RSA-Verschlüsselung/Entschlüsselung
def encrypt_rsa(m, e, n):
    """RSA-Verschlüsselung: Verschlüsselt m mit Schlüssel (e, n)."""
    return pow(m, e, n)

def decrypt_rsa(c, d, n):
    """RSA-Entschlüsselung: Entschlüsselt c mit Schlüssel (d, n)."""
    return pow(c, d, n)

# Überprüfung Chiffretext
def chiphre_text(c, m, e, n):
    """Prüft, ob der Geheimtext c korrekt aus m, e, n berechnet wurde."""
    if c == pow(m, e, n):
        print("✔ Super! Du hast deine Nachricht erfolgreich in einen Geheimtext umgewandelt.")
    else:
        print("❗ Da hast du dich leider verrechnet. Probier es nochmal.", file=sys.stderr)

# Beispiel für d-Berechnung (RSA)
def d_berechnen(e, phi_n):
    """Berechnet den privaten Schlüssel d aus e und phi(n)."""
    return modinv(e, phi_n)

# Tag-Funktion (z.B. für Wochentag)
def day(n):
    """Gibt den Wochentag zu einer Zahl n zurück."""
    tage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    return tage[n % 7]

# Sport-Funktion (Platzhalter)
def sport():
    """Platzhalterfunktion: Gibt einen Sport-Spruch aus."""
    print("Sport macht Spaß!")

# Topf-Funktion (Platzhalter)
def topf():
    """Platzhalterfunktion: Gibt einen Topf-Spruch aus."""
    print("Hier ist dein Topf!")

# ZBggT (Zusammenhang ggT, Platzhalter)
def zbggt(a, b):
    """Gibt den ggT von a und b aus."""
    print(f"Der ggT von {a} und {b} ist {ggt(a, b)}.")

def caesar_wheel_widget():
    """Interaktives Widget für das Caesar-Rad (Jupyter)."""
    import ipywidgets as widgets
    from IPython.display import display, HTML
    import math

    def caesar_wheel_svg(shift):
        outer = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        inner = outer[shift:] + outer[:shift]
        svg = [
            '<svg width="340" height="340" viewBox="0 0 340 340">',
            '  <g>',
            '    <circle cx="170" cy="170" r="150" fill="#e0e0e0" stroke="#333" stroke-width="2"/>',
            '    <circle cx="170" cy="170" r="110" fill="#fff" stroke="#333" stroke-width="2"/>',
            '    <circle cx="170" cy="170" r="70" fill="none" stroke="#bbb" stroke-width="2"/>',  # kleinerer innerer Kreis
        ]
        # Trennlinien zwischen die Buchstaben (zwischen den Segmenten)
        for i in range(26):
            angle = ((i + 0.5) / 26) * 2 * math.pi - math.pi / 2
            x1 = 170 + 150 * math.cos(angle)
            y1 = 170 + 150 * math.sin(angle)
            x2 = 170 + 70 * math.cos(angle)
            y2 = 170 + 70 * math.sin(angle)
            svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#888" stroke-width="1"/>')
        # Äußere Buchstaben (zur Mitte ausgerichtet)
        for i, c in enumerate(outer):
            angle = (i / 26) * 2 * math.pi - math.pi / 2
            x = 170 + 135 * math.cos(angle)
            y = 170 + 135 * math.sin(angle)
            rotate = angle * 180 / math.pi + 90
            svg.append(
                f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" dominant-baseline="middle" '
                f'font-size="18" font-family="monospace" '
                f'transform="rotate({rotate:.1f},{x:.1f},{y:.1f})">{c}</text>'
            )
        # Innere Buchstaben (zur Mitte ausgerichtet, größer)
        for i, c in enumerate(inner):
            angle = (i / 26) * 2 * math.pi - math.pi / 2
            x = 170 + 90 * math.cos(angle)
            y = 170 + 90 * math.sin(angle)
            rotate = angle * 180 / math.pi + 90
            svg.append(
                f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" dominant-baseline="middle" '
                f'font-size="19" font-family="monospace" fill="#1976d2" '
                f'transform="rotate({rotate:.1f},{x:.1f},{y:.1f})">{c}</text>'
            )
        svg.append('  </g></svg>')
        return ''.join(svg)

    def update_wheel(shift):
        display(HTML(caesar_wheel_svg(shift)))

    slider = widgets.IntSlider(value=0, min=0, max=25, step=1, description='Drehung:')
    widgets.interact(update_wheel, shift=slider)

# Aufruf im Notebook:
# caesar_wheel_widget()


def vigenere_quadrat_widget():
    """Interaktives Widget für das Vigenère-Quadrat (Jupyter)."""
    import ipywidgets as widgets
    from IPython.display import display, Markdown

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Mehr Platz für die Beschriftung der Schieberegler
    row_slider = widgets.IntSlider(
        value=0, min=0, max=25,
        description='Schlüssel (links):',
        style={'description_width': '150px'},
        layout=widgets.Layout(width='400px')
    )
    col_slider = widgets.IntSlider(
        value=0, min=0, max=25,
        description='Klartext (oben):',
        style={'description_width': '150px'},
        layout=widgets.Layout(width='400px')
    )

    output = widgets.Output()

    def update(*args):
        j = row_slider.value  # Schlüssel (links)
        i = col_slider.value  # Klartext (oben)
        klar = alpha[i]
        schl = alpha[j]
        erg = alpha[(i + j) % 26]
        # Tabelle: Klartext oben, Schlüssel links
        table = (
            "<style>"
            ".vigcell {padding:0; width:19px; height:18px; text-align:center; border:1px solid #bbb; font-family:monospace;font-size:12px}"
            ".vighead {background:#e0e0e0; font-weight:bold;}"
            ".vighigh {background:#ffe082; font-weight:bold;}"
            ".vighighcell {background:#fff9c4;}"
            ".vighighboth {background:#ffd54f; font-weight:bold;}"
            "</style>"
            "<table style='border-collapse:collapse;'>"
            "<tr><td class='vigcell'></td>"
        )
        # Klartext-Überschriften (oben)
        for c in range(26):
            cls = "vigcell vighead"
            if c == i:
                cls += " vighigh"
            table += f"<td class='{cls}'>{alpha[c]}</td>"
        table += "</tr>"
        # Zeilen: Schlüssel links
        for r in range(26):
            cls = "vigcell vighead"
            if r == j:
                cls += " vighigh"
            table += f"<tr><td class='{cls}'>{alpha[r]}</td>"
            for c in range(26):
                cell = alpha[(c + r) % 26]
                cell_cls = "vigcell"
                if c == i and r == j:
                    cell_cls += " vighighboth"
                elif c == i or r == j:
                    cell_cls += " vighighcell"
                table += f"<td class='{cell_cls}'>{cell}</td>"
            table += "</tr>"
        table += "</table>"
        with output:
            output.clear_output()
            display(Markdown(
                f"**Klartext:** {klar}  **Schlüssel:** {schl}  **Geheimtext:** **{erg}**\n\n"
            ))
            display(Markdown(table))

    row_slider.observe(update, 'value')
    col_slider.observe(update, 'value')

    display(widgets.HBox([row_slider, col_slider]))
    display(output)
    update()









from IPython.display import display, HTML

def vigenere_quadrat_interaktiv():
    """Interaktive HTML-Tabelle für das Vigenère-Quadrat (Jupyter)."""
    #Funktioniert nicht in JupyterLite
    # Alphabet
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Tabelle als HTML mit IDs für Zeilen/Spalten
    html = """
    <style>
    .vig-table { border-collapse: collapse; }
    .vig-table td, .vig-table th { border: 1px solid #888; padding: 4px 7px; text-align: center; font-family: monospace; }
    .vig-table th { background: #e0e0e0; }
    .vig-highlight { background: #ffe082 !important; }
    .vig-highlight-header { background: #ffd54f !important; }
    </style>
    <table class="vig-table" id="vig-table">
      <tr>
        <th></th>
    """
    # Spaltenüberschriften
    for c in alpha:
        html += f'<th id="colh_{c}">{c}</th>'
    html += '</tr>\n'
    # Zeilen
    for i, row in enumerate(alpha):
        html += f'<tr><th id="rowh_{row}">{row}</th>'
        for j in range(26):
            val = alpha[(i + j) % 26]
            html += f'<td id="cell_{i}_{j}" onclick="highlightVig({i},{j})">{val}</td>'
        html += '</tr>\n'
    html += '</table>'
    # JavaScript für Hervorhebung
    html += """
    <script>
    function highlightVig(row, col) {
        // Alle Zellen und Header zurücksetzen
        let t = document.getElementById("vig-table");
        for (let r=1; r<=26; r++) {
            t.rows[r].cells[0].classList.remove("vig-highlight-header");
            for (let c=1; c<=26; c++) {
                t.rows[0].cells[c].classList.remove("vig-highlight-header");
                t.rows[r].cells[c].classList.remove("vig-highlight");
            }
        }
        // Zeile und Spalte hervorheben
        for (let c=1; c<=26; c++) {
            t.rows[row+1].cells[c].classList.add("vig-highlight");
        }
        for (let r=1; r<=26; r++) {
            t.rows[r].cells[col+1].classList.add("vig-highlight");
        }
        // Header hervorheben
        t.rows[0].cells[col+1].classList.add("vig-highlight-header");
        t.rows[row+1].cells[0].classList.add("vig-highlight-header");
    }
    </script>
    """
    display(HTML(html))

# Aufruf in einer Codezelle: vigenere_quadrat_interaktiv()


def PrimzahlErkennen(Zahl_6, Zahl_11, Zahl_23, Zahl_31, Zahl_42, Zahl_63):
    """Prüft, ob die Antworten zu den Zahlen 6, 11, 23, 31, 42, 63 korrekt als Primzahl/Nicht-Primzahl angegeben wurden."""

    antwort_sus = [Zahl_6, Zahl_11, Zahl_23, Zahl_31, Zahl_42, Zahl_63]
    #print(antwort_sus)
    richtige_antwort = ["nein", "ja", "ja", "ja", "nein", "nein"]
    labels = ["Zahl_6", "Zahl_11", "Zahl_23", "Zahl_31", "Zahl_42", "Zahl_63"]

    is_correct_value = [a == r for a, r in zip(antwort_sus, richtige_antwort)]
    idx_wrong_values = [i for i, x in enumerate(is_correct_value) if not x]
    labels_wrong_values = [labels[i] for i in idx_wrong_values]

    if len(labels_wrong_values) == 0:
        print("✔ Super! Deine Lösungen sind alle richtig!")
    else:
        print("❗ Schade. Deine Lösungen sind leider noch nicht komplett richtig. Schau dir die Zahlen nochmals an.", file=sys.stderr)

    

def correctprime(p, q):
    """Prüft, ob p und q verschieden und Primzahlen sind."""
    """Prüft, ob p und q Primzahlen sind und verschieden sind."""
    def ist_primzahl(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    if p == q:
        print("❗ Die Zahlen dürfen nicht identisch sein.")
    elif not ist_primzahl(p):
        print(f"❗ {p} ist keine Primzahl.")
    elif not ist_primzahl(q):
        print(f"❗ {q} ist keine Primzahl.")
    else:
        print("✔ Beide Zahlen sind verschieden und Primzahlen!")

def product(p, q, N):
    """Prüft, ob N das Produkt aus p und q ist."""
    """Prüft, ob N das Produkt aus p und q ist."""
    if N == p * q:
             print(f"✔ {N} ist das Produkt von {p} und {q}.")
    else:
             print(f"❗ {N} ist nicht das Produkt von {p} und {q}. Bitte prüfe deine Berechnung.")

def primfaktorzerlegung(zerlegung_52, zerlegung_108):
    """Prüft Primfaktorzerlegung für 52 und 108."""
    # Prüft, ob die übergebenen Zerlegungen von 52 und 108 korrekt sind.
    # Die Zerlegungen sollen als Strings wie "2*2*13" bzw. "2*2*3*3*3" übergeben werden.

    # Hilfsfunktion: Wandelt String in Liste von Faktoren um
    def parse_faktoren(s):
        try:
            return sorted([int(x) for x in str(s).replace(" ", "").split("*")])
        except Exception:
            return []

    # Richtige Zerlegungen
    korrekt_52 = sorted([2, 2, 13])
    korrekt_108 = sorted([2, 2, 3, 3, 3])

    eingabe_52 = parse_faktoren(zerlegung_52)
    eingabe_108 = parse_faktoren(zerlegung_108)

    fehler = []
    if eingabe_52 != korrekt_52:
        fehler.append(f"❗ Primfaktorzerlegung von 52 ist falsch. Deine Eingabe: {zerlegung_52}. Richtig: 2*2*13")
    if eingabe_108 != korrekt_108:
        fehler.append(f"❗ Primfaktorzerlegung von 108 ist falsch. Deine Eingabe: {zerlegung_108}. Richtig: 2*2*3*3*3")

    if not fehler:
        print("✔ Beide Primfaktorzerlegungen sind korrekt!")
    else:
        for f in fehler:
            print(f)

def pruefe_ggT(ggT_16_32, ggT_3_17, ggT_30_50, ggT_12_27):
    """Prüft ggT-Aufgaben für verschiedene Zahlenpaare."""
    # Nutzt die in check vorhandene Funktion ggt_berechnen(a, b)
    korrekt = [
        ggt(16, 32),
        ggt(3, 17),
        ggt(30, 50),
        ggt(12, 27)
    ]
    eingaben = [ggT_16_32, ggT_3_17, ggT_30_50, ggT_12_27]
    zahlenpaare = [(16, 32), (3, 17), (30, 50), (12, 27)]
    alles_richtig = True
    for i in range(4):
        if str(eingaben[i]) != str(korrekt[i]):
            print(f"❌ ggT({zahlenpaare[i][0]},{zahlenpaare[i][1]}) ist falsch. Deine Eingabe: {eingaben[i]}. Richtig: {korrekt[i]}")
            alles_richtig = False
    if alles_richtig:
        print("✔ Alle ggT-Ergebnisse sind korrekt!")

def pruefe_public(e, N):
    """Prüft Public Key auf Gültigkeit."""
    # Nutzt vorhandene Funktionen: phi(N) und ggt(e, phi(N))
    try:
        phi_N = phi(N)
        if not (1 < e < phi_N):
            print(f"❌ Ungültig: e muss zwischen 1 und φ(N) liegen. Dein e: {e}, φ(N): {phi_N}")
            return
        if ggt(e, phi_N) != 1:
            print(f"❌ Ungültig: ggT(e, φ(N)) muss 1 sein. Dein ggT: {ggt(e, phi_N)}")
            return
        print(f"✔ Gültiger Public Key: (e, N) = ({e}, {N})")
    except Exception as ex:
        print(f"Fehler bei der Prüfung: {ex}")

def day(wochentag):
    """Prüft, ob der übergebene Wochentag korrekt 'Dienstag' ist."""
    """
    Prüft, ob der übergebene Wochentag korrekt 'Dienstag' ist (Groß-/Kleinschreibung egal).
  
    """
    if str(wochentag).strip().lower() == "dienstag":
        print("✔ Richtig! Wenn jetzt Montag ist, dann ist in 134 Tagen Dienstag.")
    else:
        print(f"❌ Falsch! Wenn heute Montag ist, dann ist in 134 Tagen nicht {wochentag}.")

def sport(zahl):
    """Prüft, ob die übergebene Zahl der Rest von 26 geteilt durch 11 ist."""
    """
    Prüft, ob die übergebene Zahl der Rest von 26 geteilt durch 11 ist.
    Gibt eine Meldung aus, ob die Antwort richtig oder falsch ist.
    """
    if zahl == 26 % 11:
        print("Richtig! 26 geteilt durch 11 ergibt Rest", 26 % 11)
    else:
        print("Falsch. Überlege noch einmal!")

def topf(zahl):
    """Gibt eine Meldung aus, ob die übergebene Zahl in der gleichen Restklasse wie 26 mod 11 ist."""
    """
    Gibt eine Meldung aus, ob die übergebene Zahl in der gleichen Restklasse wie 26 mod 11 ist.
    """
    if zahl % 11 == 26 % 11:
        print("Richtig! Die Zahl ist in der gleichen Restklasse wie 26 mod 11 (Rest 4).")
    else:
        print("Falsch. Diese Zahl ist nicht in der gleichen Restklasse wie 26 mod 11.")

def modulo2(Antwort1, Antwort2, Antwort3, Antwort4, Antwort5):
    """Prüft Modulo-2 Aufgaben."""
    if Antwort1 == 1 and Antwort2 == 1 and Antwort3 == 2 and Antwort4 == 3 and Antwort5 == 3:
        print("Alle Antworten sind korrekt!")
    else:
        print("Mindestens eine Antwort ist falsch. Bitte überprüfe deine Antworten.")

def rsa_message(m, N):
    """Verschlüsselt eine Nachricht m mit N."""
    if m < N:
        print("✔ Super! Du hast eine zulässige Nachricht gewählt.")
    else:
        print("❗ Diese Nachricht kann nicht gewählt werden. Wähle eine andere.", file=sys.stderr)

def rsa_chiphretext(c, m, e, N):
    """Prüft RSA-Chiffretext."""
    if c == pow(m, e, N):
        print("✔ Richtig! Der Geheimtext c stimmt mit m^e mod N überein.")
    else:
        print("❗ Falsch! Der Geheimtext c ist nicht korrekt. Prüfe deine Rechnung.")

def check_public(e, N):
    """Prüft, ob e eine natürliche Zahl zwischen 1 und phi(N) ist und ob ggT(e, phi(N))=1. Gibt Erfolgsmeldung oder Fehlermeldung aus."""
    try:
        phi_N = phi(N)
        if not (isinstance(e, int) and 1 < e < phi_N):
            print(f"❌ Fehler: e muss eine natürliche Zahl zwischen 1 und phi(N) sein. Dein e: {e}, phi(N): {phi_N}")
            return
        if ggt(e, phi_N) != 1:
            print(f"❌ Fehler: ggT(e, phi(N)) muss 1 sein. Dein ggT: {ggt(e, phi_N)}")
            return
        print(f"✔ Gültiger Public Key: (e, N) = ({e}, {N})")
    except Exception as ex:
        print(f"Fehler bei der Prüfung: {ex}")

def encrypt_text_rsa(e, N, Nachricht):
    """Verschlüsselt jeden Buchstaben der Nachricht mit RSA (e, N) und gibt die Liste der verschlüsselten Zahlen zurück."""
    result = []
    for char in Nachricht:
        m = ord(char)
        c = pow(m, e, N)
        result.append(c)
    print(f"RSA-verschlüsselte Nachricht: {result}")
    return result

def decrypt_text_rsa(d, N, Geheimtext):
    """Entschlüsselt eine mit RSA verschlüsselte Liste von Zahlen (Geheimtext) und gibt den Klartext als Zeichenkette zurück."""
    klartext = ""
    for c in Geheimtext:
        m = pow(c, d, N)
        klartext += chr(m)
    print(f"Entschlüsselter Text: {klartext}")
    return klartext
