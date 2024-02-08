#proměnné
uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

jmeno = input("Dobrý den, zadejte prosím uživatelské jméno:")
heslo = input("Nyní zadejte heslo:")

kontrola_hesla = uzivatele.get(jmeno)

#přihlášení uživatele

if jmeno in uzivatele and kontrola_hesla == heslo:
    print("username:", jmeno)
    print("password:", heslo)
    print("-" * 30)
    print("Vítej v aplikaci", jmeno)
    print("Máme zde 3 texty pro analýzu")
    print("-" * 30)
else:
    print("username:", jmeno)
    print("password:", heslo)
    print("neregistrovaný uživatel, ukončuji program...")

