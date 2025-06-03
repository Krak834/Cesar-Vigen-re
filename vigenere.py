def vigenere_chiffrer(texte, cle):
    resultat = ''
    cle = cle.lower()
    j = 0
    for c in texte:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            decalage = ord(cle[j % len(cle)]) - ord('a')
            resultat += chr((ord(c) - base + decalage) % 26 + base)
            j += 1
        else:
            resultat += c
    return resultat

def vigenere_dechiffrer(texte, cle):
    resultat = ''
    cle = cle.lower()
    j = 0
    for c in texte:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            decalage = ord(cle[j % len(cle)]) - ord('a')
            resultat += chr((ord(c) - base - decalage) % 26 + base)
            j += 1
        else:
            resultat += c
    return resultat

action = input("Souhaitez-vous chiffrer ou déchiffrer ? (c/d) : ").lower()

if action not in ['c', 'd']:
    print("Choix invalide.")
else:
    texte = input("Entrez le texte : ")
    cle = input("Entrez la clé (lettres uniquement) : ")

    if not cle.isalpha():
        print("Clé invalide : elle doit contenir uniquement des lettres.")
    else:
        if action == 'c':
            print("Texte chiffré :", vigenere_chiffrer(texte, cle))
        else:
            print("Texte déchiffré :", vigenere_dechiffrer(texte, cle))
