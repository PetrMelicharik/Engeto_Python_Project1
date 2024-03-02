#Engeto_Python_Project1
#Textový analyzátor
#projekt_1.py: první projekt do Engeto Online Python Akademie
#author: Petr Melichařík
#email: petr.melicharik@seznam.cz
#discord: PetrMelicharik


#proměnné
uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

jmeno = input("uživatelské jméno:")
heslo = input("heslo:")

kontrola_hesla = uzivatele.get(jmeno)

seznam_slov = list()

pocet_slov = 0
slova_s_velkym_pismenem = 0
slova_velkym = 0
slova_malym = 0
pocet_cisel = 0
cisla = list()
delky_slov = dict()

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

#přihlášení uživatele a zvolení textu

if kontrola_hesla == heslo:
    print("-" * 55)
    print("Vítej v aplikaci,", jmeno)
    print("Máme zde 3 texty pro analýzu")
    print("-" * 55)
    zvoleny_text = input("Zvol číslo textu od 1 do 3:")

    if zvoleny_text.isnumeric() and int(zvoleny_text) in range(1, 4):
        rozdeleni_textu = list(texty[int(zvoleny_text) - 1].split())

#očištění slov
        for retezec in rozdeleni_textu:
            seznam_slov.append(retezec.strip(".").strip(","))

        for slovo in seznam_slov:
            pocet_slov = pocet_slov + 1
            if len(slovo) not in delky_slov:
                delky_slov[len(slovo)] = 1
            else:
                delky_slov[len(slovo)] = delky_slov[len(slovo)] + 1
            if slovo.istitle() and slovo.isalpha():
                slova_s_velkym_pismenem = slova_s_velkym_pismenem + 1
            elif slovo.isupper() and slovo.isalpha():
                slova_velkym = slova_velkym + 1
            elif slovo.islower() and slovo.isalpha():
                slova_malym = slova_malym + 1
            elif slovo.isdigit():
                pocet_cisel = pocet_cisel + 1
                cisla.append(int(slovo))

        print("-" * 55)
        print("V textu je", pocet_slov, "slov")
        print("V textu je", slova_s_velkym_pismenem, "slov s počátečním velkým písmenem")
        print("V textu je", slova_velkym, "slov, která jsou napsaná velkými písmeny")
        print("V textu je", slova_malym, "slov, která jsou napsaná malými písmeny")
        print("V textu je", pocet_cisel, "čísel")
        print("Součet všech čísel je", sum(cisla))
        print("-" * 55)
        print("Počet znaků|              Graf               |Počet slov")
        for delka in sorted(delky_slov):
            if delka < 10:
                print("        ", delka, "|", "*" * delky_slov[delka], " " * (30 - delky_slov[delka]), "|", delky_slov[delka])
            else:
                print("       ", delka, "|", "*" * delky_slov[delka], " " * (30 - delky_slov[delka]), "|",
                    delky_slov[delka])
    else:
        print("Neplatný vstup, je třeba zvolit číslo v rozmezí 1 - 3!!! Ukončuji program...")
else:
    print("username:", jmeno)
    print("password:", heslo)
    print("neregistrovaný uživatel, ukončuji program...")

