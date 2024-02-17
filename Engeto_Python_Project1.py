#proměnné
uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

jmeno = input("uživatelské jméno:")
heslo = input("heslo:")

kontrola_hesla = uzivatele.get(jmeno)

seznam_slov = list()

#texty
texty = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#přihlášení uživatele

if jmeno in uzivatele and kontrola_hesla == heslo:
    print("-" * 30)
    print("Vítej v aplikaci,", jmeno)
    print("Máme zde 3 texty pro analýzu")
    print("-" * 30)
    zvoleny_text = int(input("Zvol číslo textu od 1 do 3:"))
    rozdeleni_textu = list(texty[zvoleny_text - 1].split())

    for slovo in rozdeleni_textu:
        seznam_slov.append(slovo.strip(".").strip(","))

    print(seznam_slov)
else:
    print("username:", jmeno)
    print("password:", heslo)
    print("neregistrovaný uživatel, ukončuji program...")

