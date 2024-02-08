#proměnné
uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

jmeno = input("uživatelské jméno:")
heslo = input("heslo:")

kontrola_hesla = uzivatele.get(jmeno)

#přihlášení uživatele

if jmeno in uzivatele and kontrola_hesla == heslo:
    print("-" * 30)
    print("Vítej v aplikaci,", jmeno)
    print("Máme zde 3 texty pro analýzu")
    print("-" * 30)
    zvoleny_text = input("Zvol číslo textu od 1 do 3:")
    print(zvoleny_text)
else:
    print("username:", jmeno)
    print("password:", heslo)
    print("neregistrovaný uživatel, ukončuji program...")

