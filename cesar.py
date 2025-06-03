def cesar_chiffrer(texte, decalage):
    resultat = ''
    for c in texte:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultat += chr((ord(c) - base + decalage) % 26 + base)
        else:
            resultat += c
    return resultat

def cesar_dechiffrer(texte, decalage):
    return cesar_chiffrer(texte, -decalage)

action = input("Souhaitez-vous chiffrer ou déchiffrer ? (c/d) : ").lower()

if action not in ['c', 'd']:
    print("Choix invalide.")
else:
    texte = input("Entrez le texte : ")
    try:
        decalage = int(input("Entrez le décalage (nombre entier) : "))
    except ValueError:
        print("Le décalage doit être un nombre entier.")
        exit()

    if action == 'c':
        print("Texte chiffré :", cesar_chiffrer(texte, decalage))
    else:
        print("Texte déchiffré :", cesar_dechiffrer(texte, decalage))
