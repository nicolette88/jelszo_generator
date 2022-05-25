import random
import string

melleknevek = [
    'álmos', 'lassú', 'büdi', 'nedves', 'duci', 'piros', 'narancs', 'sárga',
    'zöld', 'kék', 'lila', 'bolyhos', 'fehér', 'büszke', 'bátor'
]

fonevek = [
    'alma', 'dinó', 'labda', 'pirítós', 'mókus', 'sárkány', 'kalapács',
    'kacsa', 'panda', 'telefon', 'banán', 'tanító'
]

print('Üdv, itt a Jelszógenerátor!')

while True:
    for szamlalo in range(3):
        melleknev = random.choice(melleknevek)
        fonev = random.choice(fonevek)
        szam = random.randrange(0, 100)
        irasjel = random.choice(string.punctuation)

        jelszo = melleknev + fonev + str(szam) + irasjel
        print('Az új jelszó: %s' % jelszo)

    valasz = input('Szeretnél újabb jelszót? Válaszolj i vagy n-el: ')
    if valasz == 'n':
        break
